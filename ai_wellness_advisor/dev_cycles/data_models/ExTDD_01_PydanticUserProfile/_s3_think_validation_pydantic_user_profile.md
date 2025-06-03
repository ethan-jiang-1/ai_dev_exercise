# S3: 验证思考与测试计划 - Pydantic用户健康档案模型 (ExTDD_01_PydanticUserProfile)

**特性名称**: `pydantic_user_profile`
**模块名称**: `data_models`
**TDD周期**: `ExTDD_01_PydanticUserProfile`

## 1. 核心验证目标

确保 `UserProfile` Pydantic模型能够正确地：
1.  使用有效数据成功实例化。
2.  对无效数据（类型错误、值超出约束范围、缺失必填字段等）抛出预期的 `ValidationError`。
3.  正确处理默认值和 `default_factory` 生成的字段 (`user_id`, `created_at`, `updated_at`)。
4.  正确处理 `Optional` 字段。
5.  正确处理 `Literal` 字段。
6.  能正确序列化为字典/JSON，并从字典/JSON反序列化。
7.  `updated_at` 字段能按预期（在当前设计中是每次验证时）更新。

## 2. 测试用例设计 (基于pytest)

我们将为 `ai_wellness_advisor/tests/data_models/test_pydantic_user_profile.py` 设计测试用例。

### 2.1. 成功实例化与基本字段验证

*   **`test_create_user_profile_success`**: 测试使用所有必填字段的有效数据成功创建 `UserProfile` 实例。
    *   验证实例的各个字段值是否与输入匹配。
    *   验证 `user_id`, `created_at`, `updated_at` 是否已自动生成且类型正确 (UUID, datetime)。
*   **`test_user_profile_optional_fields_default_none`**: 测试在不提供 `allergies` 和 `medical_conditions` 时，它们默认为 `None`。
*   **`test_user_profile_optional_fields_with_values`**: 测试当提供 `allergies` 和 `medical_conditions` (包括空列表和有内容的列表) 时，模型能正确接收。

### 2.2. 字段约束验证 (无效数据)

将使用 `pytest.raises(ValidationError)` 来捕获预期的验证错误。

*   **`test_age_invalid_range`**: 
    *   测试 `age` 小于等于0 (e.g., 0, -1)。
    *   测试 `age` 大于等于120 (e.g., 120, 150)。
*   **`test_age_invalid_type`**: 测试 `age` 为非整数类型 (e.g., "abc", 30.5)。
*   **`test_gender_invalid_value`**: 测试 `gender` 为非 `Literal` 定义的值 (e.g., "unknown", "malee").
*   **`test_height_cm_invalid_value`**: 测试 `height_cm` 小于等于0 (e.g., 0, -10.5)。
*   **`test_height_cm_invalid_type`**: 测试 `height_cm` 为非数字类型 (e.g., "abc").
*   **`test_weight_kg_invalid_value`**: 测试 `weight_kg` 小于等于0 (e.g., 0, -5.5)。
*   **`test_weight_kg_invalid_type`**: 测试 `weight_kg` 为非数字类型 (e.g., "abc").
*   **`test_health_goals_empty_list`**: 测试 `health_goals` 为空列表 (应失败，因为 `min_length=1`)。
*   **`test_health_goals_invalid_type`**: 测试 `health_goals` 为非列表类型，或列表中包含非字符串元素。

### 2.3. 必填字段缺失验证

*   **`test_missing_required_fields`**: 逐个测试缺少必填字段 (如 `age`, `gender`, `height_cm`, `weight_kg`, `health_goals`) 时是否抛出 `ValidationError`。
    *   例如，创建一个字典，缺少 `age`，然后尝试用 `UserProfile.model_validate()` 创建实例。

### 2.4. `created_at` 和 `updated_at` 行为验证

