# 项目整体目录结构

本文档定义了 `ai_dev_exercise_tdd` 项目（根目录）及其内部 `ai_wellness_advisor` 应用的目录结构和文件组织规范。

### 1. 根目录 (`ai_dev_exercise_tdd/`)

这是整个TDD练习项目的根目录。它包含了各个独立的TDD练习模块 (`exercise_tdd_xxx/`)、最终整合的AI健康助手应用 (`ai_wellness_advisor/`) 以及一些通用工具和文档。

*   **`README_folders.md`**: (本文档) 描述了整个项目的目录结构和文件组织规范。
*   **`README_prj.md`**: 项目的总体说明、目标、如何开始、贡献指南等。
*   **`exercise_tdd_xxx/`**: 包含各个具体TDD练习的目录，例如 `exercise_tdd_bmi/`, `exercise_tdd_dcnc/` 等。每个这样的目录都是一个独立的学习单元，包含练习说明、教学框架和可能的辅助材料。
*   **`ai_wellness_advisor/`**: 这是通过各个TDD练习逐步构建起来的最终AI健康助手应用程序。它有自己独立的源代码 (`src/`)、测试代码 (`tests/`)、文档 (`docs/`) 等。 **注意**：下面的项目结构图示例中，为了更清晰地展示 `ai_wellness_advisor` 内部结构，该图示的“根”实际是 `ai_wellness_advisor/` 目录，并非整个 `ai_dev_exercise_tdd/` 的根。但为了完整性，结构图的顶层已补充了实际根目录下的关键 `README` 文件。
*   **`utils_llm/`**: (可选) 如果项目中用到了大型语言模型 (LLM) 相关的通用工具，可以放在这里。
*   **`migration/`**: (可选) 如果项目涉及到从旧结构迁移到当前结构的计划和文档，可以放在这里。
*   `.gitignore`: 指定Git版本控制系统应忽略的文件和目录。
*   `.flake8` (或 `pyproject.toml` 中的 `tool.flake8`): Flake8代码风格检查工具的配置文件。

### 2. `ai_wellness_advisor/` 应用目录结构细节

(接下来的结构图主要展示 `ai_wellness_advisor/` 内部)

