# Practice: Simple BMI Calculator

(核心开发理念参考: [测试驱动开发核心理念](./teaching_framework/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](./teaching_framework/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](./teaching_framework/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

## User Story (用户故事)
作为一名关心健康的用户，在我知道自己的BMI数值和健康状况分类。



## 简单BMI计算器：AI+TDD练习实践实例

> **重要约束**：在整个实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。

### 基础结构说明

在本练习中，涉及到的占位符具体含义如下：
*   `{app_name}`: `ai_wellness_advisor`
*   `{module_name}`: `bmi` (具体在各特性实现部分会再次明确)

本实践遵循标准的TDD练习框架结构：

#### 命名规范

1. **特性名称 (feature_name)**：
   - 格式：`小写字母_用下划线分隔`
   - 示例：`bmi_calculate`, `bmi_categorize`
   - 要求：描述性、简洁、表明功能

2. **目录命名**：
   - 练习系列目录：`ExTDD_XX_FeatureName`
     - XX：两位数字编号（01、02等）
     - FeatureName：驼峰式命名
     - 示例：`ExTDD_01_BMICalculation`

3. **文件命名**：
   - 思考文件：`_s{step}_{type}_{feature_name}.md`
   - 代码文件：`{feature_name}.py`
   - 测试文件：`test_{feature_name}.py`
   - 文档文件：`doc_{feature_name}.md`

### 目录结构
**工作目录说明**：本文档（用户故事）位于 `exercise_tdd_bmi/` 目录下。所有与本用户故事直接相关的文件引用路径均基于此目录。例如，`./teaching_framework/test_driven_development_with_ai.md`。

**TDD周期产出物归档说明**：本练习相关的每个TDD周期（例如 `ExTDD_01_BMICalculation`）的详细思考过程、约束、代码实现、测试代码和周期性README等产出物，将统一归档到主应用项目 `{app_name}` 的开发周期记录区内，具体路径为 `../{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` (例如 `../ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/`)。本项目中的 `practice_*.md` 文件主要作为TDD练习的起点和高级别需求描述。

本练习中定义的各特性对应的最终用户故事文档 (`_user_story_{feature_name}.md`) 位于 `{app_name}` 项目的相应特性开发周期目录中：
 - BMI 计算特性 (`bmi_calculate`): `../{app_name}/dev_cycles/bmi/ExTDD_01_BMICalculation/_user_story_bmi_calculate.md`
 - BMI 分类特性 (`bmi_categorize`): `../{app_name}/dev_cycles/bmi/ExTDD_02_BMICategorization/_user_story_bmi_categorize.md`

### TDD周期产出物目录结构规范 (位于 `{app_name}` 项目内)

根据 [README_folder_feature.md](../README_folder_feature.md) 和 [README_folders.md](../README_folders.md) 的定义，每个TDD练习周期（例如 `ExTDD_01_BMICalculation`）的产出物，归档在 `{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` 目录下。在本练习中，`{app_name}` 为 `ai_wellness_advisor`，`{module_name}` 为 `bmi`。

例如，`ExTDD_01_BMICalculation` 的产出物将位于 `{app_name}/dev_cycles/{module_name}/ExTDD_01_BMICalculation/` (即 `ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/`)，其内部结构**必须, 一定**包含：
(此路径是相对于 `{app_name}` 项目根目录而言)

```
{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/
├── _user_story_{feature_name}.md             # 用户故事描述。
├── _s1_think_options_{feature_name}.md       # 思考过程：方案选择与分析。
├── _s2_think_design_{feature_name}.md        # 思考过程：详细设计。
├── _s3_think_validation_{feature_name}.md      # 思考过程：验证和测试点设计。
└── _constraints_{feature_name}.md            # (可选) 项目约束或特殊说明。
```

同时，该TDD周期对应的**代码快照**位于：
*   **源代码**: `{app_name}/src/{module_name}/{feature_name}.py` (例如 `ai_wellness_advisor/src/bmi/bmi_calculate.py`)
*   **特性代码说明**: `{app_name}/src/{module_name}/README_{feature_name}.md` (例如 `ai_wellness_advisor/src/bmi/README_bmi_calculate.md`)
*   **测试代码**: `{app_name}/tests/{module_name}/test_{feature_name}.py` (例如 `ai_wellness_advisor/tests/bmi/test_bmi_calculate.py`)

**请注意**：
- 高级用户故事（如本文档 `practice_tdd_bmi_calculator.md`）位于 `exercise_tdd_bmi/` 目录下，作为练习的起点。
- `_user_story_{feature_name}.md` 是在 `{app_name}/dev_cycles/...` 目录中对用户故事的详细阐述和演进记录。
- TDD开发周期中产生的代码 (`{feature_name}.py` 和 `test_{feature_name}.py`) 的快照版本直接位于 `{app_name}/src/{module_name}/` 和 `{app_name}/tests/{module_name}/` 下，而不是在 `dev_cycles` 目录的 `outputs` 子目录中。`dev_cycles` 目录专注于记录思考、设计和演进过程的文档。

## BMI计算器特定实现(两个Feature)

### 1. ExTDD_01_BMICalculation: 实现BMI值的计算

module_name: bmi
feature_name: bmi_calculate

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_01_BMICalculation/`

其内部结构遵循 [README_folder_feature.md](../README_folder_feature.md) 定义的规范，例如 (`{app_name}/dev_cycles/{module_name}/ExTDD_01_BMICalculation/`):
```
ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/
├── _user_story_bmi_calculate.md
├── _s1_think_options_bmi_calculate.md
├── _s2_think_design_bmi_calculate.md
├── _s3_think_validation_bmi_calculate.md
└── _constraints_bmi_calculate.md
```
对应的代码快照位于：
*   `../{app_name}/src/{module_name}/README_bmi_calculate.md`
*   `../{app_name}/src/{module_name}/bmi_calculate.py`
*   `../{app_name}/tests/{module_name}/test_bmi_calculate.py`

#### 核心用户故事 (ExTDD_01_BMICalculation) 针对Feature_01
> 作为一名普通用户，我希望能方便地输入我的身高（以米为单位）和体重（以千克为单位），然后系统能帮我算出我的身体质量指数（BMI）。如果我输错了数字（比如不是有效的身高体重值），希望能得到一个友好的提示。我最主要就是想知道计算出来的BMI结果。

### 2. ExTDD_02_BMICategorization: 实现BMI值的分类

module_name: bmi
feature_name: bmi_categorize

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_02_BMICategorization/`

其内部结构遵循 [README_folder_feature.md](../README_folder_feature.md) 定义的规范，例如 (`{app_name}/dev_cycles/{module_name}/ExTDD_02_BMICategorization/`):
```
ai_wellness_advisor/dev_cycles/bmi/ExTDD_02_BMICategorization/
├── _user_story_bmi_categorize.md
├── _s1_think_options_bmi_categorize.md
├── _s2_think_design_bmi_categorize.md
├── _s3_think_validation_bmi_categorize.md
└── _constraints_bmi_categorize.md
```
对应的代码快照位于：
*   `../{app_name}/src/{module_name}/README_bmi_categorize.md`
*   `../{app_name}/src/{module_name}/bmi_categorize.py`
*   `../{app_name}/tests/{module_name}/test_bmi_categorize.py`

#### 核心用户故事 (ExTDD_02_BMICategorization) 针对Feature_02
> 作为一名关心健康的用户，在我知道自己的BMI值之后，我还想知道这个数值到底代表什么意思，比如我是不是偏瘦了、体重是否标准，或者是不是有点超重。希望能给我一个简单明了的健康状况分类。

