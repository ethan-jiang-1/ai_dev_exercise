# S2: 设计方案 - Pydantic用户健康档案模型 (ExTDD_01_PydanticUserProfile)

**特性名称**: `pydantic_user_profile`
**模块名称**: `data_models`
**TDD周期**: `ExTDD_01_PydanticUserProfile`

## 1. 目标模型: `UserProfile`

基于用户故事和S1的思考，我们将设计 `UserProfile` Pydantic模型。

## 2. Pydantic模型定义

```python
from typing import List, Optional, Literal
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field, validator

class UserProfile(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    age: int = Field(..., gt=0, lt=120, description="User's age in years")
    gender: Literal['male', 'female', 'other'] = Field(..., description="User's gender")
    height_cm: float = Field(..., gt=0, description="User's height in centimeters")
    weight_kg: float = Field(..., gt=0, description="User's weight in kilograms")
    health_goals: List[str] = Field(..., min_length=1, description="List of user's health goals")
    allergies: Optional[List[str]] = Field(default=None, description="List of user's allergies")
    medical_conditions: Optional[List[str]] = Field(default=None, description="List of user's medical conditions")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of profile creation")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of last profile update")

    # 自动更新 updated_at 字段的校验器
    @validator('updated_at', always=True)
    def set_updated_at(cls, v, values):
        # 如果是新建或者其他字段有变动，则更新 updated_at
        # 这里的逻辑可以更复杂，例如只在特定字段更改时更新
        # 为简单起见，这里每次验证都更新为当前时间，或者可以比较与 created_at
        # 更稳妥的做法是在应用层面，当数据实际发生变更并持久化前更新此字段
        # 此处暂时设置为与 created_at 相同，或在模型被访问/验证时更新
        # Pydantic v2 中，推荐使用 model_validator
        return datetime.utcnow()

    class Config:
        validate_assignment = True # 允许在字段赋值时进行验证
        json_encoders = {
            UUID: lambda v: str(v), # 将 UUID 对象序列化为字符串
            datetime: lambda v: v.isoformat() # 将 datetime 对象序列化为 ISO 格式字符串
        }
        # Pydantic V2 移除了 anystr_strip_whitespace, 需要在 validator 中处理
        # Pydantic V2 推荐使用 model_config 而不是 Config
        # title = "User Health Profile"
        # schema_extra = {
        #     "example": {
        #         "user_id": "123e4567-e89b-12d3-a456-426614174000",
        #         "age": 30,
        #         "gender": "female",
        #         "height_cm": 165.5,
        #         "weight_kg": 60.2,
        #         "health_goals": ["Lose weight", "Improve stamina"],
        #         "allergies": ["Pollen", "Dust mites"],
        #         "medical_conditions": ["Asthma"],
        #         "created_at": "2023-01-01T10:00:00Z",
        #         "updated_at": "2023-01-02T12:00:00Z"
        #     }
        # }

# Pydantic V2 风格的 Config (如果项目使用V2)
# from pydantic import model_validator
# class UserProfileV2(BaseModel):
#     user_id: UUID = Field(default_factory=uuid4)
#     age: int = Field(..., gt=0, lt=120, description="User's age in years")
#     gender: Literal['male', 'female', 'other'] = Field(..., description="User's gender")
#     height_cm: float = Field(..., gt=0, description="User's height in centimeters")
#     weight_kg: float = Field(..., gt=0, description="User's weight in kilograms")
#     health_goals: List[str] = Field(..., min_length=1, description="List of user's health goals")
#     allergies: Optional[List[str]] = Field(default=None, description="List of user's allergies")
#     medical_conditions: Optional[List[str]] = Field(default=None, description="List of user's medical conditions")
#     created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of profile creation")
#     updated_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of last profile update")

#     @model_validator(mode='before') # Pydantic V2
#     @classmethod
#     def set_updated_at_on_update(cls, data):
#         if isinstance(data, dict):
#             data['updated_at'] = datetime.utcnow()
#         return data

#     model_config = {
#         "validate_assignment": True,
#         "json_encoders": {
#             UUID: lambda v: str(v),
#             datetime: lambda v: v.isoformat()
#         },
#         "title": "User Health Profile",
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "user_id": "123e4567-e89b-12d3-a456-426614174000",
#                     "age": 30,
#                     "gender": "female",
#                     "height_cm": 165.5,
#                     "weight_kg": 60.2,
#                     "health_goals": ["Lose weight", "Improve stamina"],
#                     "allergies": ["Pollen", "Dust mites"],
#                     "medical_conditions": ["Asthma"],
#                     # created_at and updated_at are usually set by the model
#                 }
#             ]
#         }
#     }

```