```
/  # Actual project root
├── README_folders.md # (This file)
├── README_prj.md     # (Overall project README)
├── .gitignore
├── requirements.txt  # 或者 pyproject.toml
├── ai_wellness_advisor/ # Application specific folder (see detailed structure below)
│   └── ...
├── exercise_tdd_xxx/ # TDD exercise folders
│   └── ...
├── utils_llm/        # Optional LLM utilities
│   └── ...
└── migration/        # Optional migration documents
    └── ...

# Detailed structure of `ai_wellness_advisor/`:
ai_wellness_advisor/
├── README.md         # README for ai_wellness_advisor application
├── src/                # (Source code) 所有Python模块源代码
│   ├── __init__.py
│   ├── bmi/            # (Module) BMI计算器模块 (第0层)
│   │   ├── __init__.py
│   │   └── bmi_calculator.py
│   ├── dcnc/           # (Module) DCNC模块 (第0层)
│   │   ├── __init__.py
│   │   └── dcnc_calculator.py
│   ├── pydantic_models/ # (Module) Pydantic模型 (第0层，或按需组织)
│   │   ├── __init__.py
│   │   └── user_profile_models.py # 示例
│   ├── core_services/  # (Module) 核心服务 (第1层和第2层)
│   │   ├── __init__.py
│   │   ├── wellness_profile_builder.py
│   │   └── personalized_advisor.py
│   └── main.py         # (Entry point) 应用主入口 (可选)
├── tests/              # (Tests) 所有Python测试代码
│   ├── __init__.py
│   ├── bmi/            # (Test Module) BMI计算器模块测试
│   │   ├── __init__.py
│   │   └── test_bmi_calculator.py
│   ├── dcnc/           # (Test Module) DCNC模块测试
│   │   ├── __init__.py
│   │   └── test_dcnc_calculator.py
│   ├── pydantic_models/ # (Test Module) Pydantic模型测试
│   │   ├── __init__.py
│   │   └── test_user_profile_models.py
│   ├── core_services/  # (Test Module) 核心服务测试
│   │   ├── __init__.py
│   │   ├── test_wellness_profile_builder.py
│   │   └── test_personalized_advisor.py
│   └── test_integration.py # (Integration Test) 集成测试 (可选)
├── docs/               # (Documentation) 项目级文档、架构图等
│   ├── architecture.md
│   ├── user_stories/   # (User Stories for TDD) TDD练习中各特性(feature)的用户故事/需求文档, 每个特性对应一个文件
│   │   ├── user_story_bmi_featureN.md
│   │   ├── user_story_dcnc_featureN.md
│   │   ├── user_story_pydantic_featureN.md
│   │   ├── user_story_llm_clients_featureN.md
│   │   └── user_story_core_services_featureN.md # 对应 exercise_ai_wellness_advisor
│   │
│   └── archived_tdd_cycles/ # (Archived TDD Cycles) TDD周期内的思考、设计和实现记录归档
│       ├── bmi/                            # (Archived TDD Cycles for BMI)
│       │   └── ExTDD_01_BMICalculation/    # (Example TDD Cycle, see structure above)
│       ├── dcnc/                           # (Archived TDD Cycles for DCNC)
│       │   └── ExTDD_XX_FeatureName/       # (Example TDD Cycle, see structure above)
│       ├── pydantic_models/                # (Archived TDD Cycles for Pydantic Models)
│       │   └── ExTDD_XX_FeatureName/       # (Example TDD Cycle, see structure above)
│       ├── llm_clients/                    # (Archived TDD Cycles for LLM Clients)
│       │   └── ExTDD_XX_FeatureName/       # (Example TDD Cycle, see structure above)
│       └── core_services/                  # (Archived TDD Cycles for Core Services)
│           ├── ExTDD_XX_FeatureName/       # (Example TDD Cycle, see structure above)
│           └── ExTDD_YY_AnotherFeature/    # (Example TDD Cycle, see structure above)
|
├── exercise_tdd_bmi/         # (TDD Exercise Entry) BMI计算器的TDD练习入口与指南
│   ├── practice_tdd_bmi_calculator.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_dcnc/        # (TDD Exercise Entry) DCNC的TDD练习入口与指南
│   ├── practice_dcnc_daily_caloric_needs_calculator.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_llm/         # (TDD Exercise Entry) LLM工具集的TDD练习入口与指南
│   ├── src/                    # (Source code) LLM相关模块源代码
│   ├── tests/                  # (Tests) LLM相关模块测试代码
│   ├── practice_tdd_llm_exercises.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_pydantic/    # (TDD Exercise Entry) Pydantic模型的TDD练习入口与指南
│   ├── practice_tdd_pydantic.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_ai_wellness_advisor/ # (TDD Exercise Entry) 核心服务层的TDD练习入口与指南 (第1、2层)
│   ├── practice_ai_wellness_advisor_core_services.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_template/    # (TDD Template) TDD练习模板
│   └── ...
├── migration/                # (Migration Documents) 迁移计划文档
│   ├── overall_plan.md
│   └── execution_plan.md
└── utils_llm/                # (LLM Utilities) LLM基础工具
    └── ...

# Reminder: The structure depicted above under `ai_wellness_advisor/` is nested within the `ai_dev_exercise_tdd/` root directory, which also contains `README_folders.md` (this file) and `README_prj.md`.

```

## 每个 ExTDD 练习的目录结构 (在 `ai_wellness_advisor/docs/archived_tdd_cycles/` 目录下)

每个TDD练习周期（例如，针对BMI模块的 `ExTDD_01_BMICalculation`）的产出物，将归档在 `ai_wellness_advisor/docs/archived_tdd_cycles/{module_name}/ExTDD_XX_{FeatureName}/` 目录下。其中 `{module_name}` 对应如 `bmi`, `dcnc` 等模块名。其内部结构和文件说明如下：

