<!-- 定义占位符 -->
<!-- 
{app_name}: 指代项目或应用的根目录名称，例如 "ai_wellness_advisor"。
{module_name}: 指代项目中的一个模块名称，例如 "bmi" 或 "user_profile"。
{FeatureName}: 指代模块下的一个具体特性名称，采用驼峰式命名，例如 "BMICalculation"。
{feature_name}: 指代模块下的一个具体特性名称，采用下划线命名，例如 "bmi_calculation"。
NN: 指代特性的两位数序号，例如 "01", "02"。
-->

# Practice: {{STORY_THEME_TITLE}}
> 版本: 3.0

> **工作目录说明**：本文档位于 `{{USER_WORKSPACE_ROOT}}/{{CURRENT_EXERCISE_COLLECTION_DIR_NAME}}/` 目录下，所有文件引用路径均基于此目录。例如，`../tdd_rules/test_driven_development_with_ai.md` 实际指向 `{{USER_WORKSPACE_ROOT}}/{{CURRENT_EXERCISE_COLLECTION_DIR_NAME}}/teaching_framework/test_driven_development_with_ai.md`。
>
> **实现目录说明**：本练习的实际代码实现位于 `{{USER_WORKSPACE_ROOT}}/{app_name}/src/{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/` 目录下，测试代码位于 `{{USER_WORKSPACE_ROOT}}/{app_name}/tests/{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/`，相关的TDD开发过程文档（如思考、设计、约束、用户故事、最终功能说明等）位于 `{{USER_WORKSPACE_ROOT}}/{app_name}/dev_cycles/{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/`。模板中的 `{{MAIN_IMPLEMENTATION_DIR_NAME}}` 将指代 `{app_name}` 项目内模块的相对路径，例如 `bmi` 或 `dcnc`。

(核心开发理念参考: [测试驱动开发核心理念](../tdd_rules/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](../tdd_rules/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](../tdd_rules/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

## 1. User Story (用户故事)

# {{STORY_TITLE_WITH_THEME}}: AI+TDD练习实践实例

> **重要约束**：在整个实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。
> {{ADDITIONAL_STORY_CONSTRAINTS_PLACEHOLDER}}

{{OPTIONAL_TOOLKIT_DESCRIPTION_PLACEHOLDER}}

## 基础结构说明

本实践遵循标准的TDD练习框架结构：

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

根据项目根目录下的 `README_folders.md` 和 `README_folder_feature.md` 定义，所有实际开发内容均在 `{app_name}` 项目下进行。每个特性 (Feature) 的TDD开发周期将涉及以下结构（以特性 `ExTDD_XX_FeatureName` 为例，其模块名为 `{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}`）：

**源代码目录 (`{app_name}/src/{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/`):**
```
{app_name}/
└── src/
    └── {{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/
        ├── README_{{feature_name}}.md      # 特性代码说明
        └── {{feature_name}}.py             # 功能实现代码
```

**测试代码目录 (`{app_name}/tests/{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/`):**
```
{app_name}/
└── tests/
    └── {{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/
        └── test_{{feature_name}}.py      # 测试代码
```

**开发过程与文档目录 (`{app_name}/dev_cycles/{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/`):**
```
{app_name}/
└── dev_cycles/
    └── {{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/
        └── ExTDD_XX_FeatureName/
            ├── _user_story_{feature_name}.md
            ├── _s1_think_options_{feature_name}.md
            ├── _s2_think_design_{feature_name}.md
            ├── _s3_think_validation_{feature_name}.md
            └── _constraints_{feature_name}.md # (可选)
```

**注意**: `{{MAIN_IMPLEMENTATION_DIR_NAME}}` 在此模板中通常指代 `{app_name}` 项目内的一个模块名 (例如 `bmi`, `dcnc`)，实际生成时应替换为 `{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}` 以强调其相对于 `src`, `tests`, `dev_cycles` 的路径。

## {{STORY_THEME_TITLE}} 特定实践

{{#each FEATURES}}
### {{FEATURE_INDEX_PADDED}}. ExTDD_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}: {{FEATURE_FRIENDLY_TITLE}}

**模块名 (Module Name within `{app_name}`):** `{{../MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}`
**特性名 (Feature Name - snake_case):** `{{FEATURE_NAME_SNAKECASE}}`
**特性开发目录 (Feature Development Directory - CamelCase):** `ExTDD_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}`

**相关文件路径概览 (Paths within `{app_name}` project):**

*   **源代码:** `{app_name}/src/{{../MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/{{FEATURE_NAME_SNAKECASE}}.py` (及 `README_{{FEATURE_NAME_SNAKECASE}}.md`)
*   **测试代码:** `{app_name}/tests/{{../MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/test_{{FEATURE_NAME_SNAKECASE}}.py`
*   **开发过程文档根目录:** `{app_name}/dev_cycles/{{../MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/ExTDD_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}/`
    *   用户故事: `_user_story_{{FEATURE_NAME_SNAKECASE}}.md`
    *   思考与选项: `_s1_think_options_{{FEATURE_NAME_SNAKECASE}}.md`
    *   设计方案: `_s2_think_design_{{FEATURE_NAME_SNAKECASE}}.md`
    *   验证方法: `_s3_think_validation_{{FEATURE_NAME_SNAKECASE}}.md`
    *   约束(可选): `_constraints_{{FEATURE_NAME_SNAKECASE}}.md`

```
# {app_name}/src/{{../MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/
# ├── README_{{FEATURE_NAME_SNAKECASE}}.md
# └── {{FEATURE_NAME_SNAKECASE}}.py

# {app_name}/tests/{{../MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/
# └── test_{{FEATURE_NAME_SNAKECASE}}.py

# {app_name}/dev_cycles/{{../MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}/ExTDD_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}/
# ├── _user_story_{{FEATURE_NAME_SNAKECASE}}.md
# ├── _s1_think_options_{{FEATURE_NAME_SNAKECASE}}.md
# ├── _s2_think_design_{{FEATURE_NAME_SNAKECASE}}.md
# ├── _s3_think_validation_{{FEATURE_NAME_SNAKECASE}}.md
# └── _constraints_{{FEATURE_NAME_SNAKECASE}}.md # (可选)
```

#### 核心用户需求 (ExTDD_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}})
> {{CORE_USER_NEED}}
{{/each}}

**重要提示**: 请确保在实际生成 `practice_xxx.md` 文件时，将占位符 `{{MAIN_IMPLEMENTATION_DIR_NAME}}` 或 `{{MAIN_IMPLEMENTATION_DIR_NAME_RELATIVE_TO_SRC}}` 替换为实际的模块名 (例如 `bmi`, `dcnc`, `llm_integration` 等)，并且所有路径引用都正确指向 `{app_name}` 项目内部。模板中的 `{{USER_WORKSPACE_ROOT}}` 应替换为实际的工作区根路径。

{{OPTIONAL_GENERAL_CONSTRAINTS_PLACEHOLDER}}
{{OPTIONAL_LEARNING_ORDER_PLACEHOLDER}}
{{OPTIONAL_TECH_DEPENDENCIES_PLACEHOLDER}}
{{OPTIONAL_DIFFICULTY_PROGRESSION_PLACEHOLDER}}