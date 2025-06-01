# 项目整体目录结构

本文档定义了 `ai_wellness_advisor` 项目及其在整体项目中的位置和结构。

### 项目整体目录结构的细节

```
ai_wellness_advisor/
├── .gitignore
├── README.md
├── requirements.txt  # 或者 pyproject.toml
├── src/                # (Source code) 所有Python模块源代码
│   ├── __init__.py
│   ├── bmi/            # (Test Module) BMI计算器模块测试            # (Module) BMI计算器模块 (第0层)
│   │   ├── __init__.py
│   │   └── bmi_calculator.py
│   ├── dcnc/           # (Test Module) DCNC模块测试           # (Module) DCNC模块 (第0层)
│   │   ├── __init__.py
│   │   └── dcnc_calculator.py
│   ├── pydantic_models/ # (Test Module) Pydantic模型测试 # (Module) Pydantic模型 (第0层，或按需组织)
│   │   ├── __init__.py
│   │   └── user_profile_models.py # 示例
│   ├── core_services/  # (Test Module) 核心服务测试  # (Module) 核心服务 (第1层和第2层)
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
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架   # (Teaching Framework) 通用TDD教学框架
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
│   └── oexecution_plan.md
└── utils_llm/                # (LLM Utilities) LLM基础工具
    └── ...

```

## 每个 ExTDD 练习的目录结构 (在 archived_tdd_cycles 目录下)

每个TDD练习周期（例如 `ExTDD_01_BMICalculation`）的产出物，将归档在 `ai_wellness_advisor/docs/archived_tdd_cycles/exercise_name/ExTDD_XX_FeatureName/` 目录下。其内部结构和文件说明如下：

```
ai_wellness_advisor/docs/archived_tdd_cycles/exercise_name/ExTDD_XX_FeatureName/
├── constraints/                    # (Constraints) 约束条件
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

为了确保项目结构的清晰和一致性，以下原则明确了各类文件和文档的存放位置：

1.  **`ai_wellness_advisor/` 项目核心地位:**
    *   此目录是我们构建的 **实际应用程序** 的唯一、权威存放地。
    *   **最终生产代码**：位于 `ai_wellness_advisor/src/` 下的相应模块中。
    *   **最终测试代码**：位于 `ai_wellness_advisor/tests/` 下的相应模块中。
    *   **最终用户故事/需求文档**：针对各模块的权威用户故事和需求文档，统一存放在 `ai_wellness_advisor/docs/user_stories/`。
    *   **最终项目与模块文档**：包括项目整体 `README.md`、架构文档 (`ai_wellness_advisor/docs/architecture.md`) 以及各模块的详细设计文档等，均位于 `ai_wellness_advisor/` 或其 `docs/` 子目录内。

2.  **`exercise_tdd_xxx/` 目录角色 (TDD练习入口与指南):**
    *   这些目录严格作为TDD练习的 **“控制器”或“入口点”（静态指南）**。
    *   **高级别用户故事 (练习起点)**：每个 `exercise_tdd_xxx/` 目录下包含一个 `practice_xxx.md` 文件。此文件作为启动和指导对应TDD练习的 **高级别、初始用户故事**。它应简明扼要，并可链接到 `ai_wellness_advisor/docs/user_stories/` 中更详细的、作为最终版本参考的对应模块用户故事。
    *   **教学材料**：包含通用的TDD教学框架文档 (`teaching_framework/`)。
    *   **引用链接**：可能包含指向 `ai_wellness_advisor/` 内部对应模块最终代码、测试和详细文档的明确引用或链接，以引导开发者查阅最终实现。
    *   **禁止存放实际代码/测试**：这些目录 **绝不包含任何实际的Python源代码、测试脚本或重复的详细设计文档**。所有这些动态的、演进的内容都必须位于 `ai_wellness_advisor/` 项目中。

3.  **TDD过程文档 (周期性产出物归档):**
    *   **位置**：所有TDD练习周期中的详细思考过程、约束分析、迭代代码、迭代测试和周期性总结（README）等，统一归档在 `ai_wellness_advisor/docs/archived_tdd_cycles/exercise_name/ExTDD_XX_FeatureName/` 目录下。
    *   **内容**：具体结构请参见上一节“每个 ExTDD 练习的目录结构 (在 archived_tdd_cycles 目录下)”的详细说明。其中 `outputs/` 目录下的 `.py` 文件是TDD过程中的代码快照，用于记录迭代，其稳定版本必须整合到 `ai_wellness_advisor/src/` 和 `ai_wellness_advisor/tests/`。
    *   **目的**：此归档的主要目的是为了追溯和复盘TDD的完整过程，而非作为最终代码的部署或引用源。

**总结速查表:**

| 文件类型             | 主要存放位置                                                                 | 说明                                                                                                |
| -------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **启动TDD的练习** | `exercise_tdd_xxx/practice_xxx.md`                                              | 高级别、练习入口                                                                                        |
| **用户故事(按Feature)**     | `ai_wellness_advisor/docs/user_stories/user_story_{PracticeName}_{FeatureName}.md`                                     | 模块化、权威版本                                                                                        |
| **TDD过程文档**      | `ai_wellness_advisor/docs/archived_tdd_cycles/.../ExTDD_XX_FeatureName/`     | 包含思考、约束、迭代代码/测试、周期总结  
| **最终功能代码**     | `ai_wellness_advisor/src/`                                                   | 生产环境代码                                                                                          |
| **最终测试代码**     | `ai_wellness_advisor/tests/`                                                 | 生产环境测试                                                                                          |
                                                                   |
| **最终项目/模块文档** | `ai_wellness_advisor/ (README.md, docs/*)`                                   | 项目概述、架构、详细设计等                                                                                |

简而言之：`exercise_tdd_xxx/` 目录是“静态的地图和指南”，而 `ai_wellness_advisor/` 是“动态的城市本身”，其 `docs/archived_tdd_cycles/` 则记录了“城市的建设蓝图和过程”。