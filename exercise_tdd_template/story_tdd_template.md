# User Story: {{STORY_THEME_TITLE}}
> 版本: 1.0

> **工作目录说明**：本文档位于 `{{USER_WORKSPACE_ROOT}}/{{CURRENT_EXERCISE_COLLECTION_DIR_NAME}}/` 目录下，所有文件引用路径均基于此目录。例如，`./teaching_framework/test_driven_development_with_ai.md` 实际指向 `{{USER_WORKSPACE_ROOT}}/{{CURRENT_EXERCISE_COLLECTION_DIR_NAME}}/teaching_framework/test_driven_development_with_ai.md`。
>
> **实现目录说明**：本练习的实际实现位于 `./{{MAIN_IMPLEMENTATION_DIR_NAME}}/` 目录下。

(核心开发理念参考: [测试驱动开发核心理念](./teaching_framework/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](./teaching_framework/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](./teaching_framework/planning_tdd_exercise.md))

## 1. User Story (用户故事)

# {{STORY_TITLE_WITH_THEME}}: AI+TDD练习故事实例

> **重要约束**：在整个故事实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。
> {{ADDITIONAL_STORY_CONSTRAINTS_PLACEHOLDER}}

{{OPTIONAL_TOOLKIT_DESCRIPTION_PLACEHOLDER}}

## 基础结构说明

本故事遵循标准的TDD练习框架结构：

### 命名规范

1.  **特性名称 (feature_name)**：
    *   格式：`小写字母_用下划线分隔`
    *   示例：`{{EXAMPLE_FEATURE_NAME_SNAKECASE_1}}`, `{{EXAMPLE_FEATURE_NAME_SNAKECASE_2}}`
    *   要求：描述性、简洁、表明功能

2.  **目录命名**：
    *   练习系列目录：`ExTDD_XX_FeatureName`
        *   XX：两位数字编号（01、02等）
        *   FeatureName：驼峰式命名
        *   示例：`ExTDD_01_{{EXAMPLE_FEATURE_NAME_CAMELCASE}}`

3.  **文件命名**：
    *   思考文件：`_s{step}_{type}_{feature_name}.md`
    *   代码文件：`{feature_name}.py`
    *   测试文件：`test_{feature_name}.py`
    *   文档文件：`doc_{feature_name}.md`

### 目录结构规范

每个练习系列都**必须, 一定**包含：

```
{{MAIN_IMPLEMENTATION_DIR_NAME}}/ExTDD_XX_FeatureName/
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

## {{STORY_THEME_TITLE}} 特定实现

{{#each FEATURES}}
### {{FEATURE_INDEX_PADDED}}. ExTDD_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}: {{FEATURE_FRIENDLY_TITLE}}

feature_name: {{FEATURE_NAME_SNAKECASE}}

```
{{MAIN_IMPLEMENTATION_DIR_NAME}}/ExTDD_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}/
├── constraints/
│   └── task_constraints.md        # {{FEATURE_FRIENDLY_TITLE}}的特定约束
├── inputs/
│   └── user_story.md             # {{FEATURE_FRIENDLY_TITLE}}的用户故事
└── outputs/
    ├── _s1_think_options_{{FEATURE_NAME_SNAKECASE}}.md
    ├── _s2_think_design_{{FEATURE_NAME_SNAKECASE}}.md
    ├── _s3_think_validation_{{FEATURE_NAME_SNAKECASE}}.md
    ├── {{FEATURE_NAME_SNAKECASE}}.py
    ├── test_{{FEATURE_NAME_SNAKECASE}}.py
    └── doc_{{FEATURE_NAME_SNAKECASE}}.md
```

#### 核心用户需求 (ExTDD_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}})
> {{CORE_USER_NEED}}
{{/each}}

{{OPTIONAL_GENERAL_CONSTRAINTS_PLACEHOLDER}}
{{OPTIONAL_LEARNING_ORDER_PLACEHOLDER}}
{{OPTIONAL_TECH_DEPENDENCIES_PLACEHOLDER}}
{{OPTIONAL_DIFFICULTY_PROGRESSION_PLACEHOLDER}} 