# 项目整体目录结构

本文档使用以下占位符：
*   `{app_name}`: 代表应用程序的名称。
*   `{module_name}`: 代表功能模块的名称 (例如 `bmi`, `dcnc`)。
*   `{FeatureName}`: 代表特性的驼峰式名称 (例如 `BMICalculation`)。
*   `{feature_name}`: 代表特性的小写名称 (例如 `bmicalculation`)。
*   `NN`: 代表特性在该模块内的两位数字顺序编号 (例如 `01`, `02`)。

本文档定义了 `ai_dev_exercise_tdd` 项目（根目录）及其内部 `{app_name}` 应用的目录结构和文件组织规范。

## 根目录 

根目录就是项目根目录, README_prj.md 和READ_folders.md, 和 .env所在的目录.

这是整个TDD练习项目的根目录。它包含了各个独立的TDD练习模块 (`exercise_tdd_xxx/`)、最终整合的AI健康助手应用 (`{app_name}/`) 以及一些通用工具和文档。

*   **`README_folders.md`**: (本文档) 描述了整个项目的目录结构和文件组织规范。
*   **`README_prj.md`**: 项目的总体说明、目标、如何开始、贡献指南等。
*   **`exercise_tdd_xxx/`**: 包含各个具体TDD练习的目录，例如 `exercise_tdd_bmi/`, `exercise_tdd_dcnc/` 等。每个这样的目录都是一个独立的学习单元，包含练习说明、教学框架和可能的辅助材料。
*   **`{app_name}/`**: 这是通过各个TDD练习逐步构建起来的最终AI健康助手应用程序。它有自己独立的源代码 (`src/`)、测试代码 (`tests/`)、文档 (`docs/`) 等。 **注意**：下面的项目结构图示例中，为了更清晰地展示 `{app_name}` 内部结构，该图示的“根”实际是 `{app_name}/` 目录，并非整个 `ai_dev_exercise_tdd/` 的根。但为了完整性，结构图的顶层已补充了实际根目录下的关键 `README` 文件。
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
├── .env              # 环境变量配置文件 (如果项目需要)
├── .gitignore        # Git忽略文件
├── requirements.txt  # Python依赖管理 (如果项目需要)
├── ai_wellness_advisor/ # ({app_name}) 应用目录
│   └── README_awa.md
├── exercise_tdd_awa_core/
├── exercise_tdd_bmi/
├── exercise_tdd_dcnc/
├── exercise_tdd_llm/
├── exercise_tdd_pydantic/
├── tdd_exercise_factory/ # TDD练习生成指令和模板
├── tdd_rules/            # TDD通用规则和教学框架文档
└── utils_llm/            # LLM 相关通用工具 (如果项目需要)
    └── ...
```

### 2. `ai_wellness_advisor/` (`{app_name}`) 应用目录结构细节

`ai_wellness_advisor/` 目录是最终AI健康助手应用程序的根目录。当前其结构较为简单，主要包含应用的入口说明文档。随着开发的深入，其内部会逐步建立起源代码、测试、文档和开发周期记录等目录。

**当前实际结构:**
```
ai_wellness_advisor/
└── README_awa.md         # 应用的简要入口和导航
```

**预期逐步完善的结构 (示例):**
```
ai_wellness_advisor/ ({app_name})
├── README_awa.md         # 应用的简要入口和导航
├── src/                # 所有Python模块源代码
│   ├── __init__.py
│   ├── {module_name}/    # 例如: bmi/, dcnc/, core_services/
│   │   ├── __init__.py
│   │   └── ...           # 模块具体实现
│   └── main.py         # 应用主入口 (可选)
├── tests/              # 所有Python测试代码
│   ├── __init__.py
│   └── {module_name}/    # 例如: bmi/, dcnc/, core_services/
│       ├── __init__.py
│       └── ...           # 模块测试代码
├── docs/               # 项目级文档、架构图等
│   └── ...
├── dev_cycles/         # TDD周期内的思考、设计和实现记录
│   └── {module_name}/
│       └── ExTDD_NN_{feature_name}/
│           └── ...       # 具体特性开发周期文档 (遵循 README_folder_feature.md)
└── ...
```
**注意**: `{app_name}` 在本项目中具体指 `ai_wellness_advisor`。

### 3. 各`exercise_tdd_xxx/`练习目录概览
(这些目录位于项目根目录下，提供各TDD练习的入口和相关说明文档)

```
/
├── exercise_tdd_awa_core/    # AI Wellness Advisor 核心组件的TDD练习
│   └── practice_awa_core_components.md
├── exercise_tdd_bmi/         # BMI计算器的TDD练习
│   └── practice_tdd_bmi_calculator.md
├── exercise_tdd_dcnc/        # DCNC的TDD练习
│   └── practice_dcnc_daily_caloric_needs_calculator.md
├── exercise_tdd_llm/         # LLM工具集的TDD练习
│   └── practice_tdd_llm_exercises.md
├── exercise_tdd_pydantic/    # Pydantic模型的TDD练习
│   └── practice_tdd_pydantic.md
# ... 其他 exercise_tdd_xxx 目录以此类推
```

**通用教学框架和规则**: 相关的通用TDD教学框架文档、规划指南和测试设计技巧等，统一存放在根目录下的 `tdd_rules/` 目录中，例如：
```
/
└── tdd_rules/
    ├── planning_tdd_exercise.md
    ├── tdd_unit_test_design_techniques.md
    └── tdd_ai_thinking.md
