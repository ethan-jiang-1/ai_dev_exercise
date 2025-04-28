#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Event Collection Service for E-commerce Recommendation System
This module collects and processes user behavior events.
"""

import os
import json
import time
import uuid
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Union

from fastapi import FastAPI, HTTPException, Query, Depends, Request, Body, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator

from kafka import KafkaProducer
from redis import Redis
from elasticsearch import Elasticsearch

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="E-commerce Event Collection API",
    description="API for collecting user behavior events",
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
KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "user_events")

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))

ES_HOST = os.environ.get("ES_HOST", "localhost")
ES_PORT = int(os.environ.get("ES_PORT", 9200))
ES_INDEX = os.environ.get("ES_INDEX", "user_events")

# Models for request/response
class EventData(BaseModel):
    user_id: str = Field(..., description="User ID, or anonymous ID for non-logged in users")
    event_type: str = Field(..., description="Type of event (view, click, add_to_cart, purchase, etc)")
    item_id: Optional[str] = Field(None, description="Product ID that this event is related to")
    session_id: Optional[str] = Field(None, description="Session ID for tracking user journey")
    category_id: Optional[str] = Field(None, description="Category ID if applicable")
    timestamp: Optional[float] = Field(None, description="Event timestamp in milliseconds")
    referrer: Optional[str] = Field(None, description="Referrer URL or page")
    device_info: Optional[Dict[str, Any]] = Field(None, description="Device information")
    properties: Optional[Dict[str, Any]] = Field(None, description="Additional event properties")
    
    @validator('event_type')
    def validate_event_type(cls, v):
        valid_types = [
            'page_view', 'product_view', 'category_view', 
            'search', 'add_to_cart', 'remove_from_cart', 
            'begin_checkout', 'purchase', 'login', 'signup',
            'add_to_wishlist', 'share'
        ]
        if v not in valid_types:
            logger.warning(f"Received non-standard event_type: {v}")
        return v
    
    @validator('timestamp', pre=True, always=True)
    def set_timestamp(cls, v):
        if v is None:
            return int(time.time() * 1000)
        return v

class EventResponse(BaseModel):
    event_id: str = Field(..., description="Unique ID for the processed event")
    status: str = Field(..., description="Status of the event processing")
    received_at: float = Field(..., description="Server timestamp when event was received")

# Event processor service
class EventProcessor:
    """Process and store user events"""
    
    def __init__(self):
        """Initialize event processor with connections to data stores"""
        # Connect to Kafka
        self.kafka_producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            acks='all'
        )
        
        # Connect to Redis for real-time analytics
        self.redis = Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )
        
        # Connect to Elasticsearch for searchable storage
        self.es = Elasticsearch([{
            'host': ES_HOST,
            'port': ES_PORT
        }])
        
        # Ensure index exists
        self._ensure_index()
        
        logger.info("EventProcessor initialized")
    
    def _ensure_index(self):
        """Ensure Elasticsearch index exists with proper mappings"""
        if not self.es.indices.exists(index=ES_INDEX):
            mappings = {
                "mappings": {
                    "properties": {
                        "user_id": {"type": "keyword"},
                        "event_type": {"type": "keyword"},
                        "item_id": {"type": "keyword"},
                        "session_id": {"type": "keyword"},
                        "category_id": {"type": "keyword"},
                        "timestamp": {"type": "date", "format": "epoch_millis"},
                        "referrer": {"type": "keyword"},
                        "device_info": {
                            "properties": {
                                "type": {"type": "keyword"},
                                "browser": {"type": "keyword"},
                                "os": {"type": "keyword"}
                            }
                        },
                        "properties": {"type": "object", "dynamic": True}
                    }
                }
            }
            
            self.es.indices.create(index=ES_INDEX, body=mappings)
            logger.info(f"Created Elasticsearch index {ES_INDEX}")
    
    def process_event(self, event: EventData, client_ip: str, user_agent: str) -> EventResponse:
        """
        Process a user event
        
        Args:
            event: EventData object containing event details
            client_ip: Client IP address
            user_agent: User agent string
            
        Returns:
            EventResponse with processing status
        """
        # Generate unique event ID
        event_id = str(uuid.uuid4())
        
        # Add server-side data
        received_at = time.time()
        
        # Prepare event for storage
        event_dict = event.dict()
        event_dict["event_id"] = event_id
        event_dict["client_ip"] = client_ip
        event_dict["user_agent"] = user_agent
        event_dict["received_at"] = received_at
        
        # Send to Kafka
        try:
            self.kafka_producer.send(KAFKA_TOPIC, event_dict)
            logger.debug(f"Sent event {event_id} to Kafka")
        except Exception as e:
            logger.error(f"Error sending to Kafka: {str(e)}")
        
        # Update real-time counters in Redis
        try:
            self._update_redis_counters(event_dict)
        except Exception as e:
            logger.error(f"Error updating Redis: {str(e)}")
        
        # Store in Elasticsearch
        try:
            self.es.index(
                index=ES_INDEX,
                id=event_id,
                body=event_dict,
                refresh=True
            )
            logger.debug(f"Stored event {event_id} in Elasticsearch")
        except Exception as e:
            logger.error(f"Error storing in Elasticsearch: {str(e)}")
        
        # Return response
        return EventResponse(
            event_id=event_id,
            status="processed",
            received_at=received_at
        )
    
    def _update_redis_counters(self, event: Dict[str, Any]):
        """Update real-time counters in Redis"""
        # Extract relevant fields
        event_type = event["event_type"]
        timestamp = event["timestamp"]
        user_id = event["user_id"]
        
        # Get current day/hour for time-based stats
        dt = datetime.fromtimestamp(timestamp / 1000)
        day_key = dt.strftime("%Y-%m-%d")
        hour_key = dt.strftime("%Y-%m-%d-%H")
        
        # Increment event type counters
        self.redis.hincrby(f"events:count:daily:{day_key}", event_type, 1)
        self.redis.hincrby(f"events:count:hourly:{hour_key}", event_type, 1)
        
        # Update unique users
        self.redis.sadd(f"events:users:daily:{day_key}", user_id)
        self.redis.sadd(f"events:users:hourly:{hour_key}", user_id)
        
        # Track item popularity if applicable
        item_id = event.get("item_id")
        if item_id:
            if event_type == "product_view":
                self.redis.zincrby(f"items:views:daily:{day_key}", 1, item_id)
            elif event_type == "add_to_cart":
                self.redis.zincrby(f"items:cart_adds:daily:{day_key}", 1, item_id)
            elif event_type == "purchase":
                self.redis.zincrby(f"items:purchases:daily:{day_key}", 1, item_id)
        
        # TTL for Redis keys (keep daily data for 30 days, hourly for 3 days)
        self.redis.expire(f"events:count:daily:{day_key}", 60*60*24*30)
        self.redis.expire(f"events:users:daily:{day_key}", 60*60*24*30)
        self.redis.expire(f"events:count:hourly:{hour_key}", 60*60*24*3)
        self.redis.expire(f"events:users:hourly:{hour_key}", 60*60*24*3)
        
        if item_id:
            self.redis.expire(f"items:views:daily:{day_key}", 60*60*24*30)
            self.redis.expire(f"items:cart_adds:daily:{day_key}", 60*60*24*30)
            self.redis.expire(f"items:purchases:daily:{day_key}", 60*60*24*30)
    
    def get_stats(self, period: str = "day") -> Dict[str, Any]:
        """
        Get real-time stats from Redis
        
        Args:
            period: Time period for stats (day or hour)
            
        Returns:
            Dictionary with stats
        """
        # Get current day/hour
        now = datetime.now()
        day_key = now.strftime("%Y-%m-%d")
        hour_key = now.strftime("%Y-%m-%d-%H")
        
        key_prefix = "events:count:daily" if period == "day" else "events:count:hourly"
        time_key = day_key if period == "day" else hour_key
        
        # Get event counts
        event_counts = self.redis.hgetall(f"{key_prefix}:{time_key}")
        
        # Convert string counts to integers
        for event_type, count in event_counts.items():
            event_counts[event_type] = int(count)
        
        # Get unique users count
        user_key_prefix = "events:users:daily" if period == "day" else "events:users:hourly"
        unique_users = self.redis.scard(f"{user_key_prefix}:{time_key}")
        
        # Get top items
        top_viewed = self._get_top_items(f"items:views:daily:{day_key}", 5)
        top_carted = self._get_top_items(f"items:cart_adds:daily:{day_key}", 5)
        top_purchased = self._get_top_items(f"items:purchases:daily:{day_key}", 5)
        
        return {
            "event_counts": event_counts,
            "unique_users": unique_users,
            "top_items": {
                "viewed": top_viewed,
                "carted": top_carted,
                "purchased": top_purchased
            },
            "period": period,
            "timestamp": now.isoformat()
        }
    
    def _get_top_items(self, key: str, count: int = 5) -> List[Dict[str, Any]]:
        """Get top items from Redis sorted set"""
        try:
            # Get top N items with scores
            top_items = self.redis.zrevrange(key, 0, count-1, withscores=True)
            
            # Format results
            return [{"item_id": item, "count": int(score)} for item, score in top_items]
        except Exception as e:
            logger.error(f"Error getting top items: {str(e)}")
            return []
    
    def close(self):
        """Close connections"""
        try:
            self.kafka_producer.close()
            self.redis.close()
            logger.info("Closed all connections")
        except Exception as e:
            logger.error(f"Error closing connections: {str(e)}")

# Dependency to get event processor
def get_event_processor():
    """Get or create event processor instance"""
    processor = EventProcessor()
    try:
        yield processor
    finally:
        processor.close()

# API endpoints
@app.post("/api/events", response_model=EventResponse)
async def track_event(
    event: EventData,
    request: Request,
    processor: EventProcessor = Depends(get_event_processor),
    user_agent: Optional[str] = Header(None)
):
    """Collect and process a user event"""
    try:
        client_ip = request.client.host
        user_agent = user_agent or "Unknown"
        
        return processor.process_event(event, client_ip, user_agent)
    except Exception as e:
        logger.error(f"Error processing event: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/events/batch")
async def track_events_batch(
    events: List[EventData],
    request: Request,
    processor: EventProcessor = Depends(get_event_processor),
    user_agent: Optional[str] = Header(None)
):
    """Collect and process a batch of user events"""
    try:
        client_ip = request.client.host
        user_agent = user_agent or "Unknown"
        
        responses = []
        for event in events:
            response = processor.process_event(event, client_ip, user_agent)
            responses.append(response)
        
        return {"processed": len(responses), "events": responses}
    except Exception as e:
        logger.error(f"Error processing event batch: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/stats")
async def get_stats(
    period: str = Query("day", enum=["day", "hour"]),
    processor: EventProcessor = Depends(get_event_processor)
):
    """Get real-time stats"""
    try:
        return processor.get_stats(period)
    except Exception as e:
        logger.error(f"Error getting stats: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 