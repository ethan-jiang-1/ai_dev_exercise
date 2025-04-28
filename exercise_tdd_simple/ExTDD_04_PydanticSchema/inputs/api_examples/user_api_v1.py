"""
用户API V1示例 - 初始版本
"""
from datetime import datetime
from typing import Dict, List, Optional, Any

from pydantic import BaseModel, EmailStr, Field

# V1模型定义

class UserAddress(BaseModel):
    """用户地址信息"""
    street: str = Field(..., description="街道地址")
    city: str = Field(..., description="城市")
    postal_code: str = Field(..., description="邮政编码")
    country: str = Field(..., description="国家")

class UserV1(BaseModel):
    """用户模型 - API V1"""
    id: int = Field(..., description="用户唯一标识符")
    username: str = Field(..., description="用户名", min_length=3, max_length=50)
    email: EmailStr = Field(..., description="电子邮件地址")
    full_name: str = Field(..., description="用户全名")
    is_active: bool = Field(True, description="账户是否激活")
    address: Optional[UserAddress] = Field(None, description="用户地址")
    created_at: datetime = Field(..., description="账户创建时间")
    role: str = Field("user", description="用户角色")
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john.doe@example.com",
                "full_name": "John Doe",
                "is_active": True,
                "address": {
                    "street": "123 Main St",
                    "city": "New York",
                    "postal_code": "10001",
                    "country": "USA"
                },
                "created_at": "2023-01-15T08:30:00Z",
                "role": "user"
            }
        }

# API响应模型

class UserListResponse(BaseModel):
    """用户列表响应"""
    items: List[UserV1]
    total: int
    page: int
    size: int

class ErrorResponse(BaseModel):
    """错误响应"""
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None

# 接口示例
"""
以下是FastAPI接口示例（注释形式展示，不实际实现）

@app.get("/api/v1/users/{user_id}", response_model=UserV1, responses={404: {"model": ErrorResponse}})
async def get_user(user_id: int):
    \"\"\"获取指定用户信息\"\"\"
    # 实现代码...
    return user

@app.get("/api/v1/users", response_model=UserListResponse)
async def list_users(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    role: Optional[str] = None
):
    \"\"\"获取用户列表\"\"\"
    # 实现代码...
    return {
        "items": users,
        "total": total_count,
        "page": page,
        "size": size
    }

@app.post("/api/v1/users", response_model=UserV1, status_code=201)
async def create_user(user: UserV1):
    \"\"\"创建新用户\"\"\"
    # 实现代码...
    return created_user

@app.put("/api/v1/users/{user_id}", response_model=UserV1)
async def update_user(user_id: int, user: UserV1):
    \"\"\"更新用户信息\"\"\"
    # 实现代码...
    return updated_user

@app.delete("/api/v1/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    \"\"\"删除用户\"\"\"
    # 实现代码...
    return None
""" 