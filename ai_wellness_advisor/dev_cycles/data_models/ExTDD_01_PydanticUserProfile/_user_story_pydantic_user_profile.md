# 用户故事：Pydantic用户健康档案模型 (ExTDD_01_PydanticUserProfile)

**特性名称**: `pydantic_user_profile`
**模块名称**: `data_models`
**TDD周期**: `ExTDD_01_PydanticUserProfile`

## 核心用户故事

> 作为开发者，我需要使用Pydantic定义一个用户健康档案模型，该模型应包含用户的基本信息（如年龄、性别、身高、体重）、健康目标、过敏史、疾病史等关键字段，并确保这些字段的数据类型和约束得到严格验证。

## 验收标准

1.  **模型定义**：
    *   存在一个名为 `UserProfile` 的Pydantic模型。
    *   模型包含以下字段，并具有适当的数据类型和验证：
        *   `user_id`: `str` (唯一标识符, 例如 UUID)
        *   `age`: `int` (例如, 大于0, 小于120)
        *   `gender`: `str` (例如, 枚举类型: 'male', 'female', 'other')
        *   `height_cm`: `float` (身高，单位厘米, 例如, 大于0)
        *   `weight_kg`: `float` (体重，单位千克, 例如, 大于0)
        *   `health_goals`: `List[str]` (健康目标列表, 例如, \["减轻体重", "增加肌肉"])
        *   `allergies`: `Optional[List[str]]` (过敏史列表, 可选)
        *   `medical_conditions`: `Optional[List[str]]` (疾病史列表, 可选)
        *   `created_at`: `datetime` (记录创建时间, 自动生成)
        *   `updated_at`: `datetime` (记录更新时间, 自动更新)
2.  **数据验证**：
    *   `age` 必须是正整数，并在合理范围内 (例如, 1-120)。
    *   `gender` 必须是预定义的几个选项之一。
    *   `height_cm` 和 `weight_kg` 必须是正数。
    *   `health_goals` 不能为空列表（如果提供了该字段）。
    *   `created_at` 和 `updated_at` 字段能正确处理时间。
3.  **实例化与使用**：
    *   模型可以成功使用有效数据实例化。
    *   当提供无效数据（例如，类型错误、超出范围的值）时，Pydantic应能捕获错误并提供有意义的错误信息。
    *   模型可以序列化为JSON，也可以从JSON反序列化。

## 相关文档链接

*   [TDD练习高级别需求](../practice_tdd_pydantic.md)
*   [特性研发目录结构核心原则](../../../../README_folder_feature.md)
*   [Pydantic官方文档](https://docs.pydantic.dev/)