from elasticsearch import Elasticsearch, helpers
from redis import Redis
import logging
import os
from datetime import datetime
import json
from typing import Dict, List, Any, Optional, Union

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 环境配置
class Config:
    """系统配置类，包含所有数据库连接和环境配置"""
    # Redis配置
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
    REDIS_DB = int(os.environ.get('REDIS_DB', 0))
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)
    REDIS_PREFIX = os.environ.get('REDIS_PREFIX', 'ecom:')
    
    # Elasticsearch配置
    ES_HOSTS = os.environ.get('ES_HOSTS', 'http://localhost:9200').split(',')
    ES_USER = os.environ.get('ES_USER', None)
    ES_PASSWORD = os.environ.get('ES_PASSWORD', None)
    
    # 索引配置
    USER_INDEX = os.environ.get('USER_INDEX', 'ecom_users')
    PRODUCT_INDEX = os.environ.get('PRODUCT_INDEX', 'ecom_products')
    EVENT_INDEX = os.environ.get('EVENT_INDEX', 'ecom_events')
    
    # 缓存配置
    CACHE_TIMEOUT = int(os.environ.get('CACHE_TIMEOUT', 3600))  # 1小时
    USER_CACHE_PREFIX = f"{REDIS_PREFIX}user:"
    PRODUCT_CACHE_PREFIX = f"{REDIS_PREFIX}product:"
    RECOMMENDATION_CACHE_PREFIX = f"{REDIS_PREFIX}rec:"
    POPULAR_ITEMS_KEY = f"{REDIS_PREFIX}popular_items"
    SIMILAR_PRODUCTS_PREFIX = f"{REDIS_PREFIX}similar:"
    
    # 批处理配置
    BATCH_SIZE = int(os.environ.get('BATCH_SIZE', 1000))
    
    @classmethod
    def get_es_client(cls) -> Elasticsearch:
        """获取Elasticsearch客户端连接"""
        try:
            auth = None
            if cls.ES_USER and cls.ES_PASSWORD:
                auth = (cls.ES_USER, cls.ES_PASSWORD)
                
            client = Elasticsearch(
                cls.ES_HOSTS,
                basic_auth=auth,
                retry_on_timeout=True,
                max_retries=3
            )
            if not client.ping():
                logger.error("无法连接到Elasticsearch服务器")
                raise ConnectionError("无法连接到Elasticsearch服务器")
            return client
        except Exception as e:
            logger.error(f"Elasticsearch连接异常: {str(e)}")
            raise
    
    @classmethod
    def get_redis_client(cls) -> Redis:
        """获取Redis客户端连接"""
        try:
            client = Redis(
                host=cls.REDIS_HOST,
                port=cls.REDIS_PORT,
                db=cls.REDIS_DB,
                password=cls.REDIS_PASSWORD,
                decode_responses=True  # 将响应解码为字符串
            )
            if not client.ping():
                logger.error("无法连接到Redis服务器")
                raise ConnectionError("无法连接到Redis服务器")
            return client
        except Exception as e:
            logger.error(f"Redis连接异常: {str(e)}")
            raise


# 数据模型
class BaseModel:
    """基础模型类，提供公共方法"""
    
    @staticmethod
    def to_dict(obj: Any) -> Dict:
        """将对象转换为字典"""
        if isinstance(obj, dict):
            return obj
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            return {}
    
    @classmethod
    def from_dict(cls, data: Dict) -> Any:
        """从字典创建对象实例"""
        if not data:
            return None
        return cls(**data)


