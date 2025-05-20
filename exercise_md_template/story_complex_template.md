# User Story: {{STORY_THEME_TITLE}}

> **工作目录说明**：本文档位于 `{{USER_WORKSPACE_ROOT}}/{{CURRENT_EXERCISE_COLLECTION_DIR_NAME}}/` 目录下，所有文件引用路径均基于此目录。例如，`./teaching_framework/thinking_driven_development_with_ai.md` 实际指向 `{{USER_WORKSPACE_ROOT}}/{{CURRENT_EXERCISE_COLLECTION_DIR_NAME}}/teaching_framework/thinking_driven_development_with_ai.md`。
>
> **实现目录说明**：本练习的实际实现位于 `./{{MAIN_IMPLEMENTATION_DIR_NAME}}/` 目录下。

(核心开发理念参考: [AI辅助思考驱动开发](./teaching_framework/thinking_driven_development_with_ai_complex.md))
(练习框架规划参考: [复杂场景MDS练习框架规划](./teaching_framework/planning_mds_exercise_complex.md))

## 1. 整体概述 (Overall Overview)

# {{STORY_TITLE_WITH_THEME}}

### 1.1. 项目/产品愿景 (Project/Product Vision)
{{PROJECT_VISION_PLACEHOLDER}}

### 1.2. 核心挑战与目标 (Core Challenges & Objectives)
{{CORE_CHALLENGES_OBJECTIVES_PLACEHOLDER}}

### 1.3. 目标学习者/用户 (Target Audience of this Exercise)
{{TARGET_AUDIENCE_PLACEHOLDER}}

### 1.4. 重要约束 (Overall Constraints)
> 重要约束将在此列出，每行以'> '开头。
> {{ADDITIONAL_OVERALL_CONSTRAINTS_PLACEHOLDER}}

## 2. 核心角色/人设 (Key Personas)

