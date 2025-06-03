# AI 辅助测试驱动开发 (AI-Assisted Test-Driven Development) 实践项目

## 项目简介

本项目旨在提供一个全面的实践框架，用于探索和掌握 AI 辅助下的测试驱动开发 (TDD) 流程。通过一系列精心设计的练习，您将学习如何利用 AI 工具（如 Cursor）来辅助 TDD 的各个阶段，包括需求分析、设计、编码、测试和重构。项目结构清晰，遵循严格的命名和目录规范，旨在提升开发效率、代码质量和可维护性。

## 核心理念与目标

*   **AI 赋能 TDD**：探索 AI 在 TDD 流程中的应用，例如辅助生成测试用例、代码实现、重构建议等。
*   **实践驱动学习**：通过实际的编码练习，深入理解 TDD 的核心原则和实践方法。
*   **规范化开发**：遵循统一的目录结构、命名约定和开发流程，培养良好的工程实践习惯。
*   **模块化与可扩展性**：设计灵活的练习框架，方便添加新的练习模块和功能。

## 项目结构概览

本项目的目录结构经过精心设计，旨在清晰地组织不同类型的资产，并支持 AI 辅助开发流程。以下是核心目录及其功能概览：

```
ai_wellness_advisor/      # 示例应用，用于实践 TDD
├── README_awa.md         # AI Wellness Advisor 应用说明
├── __init__.py
├── dev_cycles/           # 开发周期记录：存放每个特性或模块的 TDD 开发过程文档
│   ├── bmi/
│   ├── data_models/
│   ├── dcnc/
│   └── llm_integration/
├── src/                  # 源代码：存放所有应用程序的实现代码
│   ├── __init__.py
│   ├── bmi/
│   ├── data_models/
│   ├── dcnc/
│   └── llm_integration/
└── tests/                # 测试代码：存放所有单元测试、集成测试等
    ├── __init__.py
    ├── bmi/
    ├── data_models/
    ├── dcnc/
    └── llm_integration/
exercise_tdd_awa_core/    # TDD 练习模块：AI 健康顾问核心组件
└── practice_awa_core_components.md
exercise_tdd_bmi/         # TDD 练习模块：BMI 计算器
└── practice_tdd_bmi_calculator.md
exercise_tdd_dcnc/        # TDD 练习模块：日常卡路里需求计算器
└── practice_dcnc_daily_caloric_needs_calculator.md
exercise_tdd_llm/         # TDD 练习模块：LLM 集成
└── practice_tdd_llm_exercises.md
exercise_tdd_pydantic/    # TDD 练习模块：Pydantic 数据模型实践
└── practice_tdd_pydantic.md
tdd_exercise_factory/     # TDD 练习工厂：生成和修改 TDD 练习的工具和说明
├── generate_tdd_exercise_instructions.md
├── modify_tdd_exercise_instructions.md
└── practice_tdd_template.md
tdd_rules/                # TDD 规则与规范：TDD 核心理念、单元测试设计技巧等指导文档
├── planning_tdd_exercise.md
├── tdd_ai_thinking.md
├── tdd_core_loop_steps.md
└── tdd_unit_test_design_techniques.md
utils_llm/                # LLM 相关工具

README.md                 # 项目主 README (当前文件)
README_folder_feature.md  # ExTDD 特性研发目录结构核心原则与详解
README_folders.md         # 项目整体目录结构定义
README_prj.md             # 项目层面的通用 README
pytest.ini                # Pytest 配置文件
requirements.txt          # 项目依赖
```

**核心目录说明**：
*   `ai_wellness_advisor/`：一个示例应用，用于实践 TDD。其内部的 `dev_cycles`、`src` 和 `tests` 子目录分别用于记录开发过程、存放源代码和测试代码。
    *   `dev_cycles/`：**开发周期记录**。此目录是 AI 理解开发上下文和进行辅助的关键，用于存放每个特性或模块的 TDD 开发过程文档，包括用户故事、设计思考、决策记录等。
    *   `src/`：**源代码**。存放所有应用程序的实现代码。
    *   `tests/`：**测试代码**。存放所有单元测试、集成测试等。
