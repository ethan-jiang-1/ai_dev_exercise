#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Recommendation Algorithms for E-commerce Recommendation System
This module implements various recommendation algorithms for product recommendations.
"""

import os
import json
import logging
import numpy as np
import pandas as pd
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RecommendationAlgorithm:
    """Base class for recommendation algorithms"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize recommendation algorithm with configuration"""
        self.config = config or {}
        self.name = "base"
    
    def recommend(self, user_id: str, context: Dict[str, Any], feature_provider) -> List[Dict[str, Any]]:
        """
        Generate recommendations based on user ID and context
        
        Args:
            user_id: User ID to generate recommendations for
            context: Context information (e.g., current item, category)
            feature_provider: Provider for user and item features
            
        Returns:
            List of recommended items with scores
        """
        raise NotImplementedError("Subclasses must implement recommend method")
    
    def _format_recommendations(self, item_scores: List[Tuple[str, float]], reason: str = None) -> List[Dict[str, Any]]:
        """
        Format raw recommendations into standard output format
        
        Args:
            item_scores: List of (item_id, score) tuples
            reason: Optional reason for the recommendation
            
        Returns:
            List of recommendation objects
        """
        recommendations = []
        for item_id, score in item_scores:
            rec = {
                "item_id": item_id,
                "score": round(float(score), 4)
            }
            if reason:
                rec["reason"] = reason
            recommendations.append(rec)
        
        return recommendations


class PopularItemsRecommender(RecommendationAlgorithm):
    """Recommends popular items"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize popular items recommender"""
        super().__init__(config)
        self.name = "popular_items"
        self.popular_items = []
        self.category_popular_items = {}
        self.last_updated = None
        self.update_interval = self.config.get("update_interval_hours", 24)
    
    def recommend(self, user_id: str, context: Dict[str, Any], feature_provider) -> List[Dict[str, Any]]:
        """Recommend popular items, optionally filtered by category"""
        # Check if popular items need updating
        current_time = datetime.now()
        if self.last_updated is None or (current_time - self.last_updated).total_seconds() > self.update_interval * 3600:
            self._update_popular_items(feature_provider)
        
        # Get recommendation count
        count = context.get("count", 10)
        
        # Get category if specified
        category_id = context.get("category_id")
        
        if category_id and category_id in self.category_popular_items:
            # Get popular items for the specific category
            items = self.category_popular_items[category_id][:count]
            reason = f"热门{category_id}商品"
        else:
            # Get overall popular items
            items = self.popular_items[:count]
            reason = "热门商品"
        
        return self._format_recommendations(items, reason)
    
    def _update_popular_items(self, feature_provider):
        """Update the list of popular items"""
        try:
            # In a real system, this would call feature_provider to get popularity data
            # Here we use a simplified approach with static data for illustration
            
            # Get overall popular items
            self.popular_items = feature_provider.get_popular_items(limit=100)
            
            # Get popular items by category
            for category in feature_provider.get_categories():
                self.category_popular_items[category] = feature_provider.get_popular_items(
                    category=category, limit=50
                )
            
            self.last_updated = datetime.now()
            logger.info(f"Updated popular items, found {len(self.popular_items)} overall popular items")
            
        except Exception as e:
            logger.error(f"Error updating popular items: {str(e)}")


