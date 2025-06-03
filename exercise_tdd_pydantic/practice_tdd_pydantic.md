# Practice: Pydantic 在AI个性化健康顾问中的应用

> **工作目录说明**：本文档位于 `exercise_tdd_pydantic/` 目录下（相对于项目根目录）。所有文件引用路径均基于此目录。例如，`../tdd_rules/tdd_ai_thinking.md` 指向的是项目根目录下的 `tdd_rules/tdd_ai_thinking.md`。

(核心开发理念参考: [测试驱动开发核心理念](../tdd_rules/tdd_ai_thinking.md))
(单元测试设计参考: [TDD单元测试设计技巧](../tdd_rules/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](../tdd_rules/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

## User Story (原始用户故事)
> 作为AI个性化健康顾问系统的开发者，我希望使用Pydantic来定义和验证系统中的核心数据模型，如用户健康档案、饮食记录、运动计划等，以确保数据的准确性、一致性和可靠性，从而提升系统的稳定性和开发效率。

## 功能需求 (Feature Requirements)
1.  **用户健康档案模型定义与验证**：使用Pydantic定义用户健康档案模型，包含基本信息、健康目标、过敏史、疾病史等，并进行数据校验。
2.  **饮食记录模型定义与验证**：使用Pydantic定义饮食记录模型，包含食物名称、分量、营养成分、用餐时间等，并进行数据校验。
3.  **运动计划模型定义与验证**：使用Pydantic定义运动计划模型，包含运动类型、持续时间、强度、目标消耗卡路里等，并进行数据校验。
4.  确保所有模型定义清晰、易于维护，并能与其他模块（如LLM集成模块）无缝对接。

## Pydantic数据模型实践：AI+TDD练习实例

> **重要约束**：
> 1. 在整个实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。
> 2. 本练习系列专注于Pydantic在数据建模和验证方面的应用。

### 基础结构说明

在本练习中，涉及到的占位符具体含义如下：
*   `{app_name}`: `ai_wellness_advisor`
*   `{module_name}`: `data_models` (用于存放Pydantic模型相关代码)

本实践遵循标准的TDD练习框架结构。详细的目录结构、文件命名规范以及TDD周期产出物的组织方式，请严格遵循以下权威文档：
*   [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md) (定义了特性研发周期内，如 `dev_cycles`, `src`, `tests` 中各产出物的具体组织和命名)
*   [项目整体目录结构](../README_folders.md) (定义了项目根目录及 `{app_name}` 应用的整体结构)

#### 核心命名原则摘要

1.  **特性名称 (feature_name)**：
    *   格式：`pydantic_小写字母_用下划线分隔` (为了清晰表明是Pydantic模型相关的特性)
    *   示例：`pydantic_user_profile`, `pydantic_diet_log`, `pydantic_exercise_plan`
    *   要求：描述性、简洁、表明功能及与Pydantic的关联

**工作目录说明**：本文档（用户故事）位于 `exercise_tdd_pydantic/` 目录下。所有与本用户故事直接相关的文件引用路径均基于此目录。例如，`../tdd_rules/tdd_ai_thinking.md`。

**TDD周期产出物归档核心路径**：
本练习相关的每个TDD周期（例如 `ExTDD_01_PydanticUserProfile`）的详细思考过程、约束等文档，将统一归档到主应用项目 `{app_name}` 的开发周期记录区内，具体路径为 `../{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` (例如 `../ai_wellness_advisor/dev_cycles/data_models/ExTDD_01_PydanticUserProfile/`)。对应的代码和测试则位于 `../{app_name}/src/{module_name}/` 和 `../{app_name}/tests/{module_name}/`。

本项目中的 `practice_*.md` 文件主要作为TDD练习的起点和高级别需求描述。

本练习中定义的各特性对应的详细用户故事文档 (`_user_story_{feature_name}.md`) 位于上述 `{app_name}` 项目的相应特性开发周期目录中，例如：
*   用户健康档案模型特性 (`pydantic_user_profile`): `../{app_name}/dev_cycles/data_models/ExTDD_01_PydanticUserProfile/_user_story_pydantic_user_profile.md`
*   饮食记录模型特性 (`pydantic_diet_log`): `../{app_name}/dev_cycles/data_models/ExTDD_02_PydanticDietLog/_user_story_pydantic_diet_log.md`
*   运动计划模型特性 (`pydantic_exercise_plan`): `../{app_name}/dev_cycles/data_models/ExTDD_03_PydanticExercisePlan/_user_story_pydantic_exercise_plan.md`

### TDD周期产出物遵循的规范

所有TDD练习周期的产出物，包括思考文档、源代码和测试代码的目录结构、文件命名及存放位置，均严格遵循以下权威文档的规定：
*   [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md)
*   [项目整体目录结构](../README_folders.md)

**核心要点回顾**：
*   **思考与设计文档**：位于 `{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` 目录下，详细文件列表（如 `_user_story_{feature_name}.md`, `_s1_think_options_{feature_name}.md`, `_s2_think_design_{feature_name}.md`, `_s3_think_validation_{feature_name}.md` 等）请参见上述规范文档。这些文档记录了TDD周期的关键思考过程，是确保AI辅助开发过程透明化和可追溯性的重要环节，**强烈建议在每个TDD周期中按规范创建，以完整体现思考和决策过程**。
*   **源代码**：位于 `{app_name}/src/{module_name}/{feature_name}.py`。
*   **特性代码说明**：位于 `{app_name}/src/{module_name}/README_{feature_name}.md`。
*   **测试代码**：位于 `{app_name}/tests/{module_name}/test_{feature_name}.py`。

**重要提示**：
- 本文档 (`practice_tdd_pydantic.md`) 作为练习的起点，提供了高级别的用户故事。
- 各特性更详细的用户故事阐述和演进记录位于其对应的 `dev_cycles` 目录下的 `_user_story_{feature_name}.md` 文件中。
- `dev_cycles` 目录专注于记录思考、设计和演进过程的文档，实际的代码和测试产出物位于 `src` 和 `tests` 目录中。
- 在每个TDD周期中，务必创建 `_s1_think_options_{feature_name}.md`, `_s2_think_design_{feature_name}.md`, 和 `_s3_think_validation_{feature_name}.md` 这三个中间思考文档。

## Pydantic 在健康顾问项目中的特定实现 (三个Feature)

### 1. ExTDD_01_PydanticUserProfile: 用户健康档案模型

> **重要提示**：开始此特性练习时，请务必遵循完整的TDD五步循环，包括创建用户故事 (`_user_story_pydantic_user_profile.md`) 以及所有相关的思考文档 (`_s1_think_options_pydantic_user_profile.md`, `_s2_think_design_pydantic_user_profile.md`, `_s3_think_validation_pydantic_user_profile.md` 等)，然后再编写测试、实现代码和重构。

module_name: data_models
feature_name: pydantic_user_profile

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_01_PydanticUserProfile/`
(其内部文件结构及对应的代码/测试路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_01_PydanticUserProfile) 针对Feature_01
> 作为开发者，我需要使用Pydantic定义一个用户健康档案模型，该模型应包含用户的基本信息（如年龄、性别、身高、体重）、健康目标、过敏史、疾病史等关键字段，并确保这些字段的数据类型和约束得到严格验证。

### 2. ExTDD_02_PydanticDietLog: 饮食记录模型

> **重要提示**：开始此特性练习时，请务必遵循完整的TDD五步循环，包括创建用户故事 (`_user_story_pydantic_diet_log.md`) 以及所有相关的思考文档 (`_s1_think_options_pydantic_diet_log.md`, `_s2_think_design_pydantic_diet_log.md`, `_s3_think_validation_pydantic_diet_log.md` 等)，然后再编写测试、实现代码和重构。

module_name: data_models
feature_name: pydantic_diet_log

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_02_PydanticDietLog/`
(其内部文件结构及对应的代码/测试路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_02_PydanticDietLog) 针对Feature_02
> 作为开发者，我需要使用Pydantic定义一个饮食记录模型，该模型应能记录用户单次餐饮的食物名称、分量、主要营养成分（如碳水化合物、蛋白质、脂肪、卡路里）以及用餐时间，并对输入数据进行有效性验证。

### 3. ExTDD_03_PydanticExercisePlan: 运动计划模型

> **重要提示**：开始此特性练习时，请务必遵循完整的TDD五步循环，包括创建用户故事 (`_user_story_pydantic_exercise_plan.md`) 以及所有相关的思考文档 (`_s1_think_options_pydantic_exercise_plan.md`, `_s2_think_design_pydantic_exercise_plan.md`, `_s3_think_validation_pydantic_exercise_plan.md` 等)，然后再编写测试、实现代码和重构。

module_name: data_models
feature_name: pydantic_exercise_plan

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_03_PydanticExercisePlan/`
(其内部文件结构及对应的代码/测试路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_03_PydanticExercisePlan) 针对Feature_03
> 作为开发者，我需要使用Pydantic定义一个运动计划模型，该模型应包含运动类型、持续时间、强度、目标消耗卡路里等字段，并确保数据的合理性和完整性。

## 技术依赖
1. **Python环境**: Python 3.8+, pip
2. **核心依赖包**: `pydantic`