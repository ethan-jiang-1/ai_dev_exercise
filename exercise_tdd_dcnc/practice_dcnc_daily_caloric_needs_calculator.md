# Practice: 每日所需热量计算器 (Daily Caloric Needs Calculator)


(核心开发理念参考: [测试驱动开发核心理念](../tdd_rules/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](../tdd_rules/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](../tdd_rules/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

## User Story (原始用户故事)
> 作为一名关心健康的用户，我希望能够输入我的个人信息（如性别、年龄、身高、体重）和日常活动量，来计算我的基础代谢率（BMR）和每日总能量消耗（TDEE），从而更好地管理我的健康。

## 功能需求 (Feature Requirements)
1.  输入性别、年龄、身高（厘米）、体重（千克），计算基础代谢率 (BMR)。
2.  基于计算出的BMR和用户选择的日常活动量水平，计算每日总能量消耗 (TDEE)。
3.  对无效输入或计算中可能发生的异常情况提供适当反馈。

## 每日所需热量计算器 (Daily Caloric Needs Calculator): AI+TDD练习实践实例

> **重要约束**：在整个练习实践过程中，请确保所有在Cursor/Trae中的交互对话均使用中文，这是出于演示目的的要求。

### 基础结构说明

在本练习中，涉及到的占位符具体含义如下：
*   `{app_name}`: `ai_wellness_advisor`
*   `{module_name}`: `dcnc` (具体在各特性实现部分会再次明确)

本实践遵循标准的TDD练习框架结构。详细的目录结构、文件命名规范以及TDD周期产出物的组织方式，请严格遵循以下权威文档：
*   [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md) (定义了特性研发周期内，如 `dev_cycles`, `src`, `tests` 中各产出物的具体组织和命名)
*   [项目整体目录结构](../README_folders.md) (定义了项目根目录及 `{app_name}` 应用的整体结构)

#### 核心命名原则摘要

1.  **特性名称 (feature_name)**：
    *   格式：`小写字母_用下划线分隔`
    *   示例：`calculate_bmr`, `calculate_tdee`
    *   要求：描述性、简洁、表明功能

**工作目录说明**：本文档（用户故事）位于 `exercise_tdd_dcnc/` 目录下。所有与本用户故事直接相关的文件引用路径均基于此目录。例如，`../tdd_rules/test_driven_development_with_ai.md`。

**TDD周期产出物归档核心路径**：
本练习相关的每个TDD周期（例如 `ExTDD_01_CalculateBMR`）的详细思考过程、约束等文档，将统一归档到主应用项目 `{app_name}` 的开发周期记录区内，具体路径为 `../{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` (例如 `../ai_wellness_advisor/dev_cycles/dcnc/ExTDD_01_CalculateBMR/`)。对应的代码和测试快照则位于 `../{app_name}/src/{module_name}/` 和 `../{app_name}/tests/{module_name}/`。

本项目中的 `practice_*.md` 文件主要作为TDD练习的起点和高级别需求描述。

本练习中定义的各特性对应的详细用户故事文档 (`_user_story_{feature_name}.md`) 位于上述 `{app_name}` 项目的相应特性开发周期目录中，例如：
*   BMR 计算特性 (`calculate_bmr`): `../{app_name}/dev_cycles/dcnc/ExTDD_01_CalculateBMR/_user_story_calculate_bmr.md`
*   TDEE 计算特性 (`calculate_tdee`): `../{app_name}/dev_cycles/dcnc/ExTDD_02_CalculateTDEE/_user_story_calculate_tdee.md`

### TDD周期产出物遵循的规范

所有TDD练习周期的产出物，包括思考文档、源代码快照和测试代码快照的目录结构、文件命名及存放位置，均严格遵循以下权威文档的规定：
*   [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md)
*   [项目整体目录结构](../README_folders.md)

**核心要点回顾**：
*   **思考与设计文档**：位于 `{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` 目录下，详细文件列表（如 `_user_story_{feature_name}.md`, `_s1_think_options_{feature_name}.md` 等）请参见上述规范文档。
*   **源代码快照**：位于 `{app_name}/src/{module_name}/{feature_name}.py`。
*   **特性代码说明**：位于 `{app_name}/src/{module_name}/README_{feature_name}.md`。
*   **测试代码快照**：位于 `{app_name}/tests/{module_name}/test_{feature_name}.py`。

**重要提示**：
- 本文档 (`practice_dcnc_daily_caloric_needs_calculator_v2.md`) 作为练习的起点，提供了高级别的用户故事。
- 各特性更详细的用户故事阐述和演进记录位于其对应的 `dev_cycles` 目录下的 `_user_story_{feature_name}.md` 文件中。
- `dev_cycles` 目录专注于记录思考、设计和演进过程的文档，实际的代码和测试产出物位于 `src` 和 `tests` 目录中。

## 每日所需热量计算器特定实现(两个Feature)

### 1. ExTDD_01_CalculateBMR: 实现BMR值的计算

module_name: dcnc
feature_name: calculate_bmr

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_01_CalculateBMR/`
(其内部文件结构及对应的代码/测试快照路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_01_CalculateBMR) 针对Feature_01
> 用户希望输入自己的性别、年龄、身高和体重，就能知道自己每天最少需要消耗多少能量来维持生命。如果输入信息不完整或无效，希望能得到清晰的提示。

### 2. ExTDD_02_CalculateTDEE: 实现TDEE值的计算

module_name: dcnc
feature_name: calculate_tdee

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_02_CalculateTDEE/`
(其内部文件结构及对应的代码/测试快照路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_02_CalculateTDEE) 针对Feature_02
> 在知道了自己的基础代谢率（BMR）之后，用户希望通过选择自己的日常活动量水平（例如：久坐、轻度活动、中度活动、重度活动、极重度活动），来估算每天实际消耗的总热量（TDEE）。如果BMR未计算或活动量未选择，希望能得到相应的提示。