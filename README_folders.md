# 项目整体目录结构

本文档定义了 `ai_wellness_advisor` 项目及其在整体项目中的位置和结构。

## `ai_wellness_advisor` 项目目录结构

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
│   ├── user_stories/   # (User Stories) 所有模块的用户故事/需求文档
│   │   ├── bmi_story.md
│   │   ├── dcnc_story.md
│   │   ├── pydantic_story.md
│   │   ├── llm_clients_story.md
│   │   └── core_services_story.md # 对应 exercise_ai_wellness_advisor
│   └── tdd_process_archive/ # (TDD Archive) TDD过程中的思考和设计文档归档
│       ├── bmi/                            # (TDD Archive for BMI)
│       │   └── ExTDD_XX_FeatureName/       # (Example: ExTDD_01_BMICalculation)
│       ├── dcnc/                           # (TDD Archive for DCNC)
│       │   └── ExTDD_XX_FeatureName/       # (Example: ExTDD_01_CalculateBMR)
│       ├── pydantic_models/                # (TDD Archive for Pydantic Models)
│       │   └── ExTDD_XX_FeatureName/       # (Example: ExTDD_01_UserProfileValidation)
│       ├── llm_clients/                    # (TDD Archive for LLM Clients)
│       │   └── ExTDD_XX_FeatureName/       # (Example: ExTDD_01_BasicChat)
│       └── core_services/                  # (TDD Archive for Core Services)
│           ├── ExTDD_XX_FeatureName/       # (Example: ExTDD_01_WellnessProfileBuilder)
│           └── ExTDD_YY_AnotherFeature/    # (Example: ExTDD_02_PersonalizedAdvisor)
└── scripts/            # (Scripts) 辅助脚本 (例如：数据迁移、部署脚本等，可选)

```

## 整体项目顶级目录结构概览 (`/Users/bowhead/ai_dev_exercise_tdd/`)

```
/Users/bowhead/ai_dev_exercise_tdd/
├── ai_wellness_advisor/      # (Application) 新的统一应用项目 (如上文详细结构所示)
│   ├── .gitignore
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   ├── tests/
│   └── docs/
├── exercise_tdd_bmi/         # (TDD Exercise Entry) BMI计算器的TDD练习入口与指南
│   ├── story_tdd_bmi_calculator.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_dcnc/        # (TDD Exercise Entry) DCNC的TDD练习入口与指南
│   ├── story_dcnc_daily_caloric_needs_calculator.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_llm/         # (TDD Exercise Entry) LLM工具集的TDD练习入口与指南
│   ├── src/                    # (Source code) LLM相关模块源代码
│   ├── tests/                  # (Tests) LLM相关模块测试代码
│   ├── story_tdd_llm_exercises.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_pydantic/    # (TDD Exercise Entry) Pydantic模型的TDD练习入口与指南
│   ├── story_tdd_pydantic.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_ai_wellness_advisor/ # (TDD Exercise Entry) 核心服务层的TDD练习入口与指南 (第1、2层)
│   ├── story_ai_wellness_advisor_core_services.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_template/    # (TDD Template) TDD练习模板
│   └── ...
├── migration/                # (Migration Documents) 迁移计划文档
│   ├── overall_plan.md
│   ├── execution_plan.md
│   └── overall_folder_structure.md # (This Document) 本文档
└── utils_llm/                # (LLM Utilities) LLM基础工具
    └── ...
```

**重要原则再次强调:**
*   **`ai_wellness_advisor/` 是我们构建的实际应用程序，是所有生产代码、测试代码、最终用户故事、详细设计文档和配置文件的唯一、权威存放地。**
*   **所有 `exercise_tdd_xxx/` 和 `exercise_ai_wellness_advisor/` 目录严格作为TDD练习的“控制器”或“入口点”（静态指南）。** 它们内部主要包含：
    *   高级别的用户故事 (`story_xxx.md`)，用于启动和指导TDD练习。
    *   指向 `ai_wellness_advisor/` 内部对应模块代码、测试和详细文档的明确引用或链接。
    *   通用的TDD教学材料 (`teaching_framework/`)。
    *   **绝不包含任何实际的Python源代码、测试脚本或重复的详细设计文档。** 所有这些动态的、演进的内容都必须位于 `ai_wellness_advisor/` 项目中。
*   简而言之：`exercise_xxx` 目录是“静态的地图和指南”，而 `ai_wellness_advisor` 是“动态的城市本身”。