## 3. 设计决策说明

*   **`user_id`**: 使用 `UUID` 类型，并提供 `default_factory=uuid4` 以便在创建实例时自动生成唯一的ID。在序列化为JSON时，通过 `json_encoders` 将 `UUID` 对象转换为字符串。
*   **`age`**: `int` 类型，使用 `Field(gt=0, lt=120)` 进行范围验证，确保年龄在合理范围内。
*   **`gender`**: 使用 `Literal['male', 'female', 'other']` 来限制性别选项，简单明了。
*   **`height_cm`, `weight_kg`**: `float` 类型，使用 `Field(gt=0)` 确保为正数。
*   **`health_goals`**: `List[str]` 类型，使用 `Field(min_length=1)` 确保健康目标列表不为空（至少有一个目标）。
*   **`allergies`, `medical_conditions`**: `Optional[List[str]]` 类型，默认为 `None`。这允许区分用户未提供此信息 (`None`) 和用户明确表示没有过敏/疾病史 (空列表 `[]`，由用户在输入时提供) 的情况。
*   **`created_at`, `updated_at`**: `datetime` 类型，使用 `default_factory=datetime.utcnow` 在模型实例化时自动设置为当前的UTC时间。对于 `updated_at`，添加了一个 `@validator` (针对Pydantic V1) 来尝试在验证时更新时间戳。然而，更可靠的 `updated_at` 更新机制通常在数据持久化层面处理，或者在Pydantic V2中使用 `@model_validator`。当前设计中的 `@validator('updated_at', always=True)` 会在每次验证模型时都将 `updated_at` 设置为当前时间，这可能过于频繁。一个更实际的Pydantic层面的自动更新，可能需要检查其他字段是否有变化。
    *   **简化处理**：为了TDD练习的简化，`updated_at` 的 `@validator` 暂时设置为每次验证都更新。在实际项目中，会仔细考虑其更新时机。
*   **`Config` / `model_config`**:
    *   `validate_assignment = True`: 允许在字段被赋值后重新验证模型，例如 `profile.age = -5` 会触发验证错误。
    *   `json_encoders`: 自定义 `UUID` 和 `datetime` 对象如何序列化为JSON。
    *   注释中包含了Pydantic V2风格的 `model_config` 和 `@model_validator` 作为参考，如果项目升级到Pydantic V2，应采用新风格。

## 4. 待验证的方面 (将在S3中细化)

*   所有字段的类型约束和值约束是否按预期工作。
*   `default_factory` 是否正确生成 `user_id`, `created_at`, `updated_at`。
*   `Optional` 字段的处理是否符合预期 (接受 `None`，接受空列表，接受有内容的列表)。
*   `Literal` 字段是否正确限制了输入值。
*   序列化 (`.model_dump_json()`, `.model_dump()`) 和反序列化 (`.model_validate()`, `.model_validate_json()`) 是否按预期工作，特别是对于 `UUID` 和 `datetime` 字段。
*   错误信息是否清晰。

## 5. 文件结构

*   模型代码将位于 `ai_wellness_advisor/src/data_models/pydantic_user_profile.py`。
*   测试代码将位于 `ai_wellness_advisor/tests/data_models/test_pydantic_user_profile.py`。

---
关联用户故事: [_user_story_pydantic_user_profile.md](./_user_story_pydantic_user_profile.md)
关联思考选项: [_s1_think_options_pydantic_user_profile.md](./_s1_think_options_pydantic_user_profile.md)