# Practice: Simple BMI Calculator

> **工作目录说明**：本文档位于 `exercise_tdd_bmi/` 目录下（相对于项目根目录 `~/ai_dev_exercise_tdd/`）。所有文件引用路径均基于此目录或项目根目录。例如，`../tdd_rules/test_driven_development_with_ai.md` 指向的是项目根目录下的 `tdd_rules/test_driven_development_with_ai.md`。

(核心开发理念参考: [测试驱动开发核心理念](../tdd_rules/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](../tdd_rules/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](../tdd_rules/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

## User Story (原始用户故事)
> 作为一名关心健康的用户，在我知道自己的BMI数值和健康状况分类。

## 功能需求 (Feature Requirements)
1.  输入身高（以米为单位）和体重（以千克为单位）,计算BMI值。
3.  根据BMI值给出健康状况分类。

## 简单BMI计算器：AI+TDD练习实践实例

> **重要约束**：在整个练习实践过程中，请确保所有在Cursor/Trae中的交互对话均使用中文，这是出于演示目的的要求。

### 基础结构说明

在本练习中，涉及到的占位符具体含义如下：
*   `{app_name}`: `ai_wellness_advisor`
*   `{module_name}`: `bmi` (具体在各特性实现部分会再次明确)

本实践遵循标准的TDD练习框架结构。详细的目录结构、文件命名规范以及TDD周期产出物的组织方式，请严格遵循以下权威文档：
*   [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md) (定义了特性研发周期内，如 `dev_cycles`, `src`, `tests` 中各产出物的具体组织和命名)
*   [项目整体目录结构](../README_folders.md) (定义了项目根目录及 `{app_name}` 应用的整体结构)

#### 核心命名原则摘要

1.  **特性名称 (feature_name)**：
    *   格式：`小写字母_用下划线分隔`
    *   示例：`bmi_calculate`, `bmi_categorize`
    *   要求：描述性、简洁、表明功能

**工作目录说明**：本文档（用户故事）位于 `exercise_tdd_bmi/` 目录下。所有与本用户故事直接相关的文件引用路径均基于此目录。例如，`../tdd_rules/test_driven_development_with_ai.md`。

**TDD周期产出物归档核心路径**：
本练习相关的每个TDD周期（例如 `ExTDD_01_BMICalculation`）的详细思考过程、约束等文档，将统一归档到主应用项目 `{app_name}` 的开发周期记录区内，具体路径为 `../{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` (例如 `../ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/`)。对应的代码和测试快照则位于 `../{app_name}/src/{module_name}/` 和 `../{app_name}/tests/{module_name}/`。

本项目中的 `practice_*.md` 文件主要作为TDD练习的起点和高级别需求描述。

本练习中定义的各特性对应的详细用户故事文档 (`_user_story_{feature_name}.md`) 位于上述 `{app_name}` 项目的相应特性开发周期目录中，例如：
*   BMI 计算特性 (`bmi_calculate`): `../{app_name}/dev_cycles/bmi/ExTDD_01_BMICalculation/_user_story_bmi_calculate.md`
*   BMI 分类特性 (`bmi_categorize`): `../{app_name}/dev_cycles/bmi/ExTDD_02_BMICategorization/_user_story_bmi_categorize.md`

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
- 本文档 (`practice_tdd_bmi_calculator.md`) 作为练习的起点，提供了高级别的用户故事。
- 各特性更详细的用户故事阐述和演进记录位于其对应的 `dev_cycles` 目录下的 `_user_story_{feature_name}.md` 文件中。
- `dev_cycles` 目录专注于记录思考、设计和演进过程的文档，实际的代码和测试产出物位于 `src` 和 `tests` 目录中。

## BMI计算器特定实现(两个Feature)

### 1. ExTDD_01_BMICalculation: 实现BMI值的计算

module_name: bmi
feature_name: bmi_calculate

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_01_BMICalculation/`
(其内部文件结构及对应的代码/测试快照路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_01_BMICalculation) 针对Feature_01
> 作为一名普通用户，我希望能方便地输入我的身高（以米为单位）和体重（以千克为单位），然后系统能帮我算出我的身体质量指数（BMI）。如果我输错了数字（比如不是有效的身高体重值），希望能得到一个友好的提示。我最主要就是想知道计算出来的BMI结果。

### 2. ExTDD_02_BMICategorization: 实现BMI值的分类

module_name: bmi
feature_name: bmi_categorize

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_02_BMICategorization/`
(其内部文件结构及对应的代码/测试快照路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_02_BMICategorization) 针对Feature_02
> 作为一名关心健康的用户，在我知道自己的BMI值之后，我还想知道这个数值到底代表什么意思，比如我是不是偏瘦了、体重是否标准，或者是不是有点超重。希望能给我一个简单明了的健康状况分类。

