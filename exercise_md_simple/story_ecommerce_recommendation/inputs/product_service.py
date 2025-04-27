#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Product Information Service for E-commerce Recommendation System
This module provides API endpoints to retrieve product data from the database.
"""

import json
import logging
from typing import Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProductDatabase:
    """Simulates a product database with in-memory storage"""
    
    def __init__(self, data_file: Optional[str] = None):
        """Initialize database with optional data file"""
        self.products = {}
        self.categories = {}
        if data_file:
            self.load_data(data_file)
    
    def load_data(self, data_file: str) -> None:
        """Load product data from JSON file"""
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.products = data.get('products', {})
                self.categories = data.get('categories', {})
                logger.info(f"Loaded {len(self.products)} products from {data_file}")
        except Exception as e:
            logger.error(f"Failed to load data from {data_file}: {e}")
            raise
    
    def get_product(self, product_id: str) -> Optional[Dict]:
        """Retrieve product by ID"""
        product = self.products.get(product_id)
        if not product:
            logger.warning(f"Product not found: {product_id}")
            return None
        return product
    
    def get_products_by_category(self, category_id: str) -> List[Dict]:
        """Retrieve all products in a category"""
        return [p for p in self.products.values() if category_id in p.get('categories', [])]
    
    def search_products(self, query: str, limit: int = 10) -> List[Dict]:
        """Search products by name or description"""
        query = query.lower()
        results = []
        
        for product in self.products.values():
            if (query in product.get('name', '').lower() or 
                query in product.get('description', '').lower()):
                results.append(product)
                if len(results) >= limit:
                    break
        
        logger.info(f"Search for '{query}' returned {len(results)} results")
        return results
    
    def get_related_products(self, product_id: str, limit: int = 5) -> List[Dict]:
        """Get related products based on shared categories"""
        product = self.get_product(product_id)
        if not product:
            return []
        
        product_categories = product.get('categories', [])
        if not product_categories:
            return []
        
        # Find products that share categories with the given product
        related = []
        for pid, p in self.products.items():
            if pid == product_id:
                continue
            
            # Calculate category overlap
            p_categories = p.get('categories', [])
            common_categories = set(product_categories) & set(p_categories)
            
            if common_categories:
                related.append({
                    'product': p,
                    'relevance': len(common_categories)
                })
        
        # Sort by relevance (number of shared categories)
        related.sort(key=lambda x: x['relevance'], reverse=True)
        return [item['product'] for item in related[:limit]]

class ProductService:
    """Service layer for product information APIs"""
    
    def __init__(self, database: ProductDatabase):
        """Initialize with database connection"""
        self.db = database
    
    def get_product_details(self, product_id: str) -> Dict:
        """Get complete product details"""
        product = self.db.get_product(product_id)
        if not product:
            return {'error': f'Product not found: {product_id}', 'status': 404}
        
        # Enrich product with additional information
        result = product.copy()
        result['related_products'] = self.db.get_related_products(product_id)
        
        return {'data': result, 'status': 200}
    
    def get_category_products(self, category_id: str, page: int = 1, 
                             per_page: int = 20) -> Dict:
        """Get paginated products for a category"""
        all_products = self.db.get_products_by_category(category_id)
        
        # Calculate pagination
        total = len(all_products)
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        products = all_products[start_idx:end_idx]
        
        return {
            'data': {
                'products': products,
                'pagination': {
                    'total': total,
                    'page': page,
                    'per_page': per_page,
                    'pages': (total + per_page - 1) // per_page
                }
            },
            'status': 200
        }
    
    def search(self, query: str, filters: Optional[Dict] = None) -> Dict:
        """Search products with optional filters"""
        if not query or len(query) < 2:
            return {'error': 'Query must be at least 2 characters', 'status': 400}
        
        results = self.db.search_products(query)
        
        # Apply filters if provided
        if filters:
            filtered_results = []
            for product in results:
                match = True
                
                # Price filter
                if 'price_min' in filters and product.get('price', 0) < filters['price_min']:
                    match = False
                if 'price_max' in filters and product.get('price', 0) > filters['price_max']:
                    match = False
                
                # Category filter
                if 'categories' in filters and not any(c in product.get('categories', []) 
                                                     for c in filters['categories']):
                    match = False
                
                if match:
                    filtered_results.append(product)
            
            results = filtered_results
        
        return {'data': results, 'status': 200}


def main():
    """Example usage of the ProductService"""
    # Load sample data
    db = ProductDatabase('sample_products.json')
    service = ProductService(db)
    
    # Example: Get product details
    result = service.get_product_details('P12345')
    print(f"Product details: {json.dumps(result, indent=2)}")
    
    # Example: Search products
    search_result = service.search('laptop', {'price_min': 500})
    print(f"Search results: {json.dumps(search_result, indent=2)}")


if __name__ == '__main__':
    main() 