{{#each PERSONAS}}
### 2.{{PERSONA_INDEX}}. {{PERSONA_NAME}}
*   **简介**: {{PERSONA_DESCRIPTION}}
*   **主要目标**: {{PERSONA_GOALS}}
*   **关键任务**: {{PERSONA_KEY_TASKS}}
*   **痛点/需求**: {{PERSONA_PAIN_POINTS_NEEDS}}
{{/each}}
{{NO_PERSONAS_DEFINED_PLACEHOLDER}}

## 3. 主要输入数据与环境 (Key Inputs & Environment)

### 3.1. 数据源 (Data Sources)
{{#each DATA_SOURCES}}
*   **名称**: {{DATA_SOURCE_NAME}}
    *   **类型/格式**: {{DATA_SOURCE_TYPE_FORMAT}}
    *   **描述/示例链接**: {{DATA_SOURCE_DESCRIPTION_EXAMPLE}}
{{/each}}
{{NO_DATA_SOURCES_DEFINED_PLACEHOLDER}}

### 3.2. 技术栈与工具 (Tech Stack & Tools)
{{TECH_STACK_TOOLS_PLACEHOLDER}}

### 3.3. 环境配置要求 (Environment Setup)
{{ENVIRONMENT_SETUP_PLACEHOLDER}}

## 4. 场景片段/核心用例 (Scenario Segments / Core Use Cases)

本练习遵循模块化的场景/用例结构进行开发。

### 4.1. 命名规范
*   **用例目录名 (UseCase Directory Name)**: `UseCase_XX_UseCaseNameCamelCase` (XX为两位数字编号)
*   **用例特性名 (UseCase Feature Name - snake_case)**: `use_case_name_snake_case` (用于文件名)
*   **思考文件**: `_s{step}_{type}_{use_case_name_snake_case}.md`
*   **代码/配置文件**: 根据实际需要命名，建议与 `use_case_name_snake_case` 相关。

### 4.2. 标准目录结构 (Standard Directory Structure per UseCase)

每个核心用例 (`UseCase_XX_UseCaseNameCamelCase`) 都建议（或强制）包含以下结构：

```
{{MAIN_IMPLEMENTATION_DIR_NAME}}/UseCase_XX_UseCaseNameCamelCase/
├── inputs/                             # 该用例特定的输入数据、配置文件等
│   └── (e.g., data_config.yaml, sample_data.csv, user_profile.json)
├── outputs/                            # 该用例期望的各种产出物
│   ├── api_specs/                      # (e.g., openapi_spec.yaml)
│   ├── data_models/                    # (e.g., database_schema.sql, entity_diagram.png)
│   ├── reports/                        # (e.g., analysis_report.pdf, evaluation_results.md)
│   ├── arch_diagrams/                  # (e.g., system_flow.drawio.png)
│   ├── code/                           # 实际代码实现 (如果涉及)
│   │   ├── {{EXAMPLE_USECASE_NAME_SNAKECASE}}.py
│   │   └── test_{{EXAMPLE_USECASE_NAME_SNAKECASE}}.py
│   └── (other_outputs_as_needed)/
├── constraints/                        # 该用例特定的约束
│   └── task_constraints.md
├── thinking_steps/                     # 思考过程记录 (核心产出)
│   ├── _s1_understand_problem_and_scope_{{EXAMPLE_USECASE_NAME_SNAKECASE}}.md
│   ├── _s2_explore_options_and_tradeoffs_{{EXAMPLE_USECASE_NAME_SNAKECASE}}.md
│   ├── _s3_design_solution_architecture_{{EXAMPLE_USECASE_NAME_SNAKECASE}}.md
│   ├── _s4_plan_implementation_and_validation_{{EXAMPLE_USECASE_NAME_SNAKECASE}}.md
│   └── (additional_thinking_steps_as_needed).md
└── README.md                           # 该用例的详细说明、目标、步骤等
```

### 4.3. 用例详述 (UseCase Details)

{{#each SCENARIO_SEGMENTS}}
#### 4.3.{{SEGMENT_INDEX_PADDED}}. UseCase_{{SEGMENT_INDEX_PADDED}}_{{SEGMENT_NAME_CAMELCASE}}: {{SEGMENT_FRIENDLY_TITLE}}

*   **用例特性名 (snake_case)**: `{{SEGMENT_NAME_SNAKECASE}}`
*   **建议目录结构**:
    ```
    {{MAIN_IMPLEMENTATION_DIR_NAME}}/UseCase_{{SEGMENT_INDEX_PADDED}}_{{SEGMENT_NAME_CAMELCASE}}/
    ├── inputs/
    │   └── ...
    ├── outputs/
    │   ├── ... (根据实际产出调整)
    │   └── code/
    │       ├── {{SEGMENT_NAME_SNAKECASE}}.py (如果适用)
    │       └── test_{{SEGMENT_NAME_SNAKECASE}}.py (如果适用)
    ├── constraints/
    │   └── task_constraints.md
    ├── thinking_steps/
    │   ├── _s1_understand_problem_and_scope_{{SEGMENT_NAME_SNAKECASE}}.md
    │   ├── _s2_explore_options_and_tradeoffs_{{SEGMENT_NAME_SNAKECASE}}.md
    │   ├── _s3_design_solution_architecture_{{SEGMENT_NAME_SNAKECASE}}.md
    │   ├── _s4_plan_implementation_and_validation_{{SEGMENT_NAME_SNAKECASE}}.md
    └── README.md
    ```
*   **核心用户/业务目标 (Core User/Business Goal)**:
    > {{SEGMENT_CORE_GOAL}}
*   **涉及人设 (Involved Personas)**: {{SEGMENT_INVOLVED_PERSONAS_LIST}}
*   **触发条件 (Triggers)**: {{SEGMENT_TRIGGERS}}
*   **主要步骤/交互流程 (Key Steps / Interaction Flow)**:
    {{SEGMENT_KEY_STEPS_MARKDOWN_LIST}}
*   **预期结果/产出物 (Expected Outcomes / Artifacts)**:
    {{SEGMENT_EXPECTED_OUTCOMES_MARKDOWN_LIST}}
*   **关键验收标准 (Key Acceptance Criteria)**:
    {{SEGMENT_ACCEPTANCE_CRITERIA_MARKDOWN_LIST}}
{{/each}}
{{NO_SCENARIO_SEGMENTS_DEFINED_PLACEHOLDER}}

## 5. 全局非功能性需求 (Global Non-Functional Requirements)

### 5.1. 性能 (Performance)
{{NFR_PERFORMANCE_PLACEHOLDER}}

### 5.2. 安全 (Security)
{{NFR_SECURITY_PLACEHOLDER}}

### 5.3. 合规性 (Compliance)
{{NFR_COMPLIANCE_PLACEHOLDER}}

### 5.4. 可用性 (Usability)
{{NFR_USABILITY_PLACEHOLDER}}

### 5.5. 可靠性 (Reliability)
{{NFR_RELIABILITY_PLACEHOLDER}}

### 5.6. 可扩展性 (Scalability)
{{NFR_SCALABILITY_PLACEHOLDER}}

### 5.7. 可维护性 (Maintainability)
{{NFR_MAINTAINABILITY_PLACEHOLDER}}

{{ADDITIONAL_NFRS_PLACEHOLDER}}

## 6. 可选补充信息 (Optional Supplementary Information)

### 6.1. 建议学习/执行顺序 (Suggested Learning/Execution Order)
{{OPTIONAL_LEARNING_ORDER_PLACEHOLDER}}

### 6.2. 难度递进说明 (Difficulty Progression)
{{OPTIONAL_DIFFICULTY_PROGRESSION_PLACEHOLDER}}

### 6.3. 常见问题FAQ (Frequently Asked Questions)
{{OPTIONAL_FAQ_PLACEHOLDER}}

### 6.4. 术语表 (Glossary)
{{OPTIONAL_GLOSSARY_PLACEHOLDER}} 