*   `exercise_tdd_*/`：**TDD 练习模块**。每个子目录代表一个独立的 TDD 练习，例如 `exercise_tdd_bmi` 用于 BMI 计算器练习，`exercise_tdd_pydantic` 用于 Pydantic 数据模型练习。每个练习都包含其特定的 `practice_*.md` 文件，作为练习的起点和高级别需求描述。
*   `tdd_exercise_factory/`：**TDD 练习工厂**。包含用于生成和修改 TDD 练习的工具和说明文档，例如 `generate_tdd_exercise_instructions.md` 和 `modify_tdd_exercise_instructions.md`。
*   `tdd_rules/`：**TDD 规则与规范**。存放关于 TDD 核心理念、单元测试设计技巧、练习框架规划等指导性文档。
*   `README_folder_feature.md`：详细阐述了 **ExTDD 特性研发目录结构的核心原则与详解**，是理解 `dev_cycles`, `src`, `tests` 中各产出物组织方式的关键文档。
*   `README_folders.md`：定义了 **项目整体目录结构**，包括项目根目录及 `{app_name}` 应用的整体结构。
*   `README_prj.md`：项目层面的通用 README，提供了项目概览和基本信息。

## 命名约定与规范

为了保持项目的一致性和可维护性，本项目遵循以下核心命名原则：

### 1. 特性名称 (feature_name)

*   **格式**：通常采用 `小写字母_用下划线分隔` 的形式，例如 `bmi_calculator`, `daily_caloric_needs_calculator`, `llm_integration`。
*   **要求**：描述性强、简洁，能清晰表达特性功能。

### 2. 模块名称 (module_name)

*   **格式**：通常采用 `小写字母_用下划线分隔` 的形式，例如 `health_metrics`, `data_models`, `llm_utils`。
*   **要求**：反映模块的职责或包含的功能集合。

### 3. 文件命名

*   **源代码**：`{feature_name}.py` (例如 `bmi_calculator.py`)。
*   **测试代码**：`test_{feature_name}.py` (例如 `test_bmi_calculator.py`)。
*   **特性代码说明**：`README_{feature_name}.md` (例如 `README_bmi_calculator.md`)。
*   **用户故事文档**：`_user_story_{feature_name}.md`。
*   **思考与设计文档**：`_s1_think_options_{feature_name}.md`, `_s2_think_design_{feature_name}.md`, `_s3_think_validation_{feature_name}.md` 等。

### 4. 目录命名

*   **开发周期目录**：`ExTDD_NN_{FeatureName}` (例如 `ExTDD_01_BMICalculator`)，其中 `NN` 是两位数字序号，`FeatureName` 是特性名称的驼峰命名。

## TDD 练习流程与指导

每个 TDD 练习都旨在引导您完成一个完整的开发周期。以下是通用的练习流程和关键指导：

### 1. 理解用户故事与功能需求

每个练习的 `practice_*.md` 文件（例如 `practice_tdd_bmi_calculator.md`）提供了高级别的用户故事和功能需求。请仔细阅读并理解。

### 2. 启动 TDD 周期

*   **创建开发周期目录**：在 `ai_wellness_advisor/dev_cycles/{module_name}/` 下创建 `ExTDD_NN_{FeatureName}/` 目录。
*   **创建用户故事文档**：在该目录下创建 `_user_story_{feature_name}.md`，并根据 `practice_*.md` 中的原始用户故事进行细化和演进。
*   **创建思考文档**：按照规范创建 `_s1_think_options_{feature_name}.md`, `_s2_think_design_{feature_name}.md`, `_s3_think_validation_{feature_name}.md` 等，记录您的设计思考、备选方案和验证过程。**强烈建议在每个 TDD 周期中按规范创建这些文档，以完整体现思考和决策过程。**

### 3. TDD 核心循环 (红-绿-重构)