```

**TDD练习生成工厂**: 用于生成TDD练习结构和模板的指令及文件位于 `tdd_exercise_factory/` 目录：
```
/
└── tdd_exercise_factory/
    ├── generate_tdd_exercise_instructions.md
    └── practice_tdd_template.md
```

**提醒**: `exercise_tdd_xxx` 目录位于项目根级别，与 `ai_wellness_advisor/` (`{app_name}`) 并列。主要的应用程序代码及其TDD周期文档位于 `ai_wellness_advisor/` 内部，如第2节和 `README_folder_feature.md` 中所述。通用TDD规则和教学框架位于 `tdd_rules/`。


#### 每个 ExTDD 练习的目录结构 (针对 feature的详尽说明, 核心思想)

关于每个特性（Feature）的TDD练习周期（包含源代码、测试代码、开发周期记录）的目录结构和文件命名规范的核心思想，请参考：[./README_folder_feature.md](./README_folder_feature.md)


**重要原则与文件定位指南:**

为确保项目结构的清晰与一致性，各类文件和文档的存放位置遵循以下核心原则：

1.  **`{app_name}/`：应用核心**
    *   作为实际构建的应用程序，是所有最终生产代码 (`src/`)、最终测试代码 (`tests/`) 的主要存放地。其根目录下的 `README.md` 作为应用的简要入口和导航。项目与模块级详细文档（如架构设计）位于 `docs/` 目录。权威的用户故事和详细的TDD开发周期文档位于其下的 `dev_cycles/` 目录中，具体结构遵循 `README_folder_feature.md`。

2.  **`exercise_tdd_xxx/`：TDD练习指南**
    *   扮演TDD练习的“静态入口点”角色，提供高级别初始用户故事和练习说明 (如 `practice_xxx.md`)。
    *   `practice_xxx.md` 中的高级别用户故事，其详细阐述和演进记录在 `ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_NN_{feature_name}/_user_story_{feature_name}.md` 中 (当应用开发逐步推进时)。
    *   **严禁** 在 `exercise_tdd_xxx/` 目录下存放任何实际Python源代码、测试脚本或重复的详细设计文档；这些动态内容均属 `ai_wellness_advisor/` (`{app_name}/`)。
    *   通用的教学框架和TDD规则文档位于根目录下的 `tdd_rules/` 目录。

3.  **`{app_name}/dev_cycles/{module_name}/ExTDD_NN_{feature_name}/`：TDD过程记录**
    *   在 `{app_name}` 应用的 `dev_cycles` 目录下，会按照模块名 (`{module_name}`) 和特性 (`ExTDD_NN_{feature_name}`) 进一步组织各个TDD练习周期的详细记录文档。
    *   这些文档记录了思考过程、约束分析、代码迭代和测试演进，遵循 `README_folder_feature.md` 中定义的命名和组织规范。
    *   其对应的源代码和测试代码也遵循 `README_folder_feature.md` 中定义的结构，位于 `{app_name}/src/{module_name}/` 和 `{app_name}/tests/{module_name}/` 下（在特性开发过程中，这些可能是临时的，最终稳定版会整合）。

## 总结速查表

| 文件类型                      | 主要存放位置                                                                    | 说明                                                                                                                               |
| ----------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **启动TDD的练习说明**         | `exercise_tdd_xxx/practice_yyy.md`                                              | 各独立TDD练习的入口和高级别用户故事/说明。                                                                                             |
| **TDD通用规则与教学框架**   | `tdd_rules/`                                                                    | 包含TDD规划、测试设计技巧、AI辅助TDD等通用性文档。                                                                                     |
| **TDD练习生成指令与模板**   | `tdd_exercise_factory/`                                                         | 包含生成新TDD练习的说明文档 (`generate_tdd_exercise_instructions.md`) 和练习模板 (`practice_tdd_template.md`)。                      |
| **TDD开发周期文档**         | `ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_NN_{feature_name}/`           | 详细记录特性开发的用户故事、思考、设计、验证等过程，遵循 `README_folder_feature.md` 规范 (随应用开发逐步创建)。                               |
| **最终功能代码**              | `ai_wellness_advisor/src/{module_name}/...`                                       | 应用程序的实际功能代码 (随应用开发逐步创建)。                                                                                             |
| **最终测试代码**              | `ai_wellness_advisor/tests/{module_name}/...`                                     | 应用程序的单元测试、集成测试等代码 (随应用开发逐步创建)。                                                                                       |
| **应用级文档**                | `ai_wellness_advisor/docs/`                                                       | 应用程序的整体架构、模块概览等 (随应用开发逐步创建)。                                                                                           |
| **项目级README**              | `/README_prj.md`, `/README_folders.md`, `/README_folder_feature.md`             | 项目的总体说明、目录结构规范、特性开发规范。                                                                                               |

简而言之：`exercise_tdd_xxx/` 目录提供独立的TDD练习入口；`tdd_rules/` 提供通用的TDD方法论指导；`tdd_exercise_factory/` 辅助创建新的练习；而 `ai_wellness_advisor/` (`{app_name}`) 是实际构建的应用程序，其内部的 `src/`、`tests/` 和 `dev_cycles/` 共同构成了每个特性“建设蓝图、过程和产出”。所有这些都严格遵循 `README_folder_feature.md` 中定义的核心原则。