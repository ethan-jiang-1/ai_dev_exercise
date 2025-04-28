#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Recommendation API Service for E-commerce Recommendation System
This module provides REST endpoints for product recommendations.
"""

import os
import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Union

from fastapi import FastAPI, HTTPException, Query, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

import redis
from elasticsearch import Elasticsearch

# Import recommendation algorithms
from recommendation_algorithms import (
    RecommendationFactory,
    RecommendationAlgorithm
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="E-commerce Recommendation API",
    description="API for product recommendations in e-commerce platform",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
REDIS_TTL = int(os.environ.get("REDIS_TTL", 3600))  # 1 hour cache

ES_HOST = os.environ.get("ES_HOST", "localhost")
ES_PORT = int(os.environ.get("ES_PORT", 9200))

# Models for request/response
class RecommendationRequest(BaseModel):
    user_id: str = Field(..., description="User ID for personalized recommendations")
    scene_id: str = Field(..., description="Scene ID (home, detail, cart, etc.)")
    item_id: Optional[str] = Field(None, description="Current item ID (for detail page)")
    category_id: Optional[str] = Field(None, description="Category ID (for category page)")
    count: int = Field(10, description="Number of recommendations to return", ge=1, le=50)
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters to apply")

class RecommendedItem(BaseModel):
    item_id: str = Field(..., description="Product ID")
    name: str = Field(..., description="Product name")
    image_url: str = Field(..., description="Product image URL")
    price: float = Field(..., description="Current price")
    original_price: Optional[float] = Field(None, description="Original price if on sale")
    score: float = Field(..., description="Recommendation score")
    reason: Optional[str] = Field(None, description="Recommendation reason")

class RecommendationResponse(BaseModel):
    recommendations: List[RecommendedItem] = Field(..., description="List of recommended items")
    request_id: str = Field(..., description="Unique request ID for tracking")
    algorithm: str = Field(..., description="Algorithm used for recommendations")
    took_ms: int = Field(..., description="Time taken to generate recommendations in ms")

# Feature provider class to connect to data sources
class FeatureProvider:
    """Provides features and data for recommendation algorithms"""
    
    def __init__(self):
        """Initialize feature provider with connections to data sources"""
        # Connect to Redis
        self.redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )
        
        # Connect to Elasticsearch
        self.es = Elasticsearch([{
            'host': ES_HOST,
            'port': ES_PORT
        }])
        
        # Index names
        self.product_index = "products"
        self.user_events_index = "user_events"
        self.user_profile_index = "user_profiles"
        
        logger.info("FeatureProvider initialized")
    
    def get_product_details(self, product_ids: List[str]) -> Dict[str, Dict[str, Any]]:
        """Get product details for a list of product IDs"""
        if not product_ids:
            return {}
        
        # Try to get from cache first
        cache_key = f"product_details:{','.join(product_ids)}"
        cached_data = self.redis.get(cache_key)
        
        if cached_data:
            return json.loads(cached_data)
        
        # If not in cache, query from Elasticsearch
        try:
            query = {
                "query": {
                    "terms": {
                        "_id": product_ids
                    }
                },
                "size": len(product_ids)
            }
            
            response = self.es.search(index=self.product_index, body=query)
            
            # Extract products
            products = {}
            for hit in response["hits"]["hits"]:
                product_id = hit["_id"]
                product_data = hit["_source"]
                products[product_id] = product_data
            
            # Cache results
            self.redis.setex(cache_key, REDIS_TTL, json.dumps(products))
            
            return products
            
        except Exception as e:
            logger.error(f"Error fetching product details: {str(e)}")
            return {}
    
    def get_user_profile(self, user_id: str) -> Dict[str, Any]:
        """Get user profile from user profile service"""
        try:
            response = self.es.get(index=self.user_profile_index, id=user_id)
            return response["_source"]
        except Exception as e:
            logger.warning(f"User profile not found for {user_id}: {str(e)}")
            return {}
    
    def get_user_items(self, user_id: str, event_type: Optional[str] = None) -> List[str]:
        """Get items a user has interacted with"""
        try:
            must_clauses = [
                {"term": {"user_id": user_id}}
            ]
            
            if event_type:
                must_clauses.append({"term": {"event_type": event_type}})
            
            query = {
                "query": {
                    "bool": {
                        "must": must_clauses
                    }
                },
                "size": 100,
                "_source": ["item_id"],
                "sort": [{"timestamp": {"order": "desc"}}]
            }
            
            response = self.es.search(index=self.user_events_index, body=query)
            
            return [hit["_source"]["item_id"] for hit in response["hits"]["hits"]]
            
        except Exception as e:
            logger.error(f"Error fetching user items: {str(e)}")
            return []
    
    def get_popular_items(self, category: Optional[str] = None, limit: int = 100) -> List[tuple]:
        """Get popular items, optionally filtered by category"""
        try:
            # Cache key
            cache_key = f"popular_items:{category or 'all'}:{limit}"
            cached_data = self.redis.get(cache_key)
            
            if cached_data:
                return json.loads(cached_data)
            
            # Build query
            must_clauses = []
            if category:
                must_clauses.append({"term": {"categories": category}})
            
            query = {
                "query": {
                    "bool": {
                        "must": must_clauses if must_clauses else {"match_all": {}}
                    }
                },
                "size": limit,
                "sort": [{"popularity_score": {"order": "desc"}}]
            }
            
            response = self.es.search(index=self.product_index, body=query)
            
            # Format results as (item_id, score) tuples
            popular_items = []
            for hit in response["hits"]["hits"]:
                product_id = hit["_id"]
                score = hit["_source"].get("popularity_score", 0)
                popular_items.append((product_id, score))
            
            # Cache results
            self.redis.setex(cache_key, REDIS_TTL, json.dumps(popular_items))
            
            return popular_items
            
        except Exception as e:
            logger.error(f"Error fetching popular items: {str(e)}")
            return []
    
    def get_categories(self) -> List[str]:
        """Get all product categories"""
        try:
            # Use aggregation to get all categories
            query = {
                "size": 0,
                "aggs": {
                    "categories": {
                        "terms": {
                            "field": "categories",
                            "size": 1000
                        }
                    }
                }
            }
            
            response = self.es.search(index=self.product_index, body=query)
            
            return [bucket["key"] for bucket in response["aggregations"]["categories"]["buckets"]]
            
        except Exception as e:
            logger.error(f"Error fetching categories: {str(e)}")
            return []
    
    def get_all_items(self) -> List[Dict[str, Any]]:
        """Get all items with their features (for content-based filtering)"""
        try:
            # Check cache first
            cache_key = "all_items"
            cached_data = self.redis.get(cache_key)
            
            if cached_data:
                return json.loads(cached_data)
            
            # Scroll through all products (this could be resource-intensive)
            query = {
                "query": {"match_all": {}},
                "size": 1000
            }
            
            response = self.es.search(
                index=self.product_index,
                body=query,
                scroll="2m"
            )
            
            scroll_id = response["_scroll_id"]
            results = []
            
            # Get initial results
            for hit in response["hits"]["hits"]:
                item = hit["_source"]
                item["id"] = hit["_id"]  # Add ID to the item
                results.append(item)
            
            # Continue scrolling until done
            while len(response["hits"]["hits"]) > 0:
                response = self.es.scroll(scroll_id=scroll_id, scroll="2m")
                scroll_id = response["_scroll_id"]
                
                for hit in response["hits"]["hits"]:
                    item = hit["_source"]
                    item["id"] = hit["_id"]
                    results.append(item)
            
            # Cache results (with reasonable TTL, e.g., 1 day)
            self.redis.setex(cache_key, 86400, json.dumps(results))
            
            return results
            
        except Exception as e:
            logger.error(f"Error fetching all items: {str(e)}")
            return []
    
    def get_purchase_data(self) -> List[tuple]:
        """Get purchase data for collaborative filtering"""
        try:
            # Check cache first
            cache_key = "purchase_data"
            cached_data = self.redis.get(cache_key)
            
            if cached_data:
                return json.loads(cached_data)
            
            # Query purchase events
            query = {
                "query": {
                    "term": {
                        "event_type": "purchase"
                    }
                },
                "size": 10000,
                "_source": ["user_id", "item_id"]
            }
            
            response = self.es.search(
                index=self.user_events_index,
                body=query
            )
            
            # Extract (user_id, item_id) tuples
            purchase_data = []
            for hit in response["hits"]["hits"]:
                source = hit["_source"]
                purchase_data.append((source["user_id"], source["item_id"]))
            
            # Cache results
            self.redis.setex(cache_key, REDIS_TTL, json.dumps(purchase_data))
            
            return purchase_data
            
        except Exception as e:
            logger.error(f"Error fetching purchase data: {str(e)}")
            return []
    
    def get_interaction_data(self) -> List[tuple]:
        """Get user-item interaction data for collaborative filtering"""
        try:
            # Check cache first
            cache_key = "interaction_data"
            cached_data = self.redis.get(cache_key)
            
            if cached_data:
                return json.loads(cached_data)
            
            # Query all interaction events
            query = {
                "query": {
                    "terms": {
                        "event_type": ["view", "add_to_cart", "purchase"]
                    }
                },
                "size": 10000,
                "_source": ["user_id", "item_id", "event_type"]
            }
            
            response = self.es.search(
                index=self.user_events_index,
                body=query
            )
            
            # Extract (user_id, item_id, event_type) tuples
            interaction_data = []
            for hit in response["hits"]["hits"]:
                source = hit["_source"]
                interaction_data.append((
                    source["user_id"],
                    source["item_id"],
                    source["event_type"]
                ))
            
            # Cache results
            self.redis.setex(cache_key, REDIS_TTL, json.dumps(interaction_data))
            
            return interaction_data
            
        except Exception as e:
            logger.error(f"Error fetching interaction data: {str(e)}")
            return []
    
    def close(self):
        """Close connections"""
        try:
            self.redis.close()
            logger.info("Closed Redis connection")
        except Exception as e:
            logger.error(f"Error closing Redis connection: {str(e)}")

# Recommendation service
class RecommendationService:
    """Service to generate recommendations using various algorithms"""
    
    def __init__(self):
        """Initialize recommendation service"""
        self.feature_provider = FeatureProvider()
        
        # Initialize recommenders
        self.recommenders = {}
        self._init_recommenders()
        
        # Scene to algorithm mapping
        self.scene_algorithms = {
            "home": "hybrid",
            "detail": "hybrid",
            "cart": "hybrid",
            "category": "hybrid",
            "search": "hybrid"
        }
        
        logger.info("RecommendationService initialized")
    
    def _init_recommenders(self):
        """Initialize recommendation algorithms"""
        # Basic recommenders
        self.recommenders["popular_items"] = RecommendationFactory.create_recommender("popular_items")
        self.recommenders["content_based"] = RecommendationFactory.create_recommender("content_based")
        self.recommenders["item_cf"] = RecommendationFactory.create_recommender("item_cf")
        self.recommenders["user_cf"] = RecommendationFactory.create_recommender("user_cf")
        
        # Hybrid recommender with custom weights
        hybrid_config = {
            "context_weights": {
                "home": {
                    "user_cf": 0.5,
                    "popular_items": 0.5
                },
                "detail": {
                    "content_based": 0.6,
                    "item_cf": 0.4
                },
                "cart": {
                    "item_cf": 0.7,
                    "popular_items": 0.3
                },
                "category": {
                    "user_cf": 0.4,
                    "popular_items": 0.3,
                    "content_based": 0.3
                },
                "search": {
                    "user_cf": 0.4,
                    "content_based": 0.6
                }
            }
        }
        self.recommenders["hybrid"] = RecommendationFactory.create_recommender("hybrid", hybrid_config)
    
    def get_recommendations(self, request: RecommendationRequest) -> RecommendationResponse:
        """
        Generate recommendations based on the request
        
        Args:
            request: Recommendation request object
            
        Returns:
            Recommendation response with recommended items
        """
        start_time = time.time()
        
        # Generate a unique request ID
        request_id = f"rec_{int(start_time)}_{request.user_id}_{request.scene_id}"
        
        # Check cache for this exact request
        cache_key = f"rec:{request.user_id}:{request.scene_id}:{request.item_id or ''}:{request.count}"
        cached_response = self.feature_provider.redis.get(cache_key)
        
        if cached_response:
            response = json.loads(cached_response)
            # Update timing and request ID
            response["request_id"] = request_id
            response["took_ms"] = int((time.time() - start_time) * 1000)
            return RecommendationResponse(**response)
        
        # Get algorithm for this scene
        algorithm_name = self.scene_algorithms.get(request.scene_id, "hybrid")
        algorithm = self.recommenders[algorithm_name]
        
        # Prepare context for algorithm
        context = {
            "scene": request.scene_id,
            "item_id": request.item_id,
            "category_id": request.category_id,
            "count": request.count,
            "filters": request.filters
        }
        
        # Get raw recommendations
        raw_recommendations = algorithm.recommend(
            request.user_id,
            context,
            self.feature_provider
        )
        
        # Extract product IDs
        product_ids = [rec["item_id"] for rec in raw_recommendations]
        
        # Get product details
        product_details = self.feature_provider.get_product_details(product_ids)
        
        # Combine recommendations with product details
        recommendations = []
        for rec in raw_recommendations:
            product_id = rec["item_id"]
            if product_id in product_details:
                product = product_details[product_id]
                
                # Create recommendation item
                item = RecommendedItem(
                    item_id=product_id,
                    name=product.get("name", "Unknown Product"),
                    image_url=product.get("images", [""])[0],
                    price=product.get("price", 0.0),
                    original_price=product.get("original_price"),
                    score=rec["score"],
                    reason=rec.get("reason")
                )
                recommendations.append(item)
        
        # Create response
        elapsed_ms = int((time.time() - start_time) * 1000)
        response = RecommendationResponse(
            recommendations=recommendations,
            request_id=request_id,
            algorithm=algorithm.name,
            took_ms=elapsed_ms
        )
        
        # Cache response
        self.feature_provider.redis.setex(
            cache_key,
            REDIS_TTL,
            json.dumps(response.dict())
        )
        
        return response
    
    def close(self):
        """Close connections"""
        self.feature_provider.close()

# Dependency to get recommendation service
def get_recommendation_service():
    """Get or create recommendation service instance"""
    service = RecommendationService()
    try:
        yield service
    finally:
        service.close()

# API endpoints
@app.post("/api/recommendations", response_model=RecommendationResponse)
async def recommend(
    request: RecommendationRequest,
    service: RecommendationService = Depends(get_recommendation_service),
    user_agent: Optional[str] = Header(None)
):
    """Generate recommendations based on user, scene, and context"""
    try:
        logger.info(f"Recommendation request: {request.dict()}")
        response = service.get_recommendations(request)
        return response
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 