class ContentBasedRecommender(RecommendationAlgorithm):
    """Content-based recommendation using product attributes"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize content-based recommender"""
        super().__init__(config)
        self.name = "content_based"
        self.vectorizer = TfidfVectorizer(
            max_features=5000, 
            stop_words='english',
            ngram_range=(1, 2)
        )
        self.item_vectors = {}
        self.item_features = {}
        self.last_updated = None
        self.update_interval = self.config.get("update_interval_hours", 24)
    
    def recommend(self, user_id: str, context: Dict[str, Any], feature_provider) -> List[Dict[str, Any]]:
        """
        Generate recommendations based on content similarity to a reference item
        
        Args:
            user_id: User ID (not used in content-based recommendations)
            context: Must contain 'item_id' to find similar items
            feature_provider: Provider for item features
            
        Returns:
            List of similar items with similarity scores
        """
        # Check if vectors need updating
        current_time = datetime.now()
        if self.last_updated is None or (current_time - self.last_updated).total_seconds() > self.update_interval * 3600:
            self._update_item_vectors(feature_provider)
        
        # Get item ID from context
        item_id = context.get("item_id")
        if not item_id:
            logger.warning("No item_id provided for content-based recommendation")
            return []
        
        # Check if we have vectors for this item
        if item_id not in self.item_vectors:
            logger.warning(f"No vector found for item {item_id}")
            return []
        
        # Get recommendation count
        count = context.get("count", 6)
        
        # Compute similarities
        item_vector = self.item_vectors[item_id]
        
        similarities = []
        for other_id, other_vector in self.item_vectors.items():
            if other_id != item_id:
                similarity = cosine_similarity([item_vector], [other_vector])[0][0]
                similarities.append((other_id, similarity))
        
        # Sort by similarity (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Get top N similar items
        similar_items = similarities[:count]
        
        # Get the item name for personalized reason
        item_name = self.item_features.get(item_id, {}).get("name", "当前商品")
        reason = f"与「{item_name}」相似"
        
        return self._format_recommendations(similar_items, reason)
    
    def _update_item_vectors(self, feature_provider):
        """Update item vectors for similarity calculation"""
        try:
            # Get all items with their features
            items = feature_provider.get_all_items()
            
            # Extract textual features for each item
            item_texts = {}
            for item in items:
                item_id = item["id"]
                
                # Store item features for later use
                self.item_features[item_id] = item
                
                # Combine relevant text fields
                text_features = [
                    item.get("name", ""),
                    item.get("description", ""),
                    " ".join(item.get("categories", [])),
                ]
                
                # Add attributes as features
                attrs = item.get("attributes", {})
                for attr_key, attr_value in attrs.items():
                    if isinstance(attr_value, str):
                        text_features.append(attr_value)
                
                item_texts[item_id] = " ".join(text_features).lower()
            
            # Fit vectorizer
            corpus = list(item_texts.values())
            if not corpus:
                logger.warning("No items found to vectorize")
                return
                
            X = self.vectorizer.fit_transform(corpus)
            
            # Store vectors by item ID
            for idx, item_id in enumerate(item_texts.keys()):
                self.item_vectors[item_id] = X[idx].toarray()[0]
            
            self.last_updated = datetime.now()
            logger.info(f"Updated content vectors for {len(self.item_vectors)} items")
            
        except Exception as e:
            logger.error(f"Error updating item vectors: {str(e)}")


