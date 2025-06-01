# 项目整体目录结构

本文档定义了 `ai_wellness_advisor` 项目及其在整体项目中的位置和结构。

## `ai_wellness_advisor` 项目目录结构

```
ai_wellness_advisor/
├── .gitignore
├── README.md
├── requirements.txt  # 或者 pyproject.toml
├── src/                # 所有Python模块源代码
│   ├── __init__.py
│   ├── bmi/            # BMI计算器模块 (第0层)
│   │   ├── __init__.py
│   │   └── calculator.py
│   ├── dcnc/           # DCNC模块 (第0层)
│   │   ├── __init__.py
│   │   └── calculator.py
│   ├── pydantic_models/ # Pydantic模型 (第0层，或按需组织)
│   │   ├── __init__.py
│   │   └── user_profile_models.py # 示例
│   ├── core_services/  # 核心服务 (第1层和第2层)
│   │   ├── __init__.py
│   │   ├── wellness_profile_builder.py
│   │   └── personalized_advisor.py
│   └── main.py         # 应用主入口 (可选)
├── tests/              # 所有Python测试代码
│   ├── __init__.py
│   ├── bmi/
│   │   ├── __init__.py
│   │   └── test_calculator.py
│   ├── dcnc/
│   │   ├── __init__.py
│   │   └── test_calculator.py
│   ├── pydantic_models/
│   │   ├── __init__.py
│   │   └── test_user_profile_models.py
│   ├── core_services/
│   │   ├── __init__.py
│   │   ├── test_wellness_profile_builder.py
│   │   └── test_personalized_advisor.py
│   └── test_integration.py # 集成测试 (可选)
├── docs/               # 项目级文档、架构图等
│   ├── architecture.md
│   ├── user_stories/   # 所有模块的用户故事/需求文档
│   │   ├── bmi_story.md
│   │   ├── dcnc_story.md
│   │   ├── pydantic_story.md
│   │   ├── llm_clients_story.md
│   │   └── core_services_story.md # 对应 exercise_ai_wellness_advisor
│   └── tdd_process_archive/ # TDD过程中的思考和设计文档归档
│       ├── bmi/
│       │   └── ExTDD_01_BMICalculator/
│       ├── dcnc/
│       │   └── ExTDD_01_CalculateBMR/
│       └── core_services/
│           ├── ExTDD_01_WellnessProfileBuilder/
│           └── ExTDD_02_PersonalizedAdvisor/
└── scripts/            # 辅助脚本 (例如：数据迁移、部署脚本等，可选)

```

## 整体项目顶级目录结构概览 (`/Users/bowhead/ai_dev_exercise_tdd/`)

```
/Users/bowhead/ai_dev_exercise_tdd/
├── ai_wellness_advisor/      # 新的统一应用项目 (如上文详细结构所示)
│   ├── .gitignore
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   ├── tests/
│   └── docs/
├── exercise_tdd_bmi/         # BMI计算器的TDD练习入口与指南
│   ├── story_tdd_bmi_calculator.md
│   └── teaching_framework/
├── exercise_tdd_dcnc/        # DCNC的TDD练习入口与指南
│   ├── story_dcnc_daily_caloric_needs_calculator.md
│   └── teaching_framework/
├── exercise_tdd_llm/         # LLM工具集的TDD练习入口与指南
│   ├── story_tdd_llm_exercises.md
│   └── teaching_framework/
├── exercise_tdd_pydantic/    # Pydantic模型的TDD练习入口与指南
│   ├── story_tdd_pydantic.md
│   └── teaching_framework/
├── exercise_ai_wellness_advisor/ # 核心服务层的TDD练习入口与指南 (第1、2层)
│   ├── story_ai_wellness_advisor_core_services.md
│   └── teaching_framework/
├── exercise_tdd_template/    # TDD练习模板
│   └── ...
├── migration/                # 迁移计划文档
│   ├── overall_plan.md
│   ├── execution_plan.md
│   └── overall_folder_structure.md # 本文档
└── utils_llm/                # LLM基础工具
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