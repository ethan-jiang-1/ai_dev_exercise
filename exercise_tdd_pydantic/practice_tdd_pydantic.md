# Practice: Pydantic功能练习

> **工作目录说明**：本文档位于 `~/ai_dev_exercise/exercise_tdd_pydantic/` 目录下，所有文件引用路径均基于此目录。例如，`./teaching_framework/test_driven_development_with_ai.md` 实际指向 `/Users/bowhead/ai_dev_exercise/exercise_tdd_pydantic/teaching_framework/test_driven_development_with_ai.md`。
>
> **实现目录说明**：本练习的实际实现位于 `./tdd_pydantic/` 目录下。

(核心开发理念参考: [测试驱动开发核心理念](./teaching_framework/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](./teaching_framework/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](./teaching_framework/planning_tdd_exercise.md))

## 1. User Story (用户故事)

# Pydantic功能练习：AI+TDD练习实践实例

> **重要约束**：在整个实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。

## 基础结构说明

本实践遵循标准的TDD练习框架结构：

### 命名规范

1. **特性名称 (feature_name)**：
   - 格式：`小写字母_用下划线分隔`
   - 示例：`api_data_validator`, `data_serializer`
   - 要求：描述性、简洁、表明功能

2. **目录命名**：
   - 练习系列目录：`ExTDD_XX_FeatureName`
     - XX：两位数字编号（01、02等）
     - FeatureName：驼峰式命名
     - 示例：`ExTDD_01_PydanticValidation`

3. **文件命名**：
   - 思考文件：`_s{step}_{type}_{feature_name}.md`
   - 代码文件：`{feature_name}.py`
   - 测试文件：`test_{feature_name}.py`
   - 文档文件：`doc_{feature_name}.md`

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

## Pydantic功能特定实现

### 1. ExTDD_01_PydanticValidation: 实现API数据验证框架

feature_name: api_data_validator

```
ExTDD_01_PydanticValidation/
├── constraints/
│   └── task_constraints.md       # 数据验证的特定约束
├── inputs/
│   └── user_story.md            # 数据验证的用户故事
└── outputs/
    ├── _s1_think_options_api_data_validator.md
    ├── _s2_think_design_api_data_validator.md
    ├── _s3_think_validation_api_data_validator.md
    ├── api_data_validator.py
    ├── test_api_data_validator.py
    └── doc_api_data_validator.md
```

#### 核心用户需求 (ExTDD_01_PydanticValidation)
> 我希望系统能帮我检查用户填的信息对不对，比如邮箱格式、年龄范围啥的。如果填错了，要清楚地告诉用户哪里错了。

### 2. ExTDD_02_PydanticSerialization: 实现数据序列化与转换

feature_name: data_serializer

```
ExTDD_02_PydanticSerialization/
├── constraints/
│   └── task_constraints.md
├── inputs/
│   └── user_story.md
└── outputs/
    ├── _s1_think_options_data_serializer.md
    ├── _s2_think_design_data_serializer.md
    ├── _s3_think_validation_data_serializer.md
    ├── data_serializer.py
    ├── test_data_serializer.py
    └── doc_data_serializer.md
```

#### 核心用户需求 (ExTDD_02_PydanticSerialization)
> 我需要把系统里的数据（比如用户信息、订单详情）方便地转成不同的格式，有时候是给前端App看（JSON），有时候是存到文件里，或者给别的系统用。还要能处理好日期这些特殊东西。

### 3. ExTDD_03_PydanticConfig: 实现基于Pydantic的配置管理系统

feature_name: config_manager

```
ExTDD_03_PydanticConfig/
├── constraints/
│   └── task_constraints.md
├── inputs/
│   └── user_story.md
└── outputs/
    ├── _s1_think_options_config_manager.md
    ├── _s2_think_design_config_manager.md
    ├── _s3_think_validation_config_manager.md
    ├── config_manager.py
    ├── test_config_manager.py
    └── doc_config_manager.md
```

#### 核心用户需求 (ExTDD_03_PydanticConfig)
> 我希望我的程序能方便地读取各种配置信息，比如数据库地址、API密钥什么的。这些配置可能来自不同的地方，比如配置文件或者环境变量，而且有些敏感信息（像密码）得安全地存起来。

### 4. ExTDD_04_PydanticSchema: 实现API模式演进与兼容性工具

feature_name: schema_evolution

```
ExTDD_04_PydanticSchema/
├── constraints/
│   └── task_constraints.md
├── inputs/
│   └── user_story.md
└── outputs/
    ├── _s1_think_options_schema_evolution.md
    ├── _s2_think_design_schema_evolution.md
    ├── _s3_think_validation_schema_evolution.md
    ├── schema_evolution.py
    ├── test_schema_evolution.py
    └── doc_schema_evolution.md
```

#### 核心用户需求 (ExTDD_04_PydanticSchema)
> 我们的API会经常升级，加一些新功能或者改动一些旧的返回信息。我希望系统能处理好不同版本的API，老的App还能用，新的App也能用上新功能，别一升级就都坏了。最好还能自动更新API文档，让大家都知道最新的接口是啥样的。