class ItemCollaborativeFilteringRecommender(RecommendationAlgorithm):
    """Item-based collaborative filtering recommender"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize item-based CF recommender"""
        super().__init__(config)
        self.name = "item_cf"
        self.item_similarities = {}
        self.last_updated = None
        self.update_interval = self.config.get("update_interval_hours", 24)
        
        # Minimum number of common users for similarity calculation
        self.min_common_users = self.config.get("min_common_users", 3)
    
    def recommend(self, user_id: str, context: Dict[str, Any], feature_provider) -> List[Dict[str, Any]]:
        """
        Generate recommendations based on collaborative filtering
        
        Args:
            user_id: User ID (used to filter out already purchased items)
            context: Context information, may contain 'item_id' for item-to-item recommendations
            feature_provider: Provider for user interaction data
            
        Returns:
            List of recommended items with scores
        """
        # Check if similarities need updating
        current_time = datetime.now()
        if self.last_updated is None or (current_time - self.last_updated).total_seconds() > self.update_interval * 3600:
            self._update_item_similarities(feature_provider)
        
        # Get recommendation count
        count = context.get("count", 6)
        
        # Check if we're doing item-to-item recommendation or user-based recommendation
        item_id = context.get("item_id")
        
        if item_id:
            # Item-to-item recommendation
            recommendations = self._recommend_similar_items(item_id, count)
            reason = "经常一起购买"
            
        else:
            # User-based recommendation based on purchase history
            recommendations = self._recommend_for_user(user_id, feature_provider, count)
            reason = "根据您的购买记录推荐"
        
        return self._format_recommendations(recommendations, reason)
    
    def _recommend_similar_items(self, item_id: str, count: int) -> List[Tuple[str, float]]:
        """Recommend items similar to the given item"""
        if item_id not in self.item_similarities:
            return []
        
        # Get similar items and sort by similarity
        similar_items = self.item_similarities[item_id].items()
        sorted_items = sorted(similar_items, key=lambda x: x[1], reverse=True)
        
        return sorted_items[:count]
    
    def _recommend_for_user(self, user_id: str, feature_provider, count: int) -> List[Tuple[str, float]]:
        """Recommend items for a user based on their purchase history"""
        # Get user's purchase history
        user_items = feature_provider.get_user_items(user_id, event_type="purchase")
        
        if not user_items:
            # If user has no purchases, try with view history
            user_items = feature_provider.get_user_items(user_id, event_type="view")
            
        if not user_items:
            # New user, no history
            return []
        
        # Calculate score for each candidate item
        item_scores = {}
        
        for user_item in user_items:
            if user_item in self.item_similarities:
                for candidate_item, similarity in self.item_similarities[user_item].items():
                    # Don't recommend items the user already interacted with
                    if candidate_item in user_items:
                        continue
                    
                    # Accumulate similarity scores
                    if candidate_item in item_scores:
                        item_scores[candidate_item] += similarity
                    else:
                        item_scores[candidate_item] = similarity
        
        # Sort by score
        sorted_items = sorted(item_scores.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_items[:count]
    
    def _update_item_similarities(self, feature_provider):
        """Update item similarity matrix based on co-purchase data"""
        try:
            # Get purchase data: list of (user_id, item_id) tuples
            purchase_data = feature_provider.get_purchase_data()
            
            # Convert to DataFrame for easier processing
            df = pd.DataFrame(purchase_data, columns=["user_id", "item_id"])
            
            # Create user-item matrix (purchase count)
            user_item_matrix = df.groupby(["user_id", "item_id"]).size().unstack().fillna(0)
            
            # Calculate item-item similarity matrix
            item_ids = user_item_matrix.columns
            
            for i, item1 in enumerate(item_ids):
                if item1 not in self.item_similarities:
                    self.item_similarities[item1] = {}
                
                for item2 in item_ids[i+1:]:
                    # Get users who purchased each item
                    users_item1 = set(user_item_matrix[item1][user_item_matrix[item1] > 0].index)
                    users_item2 = set(user_item_matrix[item2][user_item_matrix[item2] > 0].index)
                    
                    # Calculate Jaccard similarity
                    common_users = users_item1.intersection(users_item2)
                    
                    if len(common_users) >= self.min_common_users:
                        similarity = len(common_users) / len(users_item1.union(users_item2))
                        
                        # Store similarity (symmetric)
                        self.item_similarities[item1][item2] = similarity
                        
                        if item2 not in self.item_similarities:
                            self.item_similarities[item2] = {}
                        self.item_similarities[item2][item1] = similarity
            
            self.last_updated = datetime.now()
            logger.info(f"Updated item similarities for {len(self.item_similarities)} items")
            
        except Exception as e:
            logger.error(f"Error updating item similarities: {str(e)}")


class UserCollaborativeFilteringRecommender(RecommendationAlgorithm):
    """User-based collaborative filtering recommender"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize user-based CF recommender"""
        super().__init__(config)
        self.name = "user_cf"
        self.user_similarities = {}
        self.user_item_matrix = None
        self.last_updated = None
        self.update_interval = self.config.get("update_interval_hours", 12)
        
        # Minimum similarity for user neighbors
        self.min_similarity = self.config.get("min_similarity", 0.1)
        
        # Maximum number of neighbors to consider
        self.max_neighbors = self.config.get("max_neighbors", 50)
    
    def recommend(self, user_id: str, context: Dict[str, Any], feature_provider) -> List[Dict[str, Any]]:
        """
        Generate recommendations using user-based collaborative filtering
        
        Args:
            user_id: User ID to generate recommendations for
            context: Context information
            feature_provider: Provider for user interaction data
            
        Returns:
            List of recommended items with scores
        """
        # Check if similarities need updating
        current_time = datetime.now()
        if self.last_updated is None or (current_time - self.last_updated).total_seconds() > self.update_interval * 3600:
            self._update_user_similarities(feature_provider)
        
        # Get recommendation count
        count = context.get("count", 8)
        
        # Check if we know this user
        if user_id not in self.user_similarities:
            logger.warning(f"No similarity data for user {user_id}, cannot make recommendations")
            return []
        
        # Get items the user has already interacted with
        user_items = set(feature_provider.get_user_items(user_id))
        
        # Get similar users
        similar_users = self.user_similarities[user_id]
        
        # Calculate item scores based on similar users
        item_scores = {}
        
        for similar_user, similarity in similar_users.items():
            # Skip if similarity is too low
            if similarity < self.min_similarity:
                continue
            
            # Get items this similar user has interacted with
            similar_user_items = feature_provider.get_user_items(similar_user)
            
            for item in similar_user_items:
                # Skip items the target user already has
                if item in user_items:
                    continue
                
                # Weight item by similarity
                if item in item_scores:
                    item_scores[item] += similarity
                else:
                    item_scores[item] = similarity
        
        # Sort by score
        sorted_items = sorted(item_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Get personalized recommendation reason
        reason = "为您量身推荐"
        
        return self._format_recommendations(sorted_items[:count], reason)
    
    def _update_user_similarities(self, feature_provider):
        """Update user similarity matrix based on interaction data"""
        try:
            # Get interaction data (all types)
            interaction_data = feature_provider.get_interaction_data()
            
            # Convert to DataFrame for easier processing
            df = pd.DataFrame(interaction_data, columns=["user_id", "item_id", "event_type"])
            
            # Apply weights based on event type
            event_weights = {
                "purchase": 1.0,
                "add_to_cart": 0.5,
                "view": 0.2
            }
            
            # Apply weights
            df["weight"] = df["event_type"].map(event_weights)
            
            # Create weighted user-item matrix
            user_item_matrix = df.pivot_table(
                index="user_id", 
                columns="item_id", 
                values="weight", 
                aggfunc="sum",
                fill_value=0
            )
            
            self.user_item_matrix = user_item_matrix
            
            # Calculate user similarities using cosine similarity
            user_vectors = user_item_matrix.values
            all_user_ids = user_item_matrix.index.tolist()
            
            similarity_matrix = cosine_similarity(user_vectors)
            
            # Update user similarities dictionary
            for i, user1 in enumerate(all_user_ids):
                if user1 not in self.user_similarities:
                    self.user_similarities[user1] = {}
                
                # Get top N similar users
                user_similarities = [(all_user_ids[j], similarity_matrix[i, j]) 
                                     for j in range(len(all_user_ids)) if i != j]
                
                user_similarities.sort(key=lambda x: x[1], reverse=True)
                
                # Store top N similar users
                self.user_similarities[user1] = {
                    u_id: sim for u_id, sim in user_similarities[:self.max_neighbors]
                }
            
            self.last_updated = datetime.now()
            logger.info(f"Updated user similarities for {len(self.user_similarities)} users")
            
        except Exception as e:
            logger.error(f"Error updating user similarities: {str(e)}")


class HybridRecommender(RecommendationAlgorithm):
    """Hybrid recommender combining multiple algorithms"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize hybrid recommender"""
        super().__init__(config)
        self.name = "hybrid"
        
        # Initialize component recommenders
        self.recommenders = {}
        
        # Default weights for different contexts
        self.context_weights = {
            "home": {
                "user_cf": 0.5,
                "popular_items": 0.5
            },
            "detail": {
                "content_based": 0.7,
                "item_cf": 0.3
            },
            "cart": {
                "item_cf": 0.7,
                "popular_items": 0.3
            }
        }
        
        # Override with config if provided
        if config and "context_weights" in config:
            for context, weights in config["context_weights"].items():
                self.context_weights[context] = weights
    
    def add_recommender(self, name: str, recommender: RecommendationAlgorithm):
        """Add a component recommender algorithm"""
        self.recommenders[name] = recommender
    
    def recommend(self, user_id: str, context: Dict[str, Any], feature_provider) -> List[Dict[str, Any]]:
        """
        Generate recommendations using a hybrid approach
        
        Args:
            user_id: User ID to generate recommendations for
            context: Must contain 'scene' to determine weights
            feature_provider: Provider for feature data
            
        Returns:
            List of recommended items with scores
        """
        # Get recommendation count
        count = context.get("count", 10)
        
        # Get scene to determine weights
        scene = context.get("scene", "home")
        
        if scene not in self.context_weights:
            logger.warning(f"Unknown scene '{scene}', using 'home' weights")
            scene = "home"
        
        weights = self.context_weights[scene]
        
        # Collect recommendations from each algorithm
        all_recommendations = {}
        
        for algo_name, weight in weights.items():
            if algo_name not in self.recommenders:
                logger.warning(f"Recommender '{algo_name}' not found, skipping")
                continue
            
            # Get recommendations from this algorithm
            algo_recs = self.recommenders[algo_name].recommend(user_id, context, feature_provider)
            
            # Add to combined recommendations with weight
            for rec in algo_recs:
                item_id = rec["item_id"]
                score = rec["score"] * weight
                
                if item_id in all_recommendations:
                    all_recommendations[item_id]["score"] += score
                    all_recommendations[item_id]["algorithms"].append(algo_name)
                else:
                    all_recommendations[item_id] = {
                        "item_id": item_id,
                        "score": score,
                        "algorithms": [algo_name],
                        "reason": rec.get("reason")
                    }
        
        # Convert to list and sort by score
        recommendations = list(all_recommendations.values())
        recommendations.sort(key=lambda x: x["score"], reverse=True)
        
        # Take top N recommendations
        top_recommendations = recommendations[:count]
        
        # Format and return
        for rec in top_recommendations:
            # Normalize score to 0-1 range
            rec["score"] = round(min(1.0, rec["score"]), 4)
            
            # If item was recommended by multiple algorithms, use primary algorithm's reason
            if len(rec["algorithms"]) > 1:
                # Use the algorithm with the highest weight for reason
                primary_algo = max(rec["algorithms"], key=lambda a: weights.get(a, 0))
                rec["primary_algo"] = primary_algo
            
            # Remove internal fields
            rec.pop("algorithms", None)
        
        return top_recommendations


class RecommendationFactory:
    """Factory for creating and configuring recommendation algorithms"""
    
    @staticmethod
    def create_recommender(algorithm_type: str, config: Dict[str, Any] = None) -> RecommendationAlgorithm:
        """
        Create a recommender instance based on algorithm type
        
        Args:
            algorithm_type: Type of algorithm to create
            config: Configuration parameters
            
        Returns:
            Configured recommender instance
        """
        if algorithm_type == "popular_items":
            return PopularItemsRecommender(config)
        elif algorithm_type == "content_based":
            return ContentBasedRecommender(config)
        elif algorithm_type == "item_cf":
            return ItemCollaborativeFilteringRecommender(config)
        elif algorithm_type == "user_cf":
            return UserCollaborativeFilteringRecommender(config)
        elif algorithm_type == "hybrid":
            hybrid = HybridRecommender(config)
            
            # Create component algorithms
            component_configs = config.get("component_configs", {})
            
            # Add popular items recommender
            if "popular_items" in component_configs:
                hybrid.add_recommender("popular_items", 
                                      PopularItemsRecommender(component_configs["popular_items"]))
            else:
                hybrid.add_recommender("popular_items", PopularItemsRecommender())
            
            # Add content-based recommender
            if "content_based" in component_configs:
                hybrid.add_recommender("content_based", 
                                      ContentBasedRecommender(component_configs["content_based"]))
            else:
                hybrid.add_recommender("content_based", ContentBasedRecommender())
            
            # Add item-CF recommender
            if "item_cf" in component_configs:
                hybrid.add_recommender("item_cf", 
                                      ItemCollaborativeFilteringRecommender(component_configs["item_cf"]))
            else:
                hybrid.add_recommender("item_cf", ItemCollaborativeFilteringRecommender())
            
            # Add user-CF recommender
            if "user_cf" in component_configs:
                hybrid.add_recommender("user_cf", 
                                      UserCollaborativeFilteringRecommender(component_configs["user_cf"]))
            else:
                hybrid.add_recommender("user_cf", UserCollaborativeFilteringRecommender())
            
            return hybrid
        else:
            raise ValueError(f"Unknown algorithm type: {algorithm_type}")


# Example usage
if __name__ == "__main__":
    # Simple test with mock data
    from collections import defaultdict
    
    class MockFeatureProvider:
        def __init__(self):
            self.items = {
                "P12345": {
                    "id": "P12345",
                    "name": "Ultra Thin Laptop Pro X",
                    "description": "High-performance laptop with 16GB RAM, 512GB SSD, and dedicated graphics card.",
                    "categories": ["electronics", "computers", "laptops"],
                    "attributes": {
                        "brand": "TechMaster",
                        "processor": "Intel Core i7",
                        "screen_size": "15.6 inches"
                    }
                },
                "P12346": {
                    "id": "P12346",
                    "name": "Professional Wireless Mouse",
                    "description": "Ergonomic wireless mouse with precision tracking and long battery life.",
                    "categories": ["electronics", "computers", "accessories"],
                    "attributes": {
                        "brand": "TechMaster",
                        "connection": "Bluetooth"
                    }
                },
                "P12347": {
                    "id": "P12347",
                    "name": "Noise-Cancelling Headphones",
                    "description": "Premium wireless headphones with active noise cancellation.",
                    "categories": ["electronics", "audio", "headphones"],
                    "attributes": {
                        "brand": "SoundWave",
                        "connection": "Bluetooth"
                    }
                }
            }
            
            self.user_items = defaultdict(list)
            self.user_items["user1"] = ["P12345", "P12346"]
            self.user_items["user2"] = ["P12345", "P12347"]
        
        def get_all_items(self):
            return list(self.items.values())
        
        def get_categories(self):
            return ["electronics", "computers", "laptops", "accessories", "audio", "headphones"]
        
        def get_popular_items(self, category=None, limit=10):
            if category == "electronics":
                return [("P12345", 0.9), ("P12347", 0.8), ("P12346", 0.7)]
            return [("P12345", 0.9), ("P12346", 0.8), ("P12347", 0.7)]
        
        def get_user_items(self, user_id, event_type=None):
            return self.user_items.get(user_id, [])
        
        def get_purchase_data(self):
            return [
                ("user1", "P12345"),
                ("user1", "P12346"),
                ("user2", "P12345"),
                ("user2", "P12347")
            ]
        
        def get_interaction_data(self):
            return [
                ("user1", "P12345", "purchase"),
                ("user1", "P12346", "purchase"),
                ("user2", "P12345", "purchase"),
                ("user2", "P12347", "purchase"),
                ("user1", "P12347", "view")
            ]
    
    # Create mock data provider
    feature_provider = MockFeatureProvider()
    
    # Test popular items recommender
    print("\nTesting Popular Items Recommender:")
    popular_rec = RecommendationFactory.create_recommender("popular_items")
    popular_results = popular_rec.recommend("user1", {"count": 3}, feature_provider)
    print(json.dumps(popular_results, indent=2))
    
    # Test content-based recommender
    print("\nTesting Content-Based Recommender:")
    cb_rec = RecommendationFactory.create_recommender("content_based")
    cb_results = cb_rec.recommend("user1", {"item_id": "P12345", "count": 2}, feature_provider)
    print(json.dumps(cb_results, indent=2))
    
    # Test item-CF recommender
    print("\nTesting Item-CF Recommender:")
    item_cf_rec = RecommendationFactory.create_recommender("item_cf")
    item_cf_results = item_cf_rec.recommend("user1", {"item_id": "P12345", "count": 2}, feature_provider)
    print(json.dumps(item_cf_results, indent=2))
    
    # Test hybrid recommender
    print("\nTesting Hybrid Recommender:")
    hybrid_config = {
        "context_weights": {
            "home": {
                "popular_items": 0.7,
                "user_cf": 0.3
            }
        }
    }
    hybrid_rec = RecommendationFactory.create_recommender("hybrid", hybrid_config)
    hybrid_results = hybrid_rec.recommend("user1", {"scene": "home", "count": 3}, feature_provider)
    print(json.dumps(hybrid_results, indent=2)) 