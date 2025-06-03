<!-- 定义核心占位符 -->
<!--
  {app_name}: 项目/应用根目录名 (例如: "ai_wellness_advisor")。
  {module_name}: {app_name} 内的模块名 (例如: "bmi", "wellness_profile")。
  {FeatureName}: 驼峰式特性名 (例如: "BMICalculation", "ComprehensiveProfileModel")。
  {feature_name}: 下划线式特性名 (例如: "bmi_calculation", "comprehensive_profile_model")。
  {NN}: 特性两位数序号 (例如: "01", "02")。
  {CURRENT_EXERCISE_DIR}: 当前练习指导文件所在的目录名 (例如: "exercise_tdd_bmi", "exercise_tdd_awa_core")。
-->

# Practice: {{PRACTICE_TITLE}}
{{#if PRACTICE_VERSION}} > 版本: {{PRACTICE_VERSION}} {{/if}}

> **工作目录说明**：本文档位于 `{{CURRENT_EXERCISE_DIR}}/` 目录下（相对于项目根目录）。所有文件引用路径均基于此目录或项目根目录。例如，`../tdd_rules/tdd_ai_thinking.md` 指向的是项目根目录下的 `tdd_rules/tdd_ai_thinking.md`。
>
> {{#if MAIN_IMPLEMENTATION_PATH_INFO}}
> **实现目录说明**：本练习系列的实际代码实现位于 `../{app_name}/src/{{MAIN_IMPLEMENTATION_PATH_INFO.module_name_for_path}}/`，测试代码位于 `../{app_name}/tests/{{MAIN_IMPLEMENTATION_PATH_INFO.module_name_for_path}}/`，相关的TDD开发过程文档位于 `../{app_name}/dev_cycles/{{MAIN_IMPLEMENTATION_PATH_INFO.module_name_for_path}}/`。
> {{else if SPECIFIC_TECH_IMPLEMENTATION_PATH_INFO}}
> **实现目录说明**：本练习的实际实现位于 `{{SPECIFIC_TECH_IMPLEMENTATION_PATH_INFO.base_path}}/` 目录下 (相对于 `{{CURRENT_EXERCISE_DIR}}/`)。
> {{/if}}

(核心开发理念参考: [测试驱动开发核心理念](../tdd_rules/tdd_ai_thinking.md))
(单元测试设计参考: [TDD单元测试设计技巧](../tdd_rules/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](../tdd_rules/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))
{{#if PROJECT_OVERVIEW_LINK}}
(项目整体结构参考: [项目整体目录结构](../README_folders.md))
{{/if}}

## 1. User Story (用户故事)

# {{USER_STORY_MAIN_TITLE}}

> **重要约束**：
> 1. 在整个实践过程中，请确保所有在Cursor/Trae中的交互对话均使用中文，这是出于演示目的的要求。
> {{#each GENERAL_CONSTRAINTS}}
> {{this}}
> {{/each}}

{{#if TOOLKIT_DESCRIPTION}}
## 工具包说明

{{{TOOLKIT_DESCRIPTION}}}
{{/if}}

## 基础结构说明

{{#if GENERAL_PLACEHOLDER_DEFINITIONS}}
在本练习系列中，涉及到的占位符具体含义如下：
*   `{app_name}`: `{{app_name_value}}`
{{#if module_name_value_is_dynamic}}
*   `{module_name}`: 具体模块名将在各练习系列中定义 (例如 `{{EXAMPLE_MODULE_NAME_1}}`, `{{EXAMPLE_MODULE_NAME_2}}`)
{{else}}
*   `{module_name}`: `{{module_name_value}}` (具体在各特性实现部分会再次明确)
{{/if}}
{{/if}}

本实践遵循标准的TDD练习框架结构。详细的目录结构、文件命名规范以及TDD周期产出物的组织方式，请严格遵循以下权威文档：
*   [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md) (定义了特性研发周期内，如 `dev_cycles`, `src`, `tests` 中各产出物的具体组织和命名)
*   [项目整体目录结构](../README_folders.md) (定义了项目根目录及 `{app_name}` 应用的整体结构)

#### 核心命名原则摘要

1.  **特性名称 (feature_name)**：
    *   格式：`小写字母_用下划线分隔`
    *   示例：`{{EXAMPLE_FEATURE_NAME_SNAKECASE_1}}`, `{{EXAMPLE_FEATURE_NAME_SNAKECASE_2}}`
    *   要求：描述性、简洁、表明功能

{{#if SPECIFIC_NAMING_CONVENTION_DETAILS}}
{{{SPECIFIC_NAMING_CONVENTION_DETAILS}}}
{{/if}}

{{#if TDD_CYCLE_OUTPUT_PATH_INFO}}
**TDD周期产出物归档核心路径**：
本练习系列相关的每个TDD周期（例如 `ExTDD_{{NN}}_{{FeatureName}}`）的详细思考过程、约束等文档，将统一归档到主应用项目 `{app_name}` 的开发周期记录区内，具体路径为 `../{app_name}/dev_cycles/{{module_name}}/ExTDD_{{NN}}_{{FeatureName}}/` (例如 `../{{app_name_value}}/dev_cycles/{{EXAMPLE_MODULE_NAME_1}}/ExTDD_01_SampleFeature/`)。对应的代码和测试则位于 `../{app_name}/src/{{module_name}}/` 和 `../{app_name}/tests/{{module_name}}/`。

本项目中的 `practice_*.md` 文件主要作为TDD练习的起点和高级别需求描述。
{{#if DETAILED_USER_STORY_LOCATION_INFO}}
本练习中定义的各特性对应的详细用户故事文档 (`_user_story_{feature_name}.md`) 位于上述 `{app_name}` 项目的相应特性开发周期目录中。
{{/if}}
{{/if}}

{{#if SPECIFIC_DIRECTORY_STRUCTURE}}
### 目录结构规范 ({{PRACTICE_TITLE}} 特定)

在遵循 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md) 的基础上，针对本练习系列的特性，其产出物（包括中间思考文档）的组织结构如下。请务必严格遵循TDD的五个核心步骤，确保生成相应的思考过程文档：

```
ExTDD_{{NN}}_{{FeatureName}}/
├── constraints/                    # 约束条件
│   └── task_constraints.md        # 任务特定约束
├── inputs/                        # 输入文件
│   └── _user_story_{{feature_name}}.md # 用户故事 (通常链接到 dev_cycles 中的版本)
├── outputs/                       # 输出文件 (在 dev_cycles 中实际生成和归档)
│   ├── _s1_think_options_{{feature_name}}.md  # 步骤1：思考与选项分析
│   ├── _s2_think_design_{{feature_name}}.md   # 步骤2：设计思考
│   ├── _s3_think_validation_{{feature_name}}.md # 步骤3：验证逻辑思考
│   ├── test_{{feature_name}}.py              # 步骤4：编写测试 (红灯)
│   ├── {{feature_name}}.py                   # 步骤5：编写实现 (绿灯)
│   └── doc_{{feature_name}}.md               # 特性说明文档 (重构与文档)
└── README.md                      # 练习说明 (通常是本 practice_*.md 的副本或引用)
```

**重要提示**：在每个TDD周期中，务必创建 `_s1_think_options_{{feature_name}}.md`, `_s2_think_design_{{feature_name}}.md`, 和 `_s3_think_validation_{{feature_name}}.md` 这三个中间思考文档。这些文档是TDD方法论的重要组成部分，有助于记录决策过程、设计思路和验证策略，确保开发过程的严谨性和可追溯性。跳过这些步骤将视为未完整执行TDD流程。

{{{SPECIFIC_DIRECTORY_STRUCTURE}}}
{{/if}}

{{#if FEATURES_OVERVIEW_TITLE}}
## {{FEATURES_OVERVIEW_TITLE}}
{{/if}}

{{#each FEATURES}}
### {{#if IS_EXERCISE_SERIES}}{{../SERIES_PREFIX}} {{FEATURE_INDEX_PADDED}}: {{else}}{{@index_plus_1}}. {{/if}}`{{FEATURE_ID_PREFIX}}_{{#unless IS_EXERCISE_SERIES}}{{FEATURE_INDEX_PADDED}}_{{/unless}}{{FEATURE_NAME_CAMELCASE}}` - {{FEATURE_FRIENDLY_TITLE}}

{{#if EXERCISE_SERIES_DETAILS}}
*   **目标**: {{EXERCISE_SERIES_DETAILS.goal}}
*   **对应 `README_prj.md` 模块**: {{EXERCISE_SERIES_DETAILS.readme_prj_module}}
*   **建议模块名 (`{module_name}`)**: `{{EXERCISE_SERIES_DETAILS.suggested_module_name}}`
*   **包含特性 (Features)**:
    {{#each EXERCISE_SERIES_DETAILS.sub_features}}
    1.  **`{{this.id}}`**:
        *   **用户故事**: {{this.user_story}}
        *   **核心任务**: {{this.core_task}}
    {{/each}}
{{else if SINGLE_FEATURE_DETAILS}}
**模块名 (`{module_name}` within `{app_name}`):** `{{SINGLE_FEATURE_DETAILS.module_name}}`
**特性名 (Feature Name - snake_case):** `{{SINGLE_FEATURE_DETAILS.feature_name_snakecase}}`
{{#if SINGLE_FEATURE_DETAILS.feature_dev_dir_camelcase}}
**特性开发目录 (Feature Development Directory - CamelCase):** `{{SINGLE_FEATURE_DETAILS.feature_dev_dir_camelcase}}`
{{/if}}

{{#if SINGLE_FEATURE_DETAILS.tdd_cycle_docs_path}}
对应的TDD周期文档存放路径：`{{SINGLE_FEATURE_DETAILS.tdd_cycle_docs_path}}`
(其内部文件结构及对应的代码/测试路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))
{{/if}}

{{#if SINGLE_FEATURE_DETAILS.specific_paths_overview}}
**相关文件路径概览 (Paths within `{app_name}` project):**
{{{SINGLE_FEATURE_DETAILS.specific_paths_overview}}}
{{/if}}

{{#if SINGLE_FEATURE_DETAILS.specific_directory_structure_snippet}}
```
{{{SINGLE_FEATURE_DETAILS.specific_directory_structure_snippet}}}
```
{{/if}}

#### 核心用户需求 ({{FEATURE_ID_PREFIX}}_{{FEATURE_NAME_CAMELCASE}})
> {{CORE_USER_NEED}}

**TDD核心循环提示**：请务必遵循完整的TDD五步循环，包括创建 `_s1_think_options_{{feature_name}}.md`, `_s2_think_design_{{feature_name}}.md`, 和 `_s3_think_validation_{{feature_name}}.md` 等中间思考文档。
{{/if}}
{{/each}}

{{#if IMPORTANT_NOTES}}
**重要提示**:
{{#each IMPORTANT_NOTES}}
- {{this}}
{{/each}}
{{/if}}

{{#if GENERAL_CONSTRAINTS_SECTION}}
## 通用约束
{{{GENERAL_CONSTRAINTS_SECTION}}}
{{/if}}

{{#if LEARNING_ORDER_SECTION}}
## 建议学习顺序
{{{LEARNING_ORDER_SECTION}}}
{{/if}}

{{#if TECH_DEPENDENCIES_SECTION}}
## 技术依赖
{{{TECH_DEPENDENCIES_SECTION}}}
{{/if}}

{{#if DIFFICULTY_PROGRESSION_SECTION}}
## 练习难度递进
{{{DIFFICULTY_PROGRESSION_SECTION}}}
{{/if}}