class Product(BaseModel):
    """产品模型类"""
    
    def __init__(self, 
                 product_id: str, 
                 name: str, 
                 description: str = "", 
                 price: float = 0.0, 
                 categories: List[str] = None, 
                 image_url: str = "", 
                 brand: str = "", 
                 attributes: Dict = None,
                 created_at: str = None,
                 updated_at: str = None):
        """
        初始化产品对象
        
        Args:
            product_id: 产品ID
            name: 产品名称
            description: 产品描述
            price: 产品价格
            categories: 产品类别列表
            image_url: 产品图片URL
            brand: 产品品牌
            attributes: 产品属性字典
            created_at: 创建时间
            updated_at: 更新时间
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.categories = categories or []
        self.image_url = image_url
        self.brand = brand
        self.attributes = attributes or {}
        
        # 设置时间戳
        now = datetime.now().isoformat()
        self.created_at = created_at or now
        self.updated_at = updated_at or now
    
    def to_index_doc(self) -> Dict:
        """转换为Elasticsearch索引文档"""
        doc = self.to_dict(self)
        # 添加内容索引字段，用于内容相似度计算
        doc['content_vector'] = f"{self.name} {self.description} {self.brand} {' '.join(self.categories)}"
        return doc

    @classmethod
    def create_index(cls, es_client: Elasticsearch) -> None:
        """创建产品索引"""
        index_name = Config.PRODUCT_INDEX
        
        # 检查索引是否存在
        if es_client.indices.exists(index=index_name):
            logger.info(f"索引 {index_name} 已存在")
            return
        
        # 定义索引映射
        mappings = {
            "properties": {
                "product_id": {"type": "keyword"},
                "name": {"type": "text", "analyzer": "standard", "fields": {"keyword": {"type": "keyword"}}},
                "description": {"type": "text", "analyzer": "standard"},
                "price": {"type": "float"},
                "categories": {"type": "keyword"},
                "image_url": {"type": "keyword"},
                "brand": {"type": "keyword"},
                "attributes": {"type": "object", "dynamic": True},
                "content_vector": {"type": "text", "analyzer": "standard"},
                "created_at": {"type": "date"},
                "updated_at": {"type": "date"}
            }
        }
        
        # 创建索引
        es_client.indices.create(
            index=index_name,
            mappings=mappings,
            settings={
                "number_of_shards": 3,
                "number_of_replicas": 1,
                "analysis": {
                    "analyzer": {
                        "standard": {
                            "type": "standard"
                        }
                    }
                }
            }
        )
        logger.info(f"索引 {index_name} 创建成功")


class UserProfile(BaseModel):
    """用户资料模型类"""
    
    def __init__(self, 
                 user_id: str, 
                 interests: Dict[str, float] = None, 
                 recent_viewed: List[Dict] = None, 
                 recent_purchased: List[Dict] = None, 
                 favorite_categories: Dict[str, float] = None,
                 favorite_brands: Dict[str, float] = None,
                 user_segment: str = "general",
                 user_embedding: List[float] = None,
                 created_at: str = None,
                 updated_at: str = None,
                 last_active: str = None):
        """
        初始化用户资料对象
        
        Args:
            user_id: 用户ID
            interests: 用户兴趣及权重 {兴趣: 权重}
            recent_viewed: 最近浏览的产品列表
            recent_purchased: 最近购买的产品列表
            favorite_categories: 喜爱的类别及权重 {类别: 权重}
            favorite_brands: 喜爱的品牌及权重 {品牌: 权重}
            user_segment: 用户细分
            user_embedding: 用户嵌入向量
            created_at: 创建时间
            updated_at: 更新时间
            last_active: 最后活跃时间
        """
        self.user_id = user_id
        self.interests = interests or {}
        self.recent_viewed = recent_viewed or []
        self.recent_purchased = recent_purchased or []
        self.favorite_categories = favorite_categories or {}
        self.favorite_brands = favorite_brands or {}
        self.user_segment = user_segment
        self.user_embedding = user_embedding or []
        
        # 设置时间戳
        now = datetime.now().isoformat()
        self.created_at = created_at or now
        self.updated_at = updated_at or now
        self.last_active = last_active or now
    
    @classmethod
    def create_index(cls, es_client: Elasticsearch) -> None:
        """创建用户资料索引"""
        index_name = Config.USER_INDEX
        
        # 检查索引是否存在
        if es_client.indices.exists(index=index_name):
            logger.info(f"索引 {index_name} 已存在")
            return
        
        # 定义索引映射
        mappings = {
            "properties": {
                "user_id": {"type": "keyword"},
                "interests": {"type": "object", "dynamic": True},
                "recent_viewed": {"type": "nested", "properties": {
                    "product_id": {"type": "keyword"},
                    "timestamp": {"type": "date"},
                    "score": {"type": "float"}
                }},
                "recent_purchased": {"type": "nested", "properties": {
                    "product_id": {"type": "keyword"},
                    "timestamp": {"type": "date"},
                    "quantity": {"type": "integer"},
                    "price": {"type": "float"}
                }},
                "favorite_categories": {"type": "object", "dynamic": True},
                "favorite_brands": {"type": "object", "dynamic": True},
                "user_segment": {"type": "keyword"},
                "user_embedding": {"type": "dense_vector", "dims": 128},
                "created_at": {"type": "date"},
                "updated_at": {"type": "date"},
                "last_active": {"type": "date"}
            }
        }
        
        # 创建索引
        es_client.indices.create(
            index=index_name,
            mappings=mappings,
            settings={
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        )
        logger.info(f"索引 {index_name} 创建成功")


class Event(BaseModel):
    """用户事件模型类"""
    
    # 定义事件类型常量
    VIEW = "view"
    CLICK = "click"
    ADD_TO_CART = "add_to_cart"
    PURCHASE = "purchase"
    REMOVE_FROM_CART = "remove_from_cart"
    SEARCH = "search"
    RATE = "rate"
    
    def __init__(self, 
                 event_id: str,
                 user_id: str, 
                 event_type: str, 
                 product_id: Optional[str] = None,
                 category_id: Optional[str] = None,
                 search_query: Optional[str] = None,
                 rating: Optional[float] = None,
                 session_id: Optional[str] = None,
                 referrer: Optional[str] = None,
                 device_info: Optional[Dict] = None,
                 timestamp: Optional[str] = None,
                 metadata: Optional[Dict] = None):
        """
        初始化事件对象
        
        Args:
            event_id: 事件ID
            user_id: 用户ID
            event_type: 事件类型
            product_id: 产品ID (对于特定产品的事件)
            category_id: 类别ID (对于类别相关的事件)
            search_query: 搜索查询 (对于搜索事件)
            rating: 评分值 (对于评分事件)
            session_id: 会话ID
            referrer: 来源页面
            device_info: 设备信息
            timestamp: 事件时间戳
            metadata: 附加元数据
        """
        self.event_id = event_id
        self.user_id = user_id
        self.event_type = event_type
        self.product_id = product_id
        self.category_id = category_id
        self.search_query = search_query
        self.rating = rating
        self.session_id = session_id
        self.referrer = referrer
        self.device_info = device_info or {}
        self.timestamp = timestamp or datetime.now().isoformat()
        self.metadata = metadata or {}
    
    @classmethod
    def create_index(cls, es_client: Elasticsearch) -> None:
        """创建事件索引"""
        index_name = Config.EVENT_INDEX
        
        # 检查索引是否存在
        if es_client.indices.exists(index=index_name):
            logger.info(f"索引 {index_name} 已存在")
            return
        
        # 定义索引映射
        mappings = {
            "properties": {
                "event_id": {"type": "keyword"},
                "user_id": {"type": "keyword"},
                "event_type": {"type": "keyword"},
                "product_id": {"type": "keyword"},
                "category_id": {"type": "keyword"},
                "search_query": {"type": "text", "analyzer": "standard"},
                "rating": {"type": "float"},
                "session_id": {"type": "keyword"},
                "referrer": {"type": "keyword"},
                "device_info": {"type": "object", "dynamic": True},
                "timestamp": {"type": "date"},
                "metadata": {"type": "object", "dynamic": True}
            }
        }
        
        # 创建索引
        es_client.indices.create(
            index=index_name,
            mappings=mappings,
            settings={
                "number_of_shards": 5,
                "number_of_replicas": 1,
                "index.mapping.nested_objects.limit": 10000,
                "index.mapping.total_fields.limit": 2000
            }
        )
        logger.info(f"索引 {index_name} 创建成功")


# 数据访问层
class DataAccess:
    """数据访问类，提供对数据库的操作方法"""
    
    def __init__(self):
        """初始化数据访问对象，连接到数据库"""
        self.es = Config.get_es_client()
        self.redis = Config.get_redis_client()
        self.initialize_indices()
    
    def initialize_indices(self) -> None:
        """初始化所有必要的索引"""
        try:
            Product.create_index(self.es)
            UserProfile.create_index(self.es)
            Event.create_index(self.es)
        except Exception as e:
            logger.error(f"初始化索引失败: {str(e)}")
            raise
    
    # 产品相关方法
    def get_product(self, product_id: str) -> Optional[Product]:
        """获取产品信息"""
        # 先从缓存获取
        cache_key = f"{Config.PRODUCT_CACHE_PREFIX}{product_id}"
        cached_data = self.redis.get(cache_key)
        
        if cached_data:
            try:
                return Product.from_dict(json.loads(cached_data))
            except Exception as e:
                logger.warning(f"解析缓存的产品数据失败: {str(e)}")
        
        # 从ES获取
        try:
            response = self.es.get(index=Config.PRODUCT_INDEX, id=product_id)
            if response and response.get('found', False):
                product = Product.from_dict(response['_source'])
                
                # 更新缓存
                self.redis.setex(
                    cache_key,
                    Config.CACHE_TIMEOUT,
                    json.dumps(response['_source'])
                )
                
                return product
            return None
        except Exception as e:
            logger.error(f"获取产品数据失败: {str(e)}")
            return None
    
    def search_products(self, query: str, from_: int = 0, size: int = 10) -> List[Product]:
        """搜索产品"""
        try:
            response = self.es.search(
                index=Config.PRODUCT_INDEX,
                query={
                    "multi_match": {
                        "query": query,
                        "fields": ["name^3", "description", "brand", "categories"]
                    }
                },
                from_=from_,
                size=size
            )
            
            products = []
            for hit in response['hits']['hits']:
                products.append(Product.from_dict(hit['_source']))
            
            return products
        except Exception as e:
            logger.error(f"搜索产品失败: {str(e)}")
            return []
    
    def get_similar_products(self, product_id: str, size: int = 10) -> List[Product]:
        """获取相似产品"""
        # 先从缓存获取
        cache_key = f"{Config.SIMILAR_PRODUCTS_PREFIX}{product_id}"
        cached_data = self.redis.get(cache_key)
        
        if cached_data:
            try:
                product_ids = json.loads(cached_data)
                products = []
                for pid in product_ids:
                    product = self.get_product(pid)
                    if product:
                        products.append(product)
                return products
            except Exception as e:
                logger.warning(f"解析缓存的相似产品数据失败: {str(e)}")
        
        # 获取当前产品
        product = self.get_product(product_id)
        if not product:
            return []
        
        # 搜索相似产品
        try:
            response = self.es.search(
                index=Config.PRODUCT_INDEX,
                query={
                    "bool": {
                        "must": [
                            {
                                "more_like_this": {
                                    "fields": ["name", "description", "categories", "brand"],
                                    "like": f"{product.name} {product.description}",
                                    "min_term_freq": 1,
                                    "max_query_terms": 20,
                                    "minimum_should_match": "30%"
                                }
                            }
                        ],
                        "must_not": [
                            {"term": {"product_id": product_id}}
                        ]
                    }
                },
                size=size
            )
            
            similar_products = []
            product_ids = []
            
            for hit in response['hits']['hits']:
                similar_product = Product.from_dict(hit['_source'])
                similar_products.append(similar_product)
                product_ids.append(similar_product.product_id)
            
            # 更新缓存
            self.redis.setex(
                cache_key,
                Config.CACHE_TIMEOUT,
                json.dumps(product_ids)
            )
            
            return similar_products
        except Exception as e:
            logger.error(f"获取相似产品失败: {str(e)}")
            return []
    
    # 用户相关方法
    def get_user_profile(self, user_id: str) -> Optional[UserProfile]:
        """获取用户资料"""
        # 先从缓存获取
        cache_key = f"{Config.USER_CACHE_PREFIX}{user_id}"
        cached_data = self.redis.get(cache_key)
        
        if cached_data:
            try:
                return UserProfile.from_dict(json.loads(cached_data))
            except Exception as e:
                logger.warning(f"解析缓存的用户数据失败: {str(e)}")
        
        # 从ES获取
        try:
            response = self.es.get(
                index=Config.USER_INDEX,
                id=user_id,
                ignore=[404]  # 忽略找不到的错误
            )
            
            if response and response.get('found', False):
                user_profile = UserProfile.from_dict(response['_source'])
                
                # 更新缓存
                self.redis.setex(
                    cache_key,
                    Config.CACHE_TIMEOUT,
                    json.dumps(response['_source'])
                )
                
                return user_profile
            
            # 如果用户不存在，创建一个新的默认资料
            default_profile = UserProfile(user_id=user_id)
            self.save_user_profile(default_profile)
            return default_profile
        
        except Exception as e:
            logger.error(f"获取用户资料失败: {str(e)}")
            return None
    
    def save_user_profile(self, user_profile: UserProfile) -> bool:
        """保存用户资料"""
        try:
            # 更新时间戳
            user_profile.updated_at = datetime.now().isoformat()
            
            # 保存到ES
            self.es.index(
                index=Config.USER_INDEX,
                id=user_profile.user_id,
                document=user_profile.to_dict(user_profile)
            )
            
            # 更新缓存
            cache_key = f"{Config.USER_CACHE_PREFIX}{user_profile.user_id}"
            self.redis.setex(
                cache_key,
                Config.CACHE_TIMEOUT,
                json.dumps(user_profile.to_dict(user_profile))
            )
            
            return True
        except Exception as e:
            logger.error(f"保存用户资料失败: {str(e)}")
            return False
    
    def find_similar_users(self, user_id: str, size: int = 10) -> List[str]:
        """查找相似用户"""
        try:
            user_profile = self.get_user_profile(user_id)
            if not user_profile or not user_profile.user_embedding:
                return []
            
            # 使用向量搜索查找相似用户
            response = self.es.search(
                index=Config.USER_INDEX,
                query={
                    "script_score": {
                        "query": {"bool": {"must_not": [{"term": {"user_id": user_id}}]}},
                        "script": {
                            "source": "cosineSimilarity(params.query_vector, 'user_embedding') + 1.0",
                            "params": {"query_vector": user_profile.user_embedding}
                        }
                    }
                },
                size=size
            )
            
            similar_users = []
            for hit in response['hits']['hits']:
                similar_users.append(hit['_source']['user_id'])
            
            return similar_users
        except Exception as e:
            logger.error(f"查找相似用户失败: {str(e)}")
            return []
    
    # 事件相关方法
    def save_event(self, event: Event) -> bool:
        """保存用户事件"""
        try:
            # 保存到ES
            self.es.index(
                index=Config.EVENT_INDEX,
                id=event.event_id,
                document=event.to_dict(event)
            )
            
            # 根据事件类型更新计数器
            if event.event_type == Event.VIEW and event.product_id:
                self.redis.zincrby(f"{Config.REDIS_PREFIX}views", 1, event.product_id)
            
            if event.event_type == Event.CLICK and event.product_id:
                self.redis.zincrby(f"{Config.REDIS_PREFIX}clicks", 1, event.product_id)
            
            if event.event_type == Event.ADD_TO_CART and event.product_id:
                self.redis.zincrby(f"{Config.REDIS_PREFIX}cart_adds", 1, event.product_id)
            
            if event.event_type == Event.PURCHASE and event.product_id:
                self.redis.zincrby(f"{Config.REDIS_PREFIX}purchases", 1, event.product_id)
            
            # 添加到最近事件列表
            if event.product_id:
                recent_key = f"{Config.REDIS_PREFIX}recent:{event.user_id}"
                self.redis.lpush(recent_key, json.dumps({
                    "product_id": event.product_id,
                    "event_type": event.event_type,
                    "timestamp": event.timestamp
                }))
                self.redis.ltrim(recent_key, 0, 99)  # 只保留最近的100个事件
            
            return True
        except Exception as e:
            logger.error(f"保存事件失败: {str(e)}")
            return False
    
    def get_user_recent_events(self, user_id: str, event_types: Optional[List[str]] = None, limit: int = 20) -> List[Dict]:
        """获取用户最近事件"""
        try:
            query = {
                "bool": {
                    "must": [
                        {"term": {"user_id": user_id}}
                    ]
                }
            }
            
            if event_types:
                query["bool"]["must"].append({"terms": {"event_type": event_types}})
            
            response = self.es.search(
                index=Config.EVENT_INDEX,
                query=query,
                sort=[{"timestamp": {"order": "desc"}}],
                size=limit
            )
            
            events = []
            for hit in response['hits']['hits']:
                events.append(hit['_source'])
            
            return events
        except Exception as e:
            logger.error(f"获取用户最近事件失败: {str(e)}")
            return []
    
    def get_popular_products(self, category_id: Optional[str] = None, limit: int = 20) -> List[str]:
        """获取热门产品ID列表"""
        try:
            # 使用Redis的有序集合获取热门产品
            # 综合考虑浏览次数、点击次数和购买次数，按加权分数排序
            pipeline = self.redis.pipeline()
            views_key = f"{Config.REDIS_PREFIX}views"
            clicks_key = f"{Config.REDIS_PREFIX}clicks"
            purchases_key = f"{Config.REDIS_PREFIX}purchases"
            popular_key = f"{Config.POPULAR_ITEMS_KEY}"
            
            if category_id:
                popular_key = f"{popular_key}:{category_id}"
            
            # 检查是否已有缓存的热门商品
            if self.redis.exists(popular_key):
                return [item for item in self.redis.zrevrange(popular_key, 0, limit-1)]
            
            # 获取各个指标的商品数据
            pipeline.zrange(views_key, 0, -1, withscores=True)
            pipeline.zrange(clicks_key, 0, -1, withscores=True)
            pipeline.zrange(purchases_key, 0, -1, withscores=True)
            results = pipeline.execute()
            
            views_dict = dict(results[0]) if results[0] else {}
            clicks_dict = dict(results[1]) if results[1] else {}
            purchases_dict = dict(results[2]) if results[2] else {}
            
            # 合并所有产品ID
            all_product_ids = set(list(views_dict.keys()) + list(clicks_dict.keys()) + list(purchases_dict.keys()))
            
            # 计算综合得分
            scores = {}
            for product_id in all_product_ids:
                # 加权计算: 浏览=1, 点击=2, 购买=5
                score = views_dict.get(product_id, 0) * 1 + \
                        clicks_dict.get(product_id, 0) * 2 + \
                        purchases_dict.get(product_id, 0) * 5
                
                # 如果指定了类别，则过滤
                if category_id:
                    product = self.get_product(product_id)
                    if not product or category_id not in product.categories:
                        continue
                
                scores[product_id] = score
            
            # 按分数排序
            sorted_products = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]
            
            # 缓存结果
            pipeline = self.redis.pipeline()
            if sorted_products:
                pipeline.delete(popular_key)
                for product_id, score in sorted_products:
                    pipeline.zadd(popular_key, {product_id: score})
                pipeline.expire(popular_key, 3600)  # 设置1小时过期
                pipeline.execute()
            
            return [product_id for product_id, _ in sorted_products]
        
        except Exception as e:
            logger.error(f"获取热门产品失败: {str(e)}")
            return []


# 初始化数据库连接和表结构的方法
def initialize_database():
    """初始化数据库，创建必要的索引和结构"""
    try:
        data_access = DataAccess()
        logger.info("数据库初始化成功")
        return data_access
    except Exception as e:
        logger.error(f"数据库初始化失败: {str(e)}")
        raise


# 单例模式，确保只有一个数据库连接实例
_data_access_instance = None

def get_data_access() -> DataAccess:
    """获取数据访问层实例"""
    global _data_access_instance
    if _data_access_instance is None:
        _data_access_instance = initialize_database()
    return _data_access_instance 