*   **`test_timestamps_auto_generated`**: 确认 `created_at` 和 `updated_at` 在实例化时自动生成，并且是 `datetime` 对象。
*   **`test_updated_at_updates_on_validation_or_assignment`**: 
    *   创建一个实例，记录 `updated_at` 的初始值。
    *   稍作等待。
    *   对实例的某个字段进行赋值 (由于 `validate_assignment=True`，会触发重新验证)。
    *   验证 `updated_at` 是否已更新为新的时间，且晚于初始值。
    *   或者，直接调用 `model_validate` 用相同数据再次验证，看 `updated_at` 是否更新。
    *   注意：这个测试依赖于当前 `updated_at` 的 `@validator` 设计，即每次验证都更新。如果未来修改了更新逻辑，此测试也需相应调整。

### 2.5. 序列化与反序列化验证

*   **`test_user_profile_serialization_to_json`**: 
    *   创建一个有效的 `UserProfile` 实例。
    *   调用 `.model_dump_json()` 将其序列化为JSON字符串。
    *   验证JSON字符串的结构和内容，特别是 `user_id` (应为字符串) 和 `datetime` 字段 (应为ISO格式字符串)。
*   **`test_user_profile_serialization_to_dict`**: 
    *   创建一个有效的 `UserProfile` 实例。
    *   调用 `.model_dump()` 将其序列化为字典。
    *   验证字典的结构和内容，特别是 `user_id` (应为UUID对象或字符串，取决于 `mode` 和 `by_alias` 等参数，默认应为UUID) 和 `datetime` 字段。
*   **`test_user_profile_deserialization_from_json`**: 
    *   准备一个有效的JSON字符串 (包含字符串格式的 `user_id` 和 `datetime`)。
    *   使用 `UserProfile.model_validate_json()` 从JSON字符串反序列化为 `UserProfile` 实例。
    *   验证实例的字段值是否正确，特别是 `user_id` (应为UUID对象) 和 `datetime` 字段 (应为datetime对象)。
*   **`test_user_profile_deserialization_from_dict`**: 
    *   准备一个有效的字典 (包含 `UUID` 对象或字符串形式的 `user_id`，以及 `datetime` 对象或字符串形式的 `datetime`)。
    *   使用 `UserProfile.model_validate()` 从字典反序列化为 `UserProfile` 实例。
    *   验证实例的字段值是否正确。
*   **`test_deserialization_invalid_json_data`**: 测试从包含无效数据（例如，`age` 为字符串）的JSON反序列化时是否抛出 `ValidationError`。

### 2.6. `validate_assignment` 配置验证

*   **`test_validate_assignment_works`**: 
    *   创建一个有效实例。
    *   尝试给 `age` 赋一个无效值 (e.g., -5)。
    *   验证是否因 `validate_assignment=True` 而抛出 `ValidationError`。

## 3. 测试数据准备

*   定义一组标准的有效输入数据字典，用于成功创建实例的测试。
*   为每个无效场景准备特定的无效数据。

## 4. 注意事项

*   确保测试覆盖Pydantic V1的行为。如果项目计划迁移到Pydantic V2，部分测试（特别是关于Config和验证器）可能需要调整以适应V2的API变化（例如使用 `model_config` 替代 `Config`，使用 `@model_validator` 替代某些场景的 `@validator` 或 `@root_validator`）。设计文档中已包含V2的注释作为参考。
*   `updated_at` 的测试逻辑与当前设计紧密相关。如果其更新机制改变，测试也必须同步更新。
*   考虑到时间的精度问题，比较 `datetime` 对象时，可能需要允许一定的误差，或者只比较到秒。

## 5. 下一步

基于此测试计划，下一步将是编写实际的测试代码 (`test_pydantic_user_profile.py`)，然后实现 `UserProfile` 模型 (`pydantic_user_profile.py`)，并进行TDD循环。

---
关联用户故事: [_user_story_pydantic_user_profile.md](./_user_story_pydantic_user_profile.md)
关联设计方案: [_s2_think_design_pydantic_user_profile.md](./_s2_think_design_pydantic_user_profile.md)