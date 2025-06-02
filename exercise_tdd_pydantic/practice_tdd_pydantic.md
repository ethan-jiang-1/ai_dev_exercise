# Practice: Pydantic在AI个性化健康顾问中的应用

> **工作目录说明**：本文档位于 `~/ai_dev_exercise/exercise_tdd_pydantic/` 目录下，所有文件引用路径均基于此目录。例如，`../tdd_rules/test_driven_development_with_ai.md` 实际指向 `/Users/bowhead/ai_dev_exercise/exercise_tdd_pydantic/teaching_framework/test_driven_development_with_ai.md`。
>
> **实现目录说明**：本练习的实际实现位于 `./tdd_pydantic/` 目录下。


(核心开发理念参考: [测试驱动开发核心理念](../tdd_rules/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](../tdd_rules/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](../tdd_rules/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

## 1. User Story (用户故事)

# Pydantic在AI个性化健康顾问中的应用：AI+TDD练习实践实例

本项目旨在构建一个AI个性化健康顾问系统 (`{app_name}`)，Pydantic将在其中扮演关键角色，特别是在**健康档案构建器 (`WellnessProfileBuilder`)**模块中，我们将借助 **Pydantic** 库来处理和验证用户的健康数据，如BMI（身体质量指数）、BMR（基础代谢率）、TDEE（每日总能量消耗）等。

> **重要约束**：在整个实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。

## 基础结构说明

本实践遵循标准的TDD练习框架结构：

### 命名规范

1.  **特性名称 (feature_name)**：
    *   格式：`小写字母_用下划线分隔`
    *   示例：`health_data_validation`, `health_data_persistence`
    *   要求：描述性、简洁、表明功能

2.  **目录命名**：
    *   练习系列目录：`ExTDD_XX_FeatureName`
        *   XX：两位数字编号（01、02等）
        *   FeatureName：驼峰式命名
        *   示例：`ExTDD_01_HealthDataValidation`

3.  **文件命名**：
    *   思考文件：`_s{step}_{type}_{feature_name}.md`
    *   代码文件：`{feature_name}.py`
    *   测试文件：`test_{feature_name}.py`
    *   文档文件：`doc_{feature_name}.md`

### 目录结构规范

每个练习系列都**必须, 一定**包含：

```
ExTDD_XX_FeatureName/
├── constraints/                    # 约束条件
│   └── task_constraints.md        # 任务特定约束
├── inputs/                        # 输入文件
│   └── user_story.md             # 用户故事
├── outputs/                       # 输出文件
│   ├── _s1_think_options_{feature_name}.md
│   ├── _s2_think_design_{feature_name}.md
│   ├── _s3_think_validation_{feature_name}.md
│   ├── {feature_name}.py
│   ├── test_{feature_name}.py
│   └── doc_{feature_name}.md
└── README.md                      # 练习说明
```

## Pydantic在健康顾问项目中的特定实现

我们将借助 **Pydantic** 库来完成以下用户故事：

### 1. ExTDD_01_HealthDataValidation: 实现健康数据的输入验证

feature_name: `health_data_validation`

```
ExTDD_01_HealthDataValidation/
├── constraints/
│   └── task_constraints.md       # 健康数据（如身高、体重、年龄、性别、活动水平）输入的特定约束
├── inputs/
│   └── user_story.md            # 健康数据验证的用户故事
└── outputs/
    ├── _s1_think_options_health_data_validation.md
    ├── _s2_think_design_health_data_validation.md
    ├── _s3_think_validation_health_data_validation.md
    ├── health_data_validation.py
    ├── test_health_data_validation.py
    └── doc_health_data_validation.md
```

#### 核心用户需求 (ExTDD_01_HealthDataValidation)
> 作为健康顾问系统的用户，我希望在我输入个人信息（如身高、体重、年龄、性别、活动水平等用于计算BMI, BMR, TDEE的数据）时，系统能借助 **Pydantic** 模型来验证这些数据的有效性和合理性（例如，年龄不能为负数，身高体重在合理范围内）。如果输入有误，系统应明确提示错误信息。

### 2. ExTDD_02_HealthDataPersistence: 实现健康数据的存档（序列化与保存）

feature_name: `health_data_persistence`

```
ExTDD_02_HealthDataPersistence/
├── constraints/
│   └── task_constraints.md       # 健康数据存档的特定约束（如存储格式JSON，文件命名规则等）
├── inputs/
│   └── user_story.md            # 健康数据存档的用户故事
└── outputs/
    ├── _s1_think_options_health_data_persistence.md
    ├── _s2_think_design_health_data_persistence.md
    ├── _s3_think_validation_health_data_persistence.md
    ├── health_data_persistence.py
    ├── test_health_data_persistence.py
    └── doc_health_data_persistence.md
```

#### 核心用户需求 (ExTDD_02_HealthDataPersistence)
> 作为健康顾问系统的用户，我希望系统能将我的健康档案信息（包含原始输入数据、计算出的BMI、BMR、TDEE结果等）通过 **Pydantic** 模型安全地序列化并保存到文件中（例如JSON格式），以便后续查阅或分析。

### 3. ExTDD_03_HealthDataLoading: 实现历史健康数据的加载（反序列化与读取）

feature_name: `health_data_loading`

```
ExTDD_03_HealthDataLoading/
├── constraints/
│   └── task_constraints.md       # 健康数据加载的特定约束（如从指定文件路径读取，处理文件不存在或格式错误的情况）
├── inputs/
│   └── user_story.md            # 健康数据加载的用户故事
└── outputs/
    ├── _s1_think_options_health_data_loading.md
    ├── _s2_think_design_health_data_loading.md
    ├── _s3_think_validation_health_data_loading.md
    ├── health_data_loading.py
    ├── test_health_data_loading.py
    └── doc_health_data_loading.md
```

#### 核心用户需求 (ExTDD_03_HealthDataLoading)
> 作为健康顾问系统的用户，我希望系统能够从之前保存的存档文件中加载我的历史健康数据。加载后的数据应能通过 **Pydantic** 模型正确地反序列化，并恢复为程序可用的对象，以便我查看历史记录或进行趋势分析。