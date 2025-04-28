"""
用户API V3示例 - 最新版本，包含多种变更
"""
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, constr

# V3模型定义

class GeoLocation(BaseModel):
    """地理位置坐标"""
    latitude: float = Field(..., description="纬度", ge=-90, le=90)
    longitude: float = Field(..., description="经度", ge=-180, le=180)

class UserLocation(BaseModel):
    """用户位置信息 - 重命名并扩展了原来的UserAddress"""
    street_address: str = Field(..., description="街道地址")  # 重命名自street
    city: str = Field(..., description="城市")
    postal_code: str = Field(..., description="邮政编码")
    country_code: constr(min_length=2, max_length=2) = Field(
        ..., description="国家代码 (ISO 3166-1 alpha-2)"
    )  # 改为国家代码
    region: Optional[str] = Field(None, description="区域/省/州")
    geo: Optional[GeoLocation] = Field(None, description="地理坐标位置")

class UserPreferences(BaseModel):
    """用户偏好设置"""
    theme: str = Field("default", description="UI主题")
    language: str = Field("en", description="首选语言")
    notifications_enabled: bool = Field(True, description="是否启用通知")
    email_frequency: str = Field("daily", description="电子邮件通知频率")

class UserV3(BaseModel):
    """用户模型 - API V3"""
    id: UUID = Field(..., description="用户唯一标识符 (UUID格式)")
    username: str = Field(..., description="用户名", min_length=3, max_length=50)
    email: EmailStr = Field(..., description="电子邮件地址")
    first_name: str = Field(..., description="名")
    last_name: str = Field(..., description="姓")
    is_active: bool = Field(True, description="账户是否激活")
    location: Optional[UserLocation] = Field(None, description="用户位置")
    created_at: datetime = Field(..., description="账户创建时间")
    updated_at: Optional[datetime] = Field(None, description="最后更新时间")
    last_login: Optional[datetime] = Field(None, description="最后登录时间")
    roles: List[str] = Field(["user"], description="用户角色列表")
    preferences: Union[Dict[str, Any], UserPreferences] = Field(
        {}, description="用户偏好设置"
    )
    account_tier: str = Field("free", description="账户等级")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                "username": "johndoe",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "is_active": True,
                "location": {
                    "street_address": "123 Main St",
                    "city": "New York",
                    "postal_code": "10001",
                    "country_code": "US",
                    "region": "NY",
                    "geo": {
                        "latitude": 40.7128,
                        "longitude": -74.006
                    }
                },
                "created_at": "2023-01-15T08:30:00Z",
                "updated_at": "2023-05-20T14:25:30Z",
                "last_login": "2023-05-21T09:15:42Z",
                "roles": ["user", "premium"],
                "preferences": {
                    "theme": "dark",
                    "language": "en",
                    "notifications_enabled": True,
                    "email_frequency": "weekly"
                },
                "account_tier": "premium"
            }
        }

# API响应模型

class PaginationMeta(BaseModel):
    """分页元数据"""
    total: int
    page: int
    size: int
    pages: int

class Links(BaseModel):
    """HATEOAS链接"""
    self: str
    next: Optional[str] = None
    prev: Optional[str] = None
    first: str
    last: str

class UserListResponseV3(BaseModel):
    """用户列表响应 - 新的JSON:API兼容格式"""
    data: List[UserV3]
    meta: PaginationMeta
    links: Links

class ErrorDetail(BaseModel):
    """详细错误信息"""
    field: Optional[str] = None
    code: str
    message: str

class ErrorResponseV3(BaseModel):
    """错误响应 - 增强版"""
    status: int
    title: str
    details: List[ErrorDetail]
    trace_id: Optional[str] = None

# 版本兼容注解示例
"""
# 使用自定义装饰器处理版本兼容

@versioned_route("/api/users/{user_id}", ["v1", "v2", "v3"])
async def get_user(
    user_id: str,
    version: str = Header("v3", alias="API-Version")
):
    # 获取用户数据
    user_data = await user_service.get_user(user_id)
    
    # 根据请求版本转换响应
    if version == "v1":
        # 转换UUID到int (如果可能)
        # 转换first_name/last_name到full_name
        # 转换location到address
        # 转换roles到单个role
        return convert_to_v1(user_data)
    
    elif version == "v2":
        # 部分转换...
        return convert_to_v2(user_data)
    
    # 默认返回v3格式
    return user_data

# 字段弃用标记示例
class UserV2(BaseModel):
    # ...
    full_name: Optional[str] = Field(
        None, 
        description="用户全名 (已弃用，将在v4中移除。请使用first_name和last_name)",
        deprecated=True
    )
    # ...
""" 