# 项目整体目录结构

本文档定义了 `ai_dev_exercise_tdd` 项目（根目录）及其内部 `ai_wellness_advisor` 应用的目录结构和文件组织规范。

## 根目录 

根目录就是项目根目录, README_prj.md 和READ_folders.md, 和 .env所在的目录.

这是整个TDD练习项目的根目录。它包含了各个独立的TDD练习模块 (`exercise_tdd_xxx/`)、最终整合的AI健康助手应用 (`ai_wellness_advisor/`) 以及一些通用工具和文档。

*   **`README_folders.md`**: (本文档) 描述了整个项目的目录结构和文件组织规范。
*   **`README_prj.md`**: 项目的总体说明、目标、如何开始、贡献指南等。
*   **`exercise_tdd_xxx/`**: 包含各个具体TDD练习的目录，例如 `exercise_tdd_bmi/`, `exercise_tdd_dcnc/` 等。每个这样的目录都是一个独立的学习单元，包含练习说明、教学框架和可能的辅助材料。
*   **`ai_wellness_advisor/`**: 这是通过各个TDD练习逐步构建起来的最终AI健康助手应用程序。它有自己独立的源代码 (`src/`)、测试代码 (`tests/`)、文档 (`docs/`) 等。 **注意**：下面的项目结构图示例中，为了更清晰地展示 `ai_wellness_advisor` 内部结构，该图示的“根”实际是 `ai_wellness_advisor/` 目录，并非整个 `ai_dev_exercise_tdd/` 的根。但为了完整性，结构图的顶层已补充了实际根目录下的关键 `README` 文件。
*   **`utils_llm/`**: (可选) 如果项目中用到了大型语言模型 (LLM) 相关的通用工具，可以放在这里。
*   `.gitignore`: 指定Git版本控制系统应忽略的文件和目录。
*   `.flake8` (或 `pyproject.toml` 中的 `tool.flake8`): Flake8代码风格检查工具的配置文件。

### 1. 根目录结构
(下面的结构图主要展示 `/` 整个根目录)

```
# Actual project root directory:
/  
├── README_folders.md # (This file)
├── README_prj.md     # (Overall project README)
├── .env              # 环境变量配置文件
├── .gitignore        # Git忽略文件
├── requirements.txt  # Python依赖管理
├── ai_wellness_advisor/ # Application specific folder (see detailed structure below)
│   └── ...
├── exercise_tdd_xxx/ # TDD exercise folders
│   └── ...
└── utils_llm/        # Optional LLM utilities
    └── ...
```

### 2. `ai_wellness_advisor/` 应用目录结构细节, 位于根目录下
(接下来的结构图主要展示 `ai_wellness_advisor/` 内部)

```
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
│   └── module_feature_overview.md # (Example: Overview of module and feature organization)
│   
├── dev_cycles/ #  TDD周期内的思考、设计和实现记录 (详细内部结构请参考 `./README_folder_feature.md`)
│   ├── {module_name}/             # 例如: bmi/, dcnc/, core_services/
│   │   └── ExTDD_NN_{feature_name}/   # 例如: ExTDD_01_BMICalculation/, ExTDD_02_DCNCCalculation/
│   │       ├── _user_story_{feature_name}.md
│   │       ├── _s1_think_options_{feature_name}.md
│   │       ├── _s2_think_design_{feature_name}.md
│   │       ├── _s3_think_validation_{feature_name}.md
│   │       └── _constraints_{feature_name}.md # (可选)
│   └── ...    # 其他模块的TDD周期记录以此类推
```

### 3. 各`exercise_tdd_xxx/`练习目录概览
(这些目录位于项目根目录下，提供各TDD练习的入口和教学材料)

```
/
├── exercise_tdd_bmi/         # (TDD Exercise Entry) BMI计算器的TDD练习入口与指南
│   ├── practice_tdd_bmi_calculator.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_dcnc/        # (TDD Exercise Entry) DCNC的TDD练习入口与指南
│   ├── practice_dcnc_daily_caloric_needs_calculator.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_llm/         # (TDD Exercise Entry) LLM工具集的TDD练习入口与指南
│   ├── practice_tdd_llm_exercises.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_tdd_pydantic/    # (TDD Exercise Entry) Pydantic模型的TDD练习入口与指南
│   ├── practice_tdd_pydantic.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── exercise_ai_wellness_advisor/ # (TDD Exercise Entry) 核心服务层的TDD练习入口与指南 (第1、2层)
│   ├── practice_ai_wellness_advisor_core_services.md
│   └── teaching_framework/   # (Teaching Framework) 通用TDD教学框架
├── factory_exercise_tdd/     # (TDD Exercise Template) TDD练习模板
│   └── ...
# ... 其他 exercise_tdd_xxx 目录以此类推
```