```
ai_wellness_advisor/docs/archived_tdd_cycles/exercise_name/ExTDD_XX_FeatureName/
├── constraints/                    # (Optional Constraints) 约束条件
│   └── {feature_name}_constraints.md # (Task Constraints) 记录当前TDD周期的特定约束和假设。
├── outputs/                       # (Outputs) TDD周期内的主要产出物
│   ├── _s1_think_options_{feature_name}.md  # 思考过程：方案选择与分析。
│   ├── _s2_think_design_{feature_name}.md   # 思考过程：详细设计。
│   ├── _s3_think_validation_{feature_name}.md # 思考过程：验证和测试点设计。
│   └── doc_{feature_name}.md         # (Optional) 特性相关的简要说明或API文档（如果适用）。
└── src/
|    └── bmi/
|        ├── __init__.py
|        └── bmi_calculator.py  # 或者 new_feature_for_bmi.py
└── tests/
    └── bmi/
        ├── __init__.py
        └── test_bmi_calculator.py # 或者 test_new_feature_for_bmi.py
```

**核心原则**：
- `outputs/` 目录中的 `.md` 文件（如 `_s1_think_...`）是TDD思考过程的永久记录。
- `outputs/` 目录不再用于存放TDD周期中产生的 `{feature_name}.py` 和 `test_{feature_name}.py` 代码文件。这些代码的开发和版本控制应直接在 `ai_wellness_advisor/src/...` 和 `ai_wellness_advisor/tests/...` 的目标位置进行，或遵循更新后的项目开发流程。

**重要原则与文件定位指南:**

为确保项目结构的清晰与一致性，各类文件和文档的存放位置遵循以下核心原则：

1.  **`ai_wellness_advisor/`：应用核心**
    *   作为实际构建的应用程序，是所有最终生产代码 (`src/`)、最终测试代码 (`tests/`)、权威用户故事 (`docs/user_stories/`) 及项目与模块文档 (`README.md`, `docs/architecture.md` 等) 的唯一存放地。

2.  **`exercise_tdd_xxx/`：TDD练习指南**
    *   扮演TDD练习的“静态入口点”角色，提供高级别初始用户故事 (`practice_xxx.md`) 和教学框架 (`teaching_framework/`)。
    *   `practice_xxx.md` 可链接至 `ai_wellness_advisor/docs/user_stories/` 中的详细需求。
    *   **严禁** 在此存放任何实际Python源代码、测试脚本或重复的详细设计文档；这些动态内容均属 `ai_wellness_advisor/`。

3.  **`ai_wellness_advisor/docs/archived_tdd_cycles/`：TDD过程归档**
    *   用于归档每个TDD练习周期 (`.../{module_name}/ExTDD_XX_{FeatureName}/`) 的完整记录，包括：
        *   思考过程与约束分析：`outputs/` 子目录下的 `.md` 文件。
        *   迭代代码与测试快照：该练习归档目录下的 `src/` 和 `tests/` 子目录。
        *   周期性总结：可能包含的 `README.md`。
    *   此归档主要服务于过程追溯与复盘，其代码快照的最终稳定版本须整合进 `ai_wellness_advisor/src/` 和 `ai_wellness_advisor/tests/`。

**总结速查表:**

| 文件类型             | 主要存放位置                                                                 | 说明                                                                                                |
| -------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **启动TDD的练习** | `exercise_tdd_xxx/practice_yyy.md`                                              | 高级别、练习入口                                                                                            |
| **用户故事(按Feature)**     | `ai_wellness_advisor/docs/user_stories/user_story_{PracticeName}_{FeatureName}.md`                                     | 模块化、权威版本                                                                                        |
| **TDD过程文档**      | `ai_wellness_advisor/docs/archived_tdd_cycles/.../ExTDD_XX_FeatureName/`     | 包含思考、约束、迭代代码/测试、周期总结  
| **最终功能代码**     | `ai_wellness_advisor/src/...`                                                   | 功能代码                                                                                          |
| **最终测试代码**     | `ai_wellness_advisor/tests/...`                                                 | 测试代码                                                                                          |
| **模块文档** | `ai_wellness_advisor/docs/...`                                   | 项目概述、架构、详细设计, user_story, feature文档等                                                                                |

简而言之：`exercise_tdd_xxx/` 目录是“静态的地图和指南”，而 `ai_wellness_advisor/` 是“动态的城市本身”，其 `docs/archived_tdd_cycles/` 则记录了“城市的建设蓝图和过程”。