*   **红 (Red)**：编写一个失败的测试用例。这个测试应该基于当前用户故事的最小可验证功能点。
    *   测试文件路径：`ai_wellness_advisor/tests/{module_name}/test_{feature_name}.py`
*   **绿 (Green)**：编写最少量的代码，使测试通过。不要过度设计，只关注通过当前测试。
    *   源代码文件路径：`ai_wellness_advisor/src/{module_name}/{feature_name}.py`
*   **重构 (Refactor)**：优化代码结构、消除重复、提高可读性，同时确保所有测试仍然通过。

### 4. 迭代与推进

重复 TDD 核心循环，逐步实现所有功能需求。在每个小步中，确保代码始终处于可工作状态，并通过测试验证。

### 5. 归档与总结

完成特性开发后，确保所有开发周期文档、源代码和测试代码都已按照项目规范归档。

## 练习模块示例

### 1. BMI 计算器 (exercise_tdd_bmi)

*   **目标**：实现一个 BMI（身体质量指数）计算器，并遵循 TDD 流程。
*   **核心功能**：根据身高和体重计算 BMI 值，并提供健康评估。
*   **相关文件**：`exercise_tdd_bmi/practice_tdd_bmi_calculator.md`

### 2. 日常卡路里需求计算器 (exercise_tdd_dcnc)

*   **目标**：实现一个日常卡路里需求计算器，考虑年龄、性别、活动水平等因素。
*   **核心功能**：计算基础代谢率 (BMR) 和总日常能量消耗 (TDEE)。
*   **相关文件**：`exercise_tdd_dcnc/practice_dcnc_daily_caloric_needs_calculator.md`

### 3. AI 健康顾问核心组件 (exercise_tdd_awa_core)

*   **目标**：开发 AI 健康顾问应用的核心组件，例如用户数据管理、健康指标追踪等。
*   **核心功能**：构建应用的基础架构和通用模块。
*   **相关文件**：`exercise_tdd_awa_core/practice_awa_core_components.md`

### 4. LLM 集成练习 (exercise_tdd_llm)

*   **目标**：探索如何将大型语言模型 (LLM) 集成到应用中，并进行 TDD 实践。
*   **核心功能**：例如，LLM 辅助健康建议生成、自然语言交互等。
*   **相关文件**：`exercise_tdd_llm/practice_tdd_llm_exercises.md`

### 5. Pydantic 数据模型实践 (exercise_tdd_pydantic)

*   **目标**：使用 Pydantic 定义和验证系统中的核心数据模型，如用户健康档案、饮食记录、运动计划等。
*   **核心功能**：确保数据的准确性、一致性和可靠性，提升系统的稳定性和开发效率。
*   **相关文件**：`exercise_tdd_pydantic/practice_tdd_pydantic.md`

## 如何开始

1.  **克隆项目**：
    ```bash
    git clone <项目仓库地址>
    cd ai_dev_exercise_tdd
    ```
2.  **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```
    (如果 `requirements.txt` 不存在，请根据具体练习的 `pyproject.toml` 或 `setup.py` 安装依赖)
3.  **选择一个练习**：进入 `exercise_tdd_*/` 目录，阅读 `practice_*.md` 文件，开始您的 TDD 实践之旅。
4.  **使用 AI 辅助**：在您的 IDE (如 Cursor) 中，利用 AI 功能辅助您完成 TDD 的各个阶段。

## AI Wellness Advisor 应用的启动和使用说明

### 完全从头开始

如果您希望完全从头开始构建此应用，可以删除以下目录：

*   `dev_cycles`
*   `src`
*   `tests`

删除这些目录后，整个项目将归零，您可以从头开始进行开发。

### 模块级别从头开始

如果您只想从头开始开发某个模块，可以删除 `dev_cycles`、`src` 和 `tests` 目录下对应模块的目录。例如，要从头开始开发 BMI 模块，您可以删除以下目录：

*   `dev_cycles/bmi`
*   `src/bmi`
*   `tests/bmi`

删除这些目录后，BMI 模块将从头开始，而其他模块不受影响。

