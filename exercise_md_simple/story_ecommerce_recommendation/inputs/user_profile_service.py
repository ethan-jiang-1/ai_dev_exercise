#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
User Profile Service for E-commerce Recommendation System
This module provides services to build and maintain user profiles for personalized recommendations.
"""

import os
import json
import time
import logging
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch, helpers
import redis

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class UserProfileService:
    """Service for managing user profiles for recommendation system"""
    
    def __init__(self):
        """Initialize the user profile service with necessary connections"""
        # Initialize Elasticsearch connection
        es_host = os.environ.get('ES_HOST', 'localhost')
        es_port = int(os.environ.get('ES_PORT', 9200))
        self.es = Elasticsearch([{'host': es_host, 'port': es_port}])
        
        # Initialize Redis connection for caching
        redis_host = os.environ.get('REDIS_HOST', 'localhost')
        redis_port = int(os.environ.get('REDIS_PORT', 6379))
        self.redis = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        
        # Redis cache TTL (2 hours)
        self.cache_ttl = 7200
        
        # ES index names
        self.user_profile_index = 'user_profiles'
        self.product_index = 'products'
        
        # Ensure indexes exist
        self._init_es_index()
        
        logger.info("UserProfileService initialized")
    
    def _init_es_index(self):
        """Initialize Elasticsearch indexes if they don't exist"""
        # Create user profile index if not exists
        if not self.es.indices.exists(index=self.user_profile_index):
            mappings = {
                "mappings": {
                    "properties": {
                        "user_id": {"type": "keyword"},
                        "interests": {
                            "type": "nested",
                            "properties": {
                                "category": {"type": "keyword"},
                                "score": {"type": "float"}
                            }
                        },
                        "preferences": {
                            "properties": {
                                "priceRange": {
                                    "properties": {
                                        "min": {"type": "float"},
                                        "max": {"type": "float"}
                                    }
                                },
                                "brands": {"type": "keyword"},
                                "features": {"type": "keyword"}
                            }
                        },
                        "behaviors": {
                            "properties": {
                                "browseCount": {"type": "integer"},
                                "purchaseCount": {"type": "integer"},
                                "averageOrderValue": {"type": "float"}
                            }
                        },
                        "embeddings": {"type": "dense_vector", "dims": 128},
                        "last_updated": {"type": "date"}
                    }
                }
            }
            self.es.indices.create(index=self.user_profile_index, body=mappings)
            logger.info(f"Created index {self.user_profile_index}")
        
        # Ensure product index exists (simple check)
        if not self.es.indices.exists(index=self.product_index):
            logger.warning(f"Product index {self.product_index} doesn't exist. Some features may not work properly.")
            
    def get_user_profile(self, user_id: str) -> Dict[str, Any]:
        """
        Get a user's profile. First checks cache, then database.
        Creates a default profile if none exists.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Dictionary containing user profile data
        """
        # Try to get from cache first
        cache_key = f"user_profile:{user_id}"
        cached_profile = self.redis.get(cache_key)
        
        if cached_profile:
            logger.debug(f"Cache hit for user {user_id}")
            return json.loads(cached_profile)
        
        # If not in cache, try to get from Elasticsearch
        try:
            response = self.es.get(index=self.user_profile_index, id=user_id)
            profile = response['_source']
            
            # Update cache
            self.redis.setex(cache_key, self.cache_ttl, json.dumps(profile))
            
            logger.debug(f"Fetched profile for user {user_id} from database")
            return profile
        
        except Exception as e:
            logger.info(f"No profile found for user {user_id}, creating default. Error: {str(e)}")
            
            # Create default profile
            profile = self._build_default_profile(user_id)
            
            # Save to database and cache
            self._save_profile(user_id, profile)
            
            return profile
    
    def _build_default_profile(self, user_id: str) -> Dict[str, Any]:
        """
        Create a default profile for new users
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            A dictionary with default profile values
        """
        current_time = datetime.now().isoformat()
        
        default_profile = {
            "user_id": user_id,
            "interests": [
                {"category": "popular", "score": 1.0},
                {"category": "trending", "score": 0.8}
            ],
            "preferences": {
                "priceRange": {"min": 0, "max": 1000},
                "brands": [],
                "features": []
            },
            "behaviors": {
                "browseCount": 0,
                "purchaseCount": 0,
                "averageOrderValue": 0
            },
            "recent_items": [],
            "last_updated": current_time
        }
        
        logger.info(f"Created default profile for user {user_id}")
        return default_profile
    
    def update_user_profile(self, user_id: str, event_data: Dict[str, Any]) -> bool:
        """
        Update a user's profile based on new event data
        
        Args:
            user_id: Unique identifier for the user
            event_data: Dictionary containing event information
            
        Returns:
            Boolean indicating success or failure
        """
        try:
            # Get current profile (creates default if none exists)
            profile = self.get_user_profile(user_id)
            
            # Get item information
            item_id = event_data.get('item_id')
            if not item_id:
                logger.warning(f"No item_id in event data for user {user_id}")
                return False
                
            item_info = self._get_item_info(item_id)
            if not item_info:
                logger.warning(f"No item info found for item {item_id}")
                return False
            
            # Update profile components
            event_type = event_data.get('event_type', 'view')
            
            # Update different aspects of the profile
            self._update_interests(profile, item_info, event_type)
            self._update_behaviors(profile, event_data, item_info)
            self._update_preferences(profile, item_info, event_type)
            
            # Add to recent items if not already there
            recent_items = profile.get('recent_items', [])
            if item_id not in [item['item_id'] for item in recent_items]:
                recent_items.append({
                    'item_id': item_id,
                    'timestamp': datetime.now().isoformat()
                })
                # Keep only latest 50 items
                profile['recent_items'] = recent_items[-50:]
            
            # Update timestamp
            profile['last_updated'] = datetime.now().isoformat()
            
            # Save updated profile
            self._save_profile(user_id, profile)
            
            logger.debug(f"Updated profile for user {user_id} based on {event_type} event")
            return True
            
        except Exception as e:
            logger.error(f"Error updating profile for user {user_id}: {str(e)}")
            return False
    
    def _get_item_info(self, item_id: str) -> Optional[Dict[str, Any]]:
        """Get item information from the product database"""
        try:
            response = self.es.get(index=self.product_index, id=item_id)
            return response['_source']
        except Exception as e:
            logger.warning(f"Error fetching item {item_id}: {str(e)}")
            return None
    
    def _update_interests(self, profile: Dict[str, Any], item_info: Dict[str, Any], event_type: str) -> None:
        """
        Update user interests based on item interaction
        
        Args:
            profile: User profile to update
            item_info: Information about the interacted item
            event_type: Type of interaction (view, click, add_to_cart, purchase)
        """
        # Initialize interests if not present
        if 'interests' not in profile:
            profile['interests'] = []
            
        # Create dictionary for faster lookups
        interests_dict = {interest['category']: interest for interest in profile['interests']}
        
        # Get categories from item
        categories = item_info.get('categories', [])
        if not categories:
            return
            
        # Event type weights (how much each event type affects interests)
        weights = {
            'view': 0.1,
            'click': 0.2,
            'add_to_cart': 0.5,
            'purchase': 1.0
        }
        weight = weights.get(event_type, 0.1)
        
        # Update interests for each category
        for category in categories:
            if category in interests_dict:
                # Update existing interest
                current_score = interests_dict[category]['score']
                # Apply exponential decay to prevent sudden large changes
                new_score = current_score + (weight * (1 - current_score))
                interests_dict[category]['score'] = round(min(new_score, 1.0), 2)
            else:
                # Add new interest
                interests_dict[category] = {'category': category, 'score': weight}
        
        # Decay other interests slightly
        decay_factor = 0.99
        for category in interests_dict:
            if category not in categories:
                interests_dict[category]['score'] *= decay_factor
        
        # Convert back to list and sort by score
        profile['interests'] = sorted(
            interests_dict.values(), 
            key=lambda x: x['score'], 
            reverse=True
        )
    
    def _update_behaviors(self, profile: Dict[str, Any], event_data: Dict[str, Any], item_info: Dict[str, Any]) -> None:
        """
        Update behavioral metrics based on event data
        
        Args:
            profile: User profile to update
            event_data: Data about the current event
            item_info: Information about the interacted item
        """
        # Initialize behaviors if not present
        if 'behaviors' not in profile:
            profile['behaviors'] = {
                'browseCount': 0,
                'purchaseCount': 0,
                'averageOrderValue': 0
            }
        
        event_type = event_data.get('event_type', 'view')
        
        # Update browse count for views
        if event_type == 'view':
            profile['behaviors']['browseCount'] += 1
        
        # Update purchase metrics
        elif event_type == 'purchase':
            profile['behaviors']['purchaseCount'] += 1
            
            # Update average order value
            current_aov = profile['behaviors']['averageOrderValue']
            purchase_count = profile['behaviors']['purchaseCount']
            item_price = item_info.get('price', 0)
            
            if purchase_count > 1:
                # Weighted average calculation
                profile['behaviors']['averageOrderValue'] = round(
                    ((current_aov * (purchase_count - 1)) + item_price) / purchase_count, 
                    2
                )
            else:
                # First purchase
                profile['behaviors']['averageOrderValue'] = item_price
    
    def _update_preferences(self, profile: Dict[str, Any], item_info: Dict[str, Any], event_type: str) -> None:
        """
        Update user preferences based on item interactions
        
        Args:
            profile: User profile to update
            item_info: Information about the interacted item
            event_type: Type of interaction (view, click, add_to_cart, purchase)
        """
        # Initialize preferences if not present
        if 'preferences' not in profile:
            profile['preferences'] = {
                'priceRange': {'min': 0, 'max': 0},
                'brands': [],
                'features': []
            }
        
        # Only significant interactions affect preferences
        if event_type not in ['add_to_cart', 'purchase']:
            return
            
        # Update price range preferences
        price = item_info.get('price', 0)
        if price > 0:
            current_min = profile['preferences']['priceRange']['min']
            current_max = profile['preferences']['priceRange']['max']
            
            # For first item, set both min and max
            if current_min == 0 and current_max == 0:
                profile['preferences']['priceRange']['min'] = price * 0.8
                profile['preferences']['priceRange']['max'] = price * 1.2
            else:
                # Update price range with 20% margin on either side
                # but ensure the range expands gradually
                new_min = min(current_min, price * 0.8)
                new_max = max(current_max, price * 1.2)
                
                # Apply smoothing to prevent wild swings
                alpha = 0.3  # Smoothing factor
                profile['preferences']['priceRange']['min'] = round(
                    (alpha * new_min) + ((1 - alpha) * current_min), 
                    2
                )
                profile['preferences']['priceRange']['max'] = round(
                    (alpha * new_max) + ((1 - alpha) * current_max), 
                    2
                )
        
        # Update brand preferences
        brand = item_info.get('attributes', {}).get('brand')
        if brand and brand not in profile['preferences']['brands']:
            profile['preferences']['brands'].append(brand)
            # Keep only top N brands
            profile['preferences']['brands'] = profile['preferences']['brands'][-5:]
        
        # Update feature preferences
        features = []
        attributes = item_info.get('attributes', {})
        
        # Extract meaningful features from attributes (simplified)
        for key, value in attributes.items():
            if key not in ['brand', 'id', 'name']:
                features.append(f"{key}:{value}")
        
        # Add features not already in preferences
        current_features = profile['preferences']['features']
        for feature in features:
            if feature not in current_features:
                current_features.append(feature)
        
        # Keep only top N features
        profile['preferences']['features'] = current_features[-10:]
    
    def _save_profile(self, user_id: str, profile: Dict[str, Any]) -> None:
        """
        Save profile to database and update cache
        
        Args:
            user_id: Unique identifier for the user
            profile: Profile data to save
        """
        try:
            # Save to Elasticsearch
            self.es.index(
                index=self.user_profile_index,
                id=user_id,
                body=profile,
                refresh=True
            )
            
            # Update cache
            cache_key = f"user_profile:{user_id}"
            self.redis.setex(cache_key, self.cache_ttl, json.dumps(profile))
            
            logger.debug(f"Saved profile for user {user_id}")
        
        except Exception as e:
            logger.error(f"Error saving profile for user {user_id}: {str(e)}")
    
    def batch_update_profiles(self) -> None:
        """
        Perform batch updates on user profiles
        This method is intended to be called by a scheduled job
        """
        try:
            # Get all profiles that haven't been updated in the last day
            query = {
                "query": {
                    "range": {
                        "last_updated": {
                            "lt": "now-1d"
                        }
                    }
                },
                "size": 1000
            }
            
            response = self.es.search(index=self.user_profile_index, body=query)
            
            profiles_to_update = response['hits']['hits']
            logger.info(f"Found {len(profiles_to_update)} profiles for batch update")
            
            for profile_doc in profiles_to_update:
                user_id = profile_doc['_id']
                profile = profile_doc['_source']
                
                # Perform any batch operations needed
                # For example, recalculate long-term interests or adjust preferences
                
                # Decay old interests slightly
                if 'interests' in profile:
                    for interest in profile['interests']:
                        interest['score'] *= 0.95
                
                # Update timestamp
                profile['last_updated'] = datetime.now().isoformat()
                
                # Save updated profile
                self._save_profile(user_id, profile)
            
            logger.info(f"Completed batch update for {len(profiles_to_update)} profiles")
            
        except Exception as e:
            logger.error(f"Error in batch profile update: {str(e)}")
    
    def find_similar_users(self, user_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Find users with similar interests and behaviors
        
        Args:
            user_id: User to find similar users for
            limit: Maximum number of similar users to return
            
        Returns:
            List of similar user profiles
        """
        try:
            # Get target user profile
            user_profile = self.get_user_profile(user_id)
            
            # Extract interests
            user_interests = {i['category']: i['score'] for i in user_profile.get('interests', [])}
            
            if not user_interests:
                logger.warning(f"No interests found for user {user_id}")
                return []
            
            # Build query to find users with similar interests
            should_clauses = []
            for category, score in user_interests.items():
                should_clauses.append({
                    "nested": {
                        "path": "interests",
                        "query": {
                            "bool": {
                                "must": [
                                    {"match": {"interests.category": category}},
                                    {"range": {"interests.score": {"gte": score * 0.7}}}
                                ]
                            }
                        },
                        "score_mode": "avg"
                    }
                })
            
            query = {
                "query": {
                    "bool": {
                        "must_not": [
                            {"term": {"user_id": user_id}}
                        ],
                        "should": should_clauses,
                        "minimum_should_match": 1
                    }
                },
                "size": limit
            }
            
            # Execute search
            response = self.es.search(index=self.user_profile_index, body=query)
            
            # Extract results
            similar_users = []
            for hit in response['hits']['hits']:
                similar_users.append({
                    "user_id": hit['_source']['user_id'],
                    "similarity_score": hit['_score'],
                    "interests": hit['_source'].get('interests', [])
                })
            
            logger.info(f"Found {len(similar_users)} similar users for user {user_id}")
            return similar_users
            
        except Exception as e:
            logger.error(f"Error finding similar users for {user_id}: {str(e)}")
            return []
    
    def generate_user_embeddings(self, user_id: str) -> Optional[np.ndarray]:
        """
        Generate embedding vector for a user based on their profile
        
        Args:
            user_id: User to generate embeddings for
            
        Returns:
            Numpy array containing user embedding vector
        """
        try:
            # Get user profile
            profile = self.get_user_profile(user_id)
            
            # Get recent items
            recent_items = self._get_user_recent_items(user_id, limit=20)
            
            if not recent_items:
                logger.warning(f"No recent items for user {user_id}, can't generate embeddings")
                return None
            
            # Extract item embeddings (assuming items have embeddings field)
            item_embeddings = []
            for item in recent_items:
                item_info = self._get_item_info(item['item_id'])
                if item_info and 'embeddings' in item_info:
                    # Append embedding with time decay based on recency
                    time_diff = datetime.now() - datetime.fromisoformat(item['timestamp'])
                    days_old = min(time_diff.days, 30)  # Cap at 30 days
                    recency_weight = 1.0 - (days_old / 30.0)
                    
                    weighted_embedding = np.array(item_info['embeddings']) * recency_weight
                    item_embeddings.append(weighted_embedding)
            
            if not item_embeddings:
                logger.warning(f"No item embeddings available for user {user_id}")
                return None
            
            # Average item embeddings to get user embedding
            user_embedding = np.mean(item_embeddings, axis=0)
            
            # Store embedding in user profile
            profile['embeddings'] = user_embedding.tolist()
            self._save_profile(user_id, profile)
            
            logger.debug(f"Generated embeddings for user {user_id}")
            return user_embedding
            
        except Exception as e:
            logger.error(f"Error generating embeddings for user {user_id}: {str(e)}")
            return None
    
    def _get_user_recent_items(self, user_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Get recent items a user has interacted with
        
        Args:
            user_id: User to get recent items for
            limit: Maximum number of items to return
            
        Returns:
            List of recent item interactions
        """
        try:
            # Get from user profile first if available
            profile = self.get_user_profile(user_id)
            recent_items = profile.get('recent_items', [])
            
            if recent_items:
                # Sort by timestamp (most recent first)
                sorted_items = sorted(
                    recent_items, 
                    key=lambda x: x.get('timestamp', ''), 
                    reverse=True
                )
                return sorted_items[:limit]
            
            # If not available in profile, could query from events database
            # This is a simplified implementation
            logger.warning(f"No recent items found in profile for user {user_id}")
            return []
            
        except Exception as e:
            logger.error(f"Error getting recent items for user {user_id}: {str(e)}")
            return []
    
    def calculate_category_affinity(self, user_id: str) -> Dict[str, float]:
        """
        Calculate user affinity scores for each product category
        
        Args:
            user_id: User to calculate affinities for
            
        Returns:
            Dictionary mapping category IDs to affinity scores
        """
        try:
            # Get user profile
            profile = self.get_user_profile(user_id)
            
            # Get interests directly
            interests = profile.get('interests', [])
            
            # Convert to dictionary for easier access
            category_scores = {}
            for interest in interests:
                category = interest.get('category')
                score = interest.get('score', 0)
                if category:
                    category_scores[category] = score
            
            # Normalize scores
            if category_scores:
                max_score = max(category_scores.values())
                if max_score > 0:
                    for category in category_scores:
                        category_scores[category] /= max_score
            
            logger.debug(f"Calculated category affinities for user {user_id}")
            return category_scores
            
        except Exception as e:
            logger.error(f"Error calculating category affinity for user {user_id}: {str(e)}")
            return {}
    
    def close(self):
        """Close database connections"""
        try:
            self.redis.close()
            logger.info("Closed Redis connection")
        except Exception as e:
            logger.error(f"Error closing Redis connection: {str(e)}")


def create_service():
    """Factory function to create and initialize a UserProfileService instance"""
    service = UserProfileService()
    return service

if __name__ == "__main__":
    # Example usage
    service = create_service()
    
    # Test user profile retrieval
    profile = service.get_user_profile("test_user_1")
    print(f"Retrieved profile: {json.dumps(profile, indent=2)}")
    
    # Test update with a sample event
    event_data = {
        "user_id": "test_user_1",
        "event_type": "view",
        "item_id": "P12345",
        "timestamp": datetime.now().isoformat()
    }
    service.update_user_profile("test_user_1", event_data)
    
    service.close()