**Reminder**: The `exercise_tdd_xxx` directories are at the root level, alongside `ai_wellness_advisor/`. The main application code and its TDD cycle documents reside within `ai_wellness_advisor/` as detailed in section 2 and `README_folder_feature.md`.


#### 每个 ExTDD 练习的目录结构 (针对 feature的详尽说明, 核心思想)

关于每个特性（Feature）的TDD练习周期（包含源代码、测试代码、开发周期记录）的目录结构和文件命名规范的核心思想，请参考：[./README_folder_feature.md](./README_folder_feature.md)


**重要原则与文件定位指南:**

为确保项目结构的清晰与一致性，各类文件和文档的存放位置遵循以下核心原则：

1.  **`ai_wellness_advisor/`：应用核心**
    *   作为实际构建的应用程序，是所有最终生产代码 (`src/`)、最终测试代码 (`tests/`)、以及项目与模块级文档 (`README.md`, `docs/architecture.md` 等) 的主要存放地。权威的用户故事和详细的TDD开发周期文档位于其下的 `dev_cycles/` 目录中，具体结构遵循 `README_folder_feature.md`。

2.  **`exercise_tdd_xxx/`：TDD练习指南**
    *   扮演TDD练习的“静态入口点”角色，提供高级别初始用户故事 (`practice_xxx.md`) 和教学框架 (`teaching_framework/`)。
    *   `practice_xxx.md` 中的高级别用户故事，其详细阐述和演进记录在 `ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_NN_{feature_name}/_user_story_{feature_name}.md` 中。
    *   **严禁** 在此存放任何实际Python源代码、测试脚本或重复的详细设计文档；这些动态内容均属 `ai_wellness_advisor/`。

3.  **`ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_NN_{feature_name}/`：TDD过程记录**
    *   在 `ai_wellness_advisor` 应用的 `dev_cycles` 目录下，会按照模块名 (`{module_name}`) 和特性 (`ExTDD_NN_{feature_name}`) 进一步组织各个TDD练习周期的详细记录文档。
    *   这些文档记录了思考过程、约束分析、代码迭代和测试演进，遵循 `README_folder_feature.md` 中定义的命名和组织规范。
    *   其对应的源代码和测试代码快照也遵循 `README_folder_feature.md` 中定义的结构，位于 `ai_wellness_advisor/src/{module_name}/` 和 `ai_wellness_advisor/tests/{module_name}/` 下（在特性开发过程中，这些可能是临时的快照，最终稳定版会整合）。

## 总结速查表

| 文件类型             | 主要存放位置                                                                 | 说明                                                                                                |
| -------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **启动TDD的练习** | `exercise_tdd_xxx/practice_yyy.md`                                              | 高级别、练习入口, 里面指定了模块名 {module_name}                                                                                            |
| **TDD开发周期文档** | `ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_NN_{feature_name}/`                               | 包含用户故事、思考、设计、验证等特性开发全过程的文档，遵循 `README_folder_feature.md` 规范。 |
| **最终功能代码**     | `ai_wellness_advisor/src/{module_name}/...`                                                   | 功能代码                                                                                          |
| **最终测试代码**     | `ai_wellness_advisor/tests/{module_name}/...`                                                 | 测试代码                                                                                          |
| **模块文档** | `ai_wellness_advisor/docs/` (项目级文档) <br> `ai_wellness_advisor/src/{module_name}/README_{feature_name}.md` (特性代码说明) <br> `ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_NN_{feature_name}/` (特性开发周期文档) | 项目概述、架构图等存放于 `docs/`。特性相关的代码说明和开发周期文档遵循 `README_folder_feature.md` 规范。                                                                              |

简而言之：`exercise_tdd_xxx/` 目录是“静态的地图和指南”，而 `ai_wellness_advisor/` 是“动态的城市本身”，其内部的 `src/`、`tests/` 和 `dev_cycles/` 共同构成了每个特性“建设蓝图、过程和产出”。所有这些都严格遵循 `README_folder_feature.md` 中定义的核心原则。