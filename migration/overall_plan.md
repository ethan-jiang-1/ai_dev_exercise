# AI个性化健康顾问：项目迁移与演进全盘计划

本文档是项目迁移与演进的“全盘计划”，包含了核心思想、新TDD练习集规划以及通用的LLM协作风险与应对策略。此文档内容相对稳定。

详细的执行步骤请查阅：[`execution_plan.md`](./execution_plan.md)
详细的项目目录结构请查阅：[`overall_folder_structure.md`](./overall_folder_structure.md)

## 1. 核心思想：从小故事到大应用，从分散到统一

当前我们拥有多个独立的TDD练习项目（`exercise_tdd_bmi`、`exercise_tdd_dcnc`、`exercise_tdd_pydantic`、`exercise_tdd_llm`），它们分别代表了“AI个性化健康顾问”这个“大故事”中的基础功能模块（可视为**第0层**的小故事）。

**核心迁移思想**是将这些分散的、独立的TDD练习产出物（源代码、测试、文档）整合到一个**统一的、新的顶级项目目录**中（暂定名为 `ai_wellness_advisor`）。这个统一的 `ai_wellness_advisor` 项目将是**所有生产代码、测试、最终文档和配置的唯一存放地**，承载我们构建“AI个性化健康顾问”的完整应用。与之相对，所有 `exercise_xxx` 目录（包括现有的和新增的）都将严格定位为**静态的TDD练习指南/启动器**，其内部不包含任何实际的、动态的生产内容。


**转变与定位：**

*   **`ai_wellness_advisor` (新顶级项目)**：作为所有代码、测试、文档和配置的单一代码库 (Monorepo)。它将包含从第0层到更高层（第1层数据整合、第2层智能建议）的所有组件。
*   **现有的 `exercise_tdd_xxx` 目录**：其角色将从代码和测试的直接存放地，转变为**“TDD练习启动器/指南”**。这些目录将主要包含一个 `README.md` 或更新后的 `story_xxx.md`，指引用户如何在 `ai_wellness_advisor` 项目中找到对应模块的源代码、运行其TDD练习、查看其特定需求等。它们本身不再包含重复的代码，而是链接或引用到统一项目中的内容。
*   **“大故事”与“小故事”**：
    *   **大故事**：构建一个功能完善的“AI个性化健康顾问”应用。
    *   **小故事 (第0层)**：现有的BMI计算器、DCNC、Pydantic工具集、LLM API工具集，它们是构成大故事的基础模块。
    *   **新的小故事 (第1层、第2层)**：将通过一个新的TDD练习集（见下文 `exercise_ai_wellness_advisor`）来开发，例如 `WellnessProfileBuilder`（健康档案构建器）和 `PersonalizedAdvisor`（个性化顾问）。

**目标：**

*   **清晰的项目结构**：方便开发人员（包括AI助手）理解项目全貌和模块间依赖。
*   **高效的协作**：简化代码共享、集成和测试。
*   **可持续的演进**：为未来添加更多功能和模块打下坚实基础。
*   **完整的TDD实践**：确保从底层模块到高层应用都遵循TDD原则。

## 2. 新TDD练习集规划：`exercise_ai_wellness_advisor` (负责第1层和第2层)

为了通过TDD开发“AI个性化健康顾问”的核心业务逻辑层（第1层和第2层），我们将创建一个新的TDD练习集，暂定名为 `exercise_ai_wellness_advisor`。这个练习集将遵循 `/Users/bowhead/ai_dev_exercise_tdd/exercise_tdd_template` 中定义的框架和流程。

**练习集基本信息：**

*   **练习集名称**: `exercise_ai_wellness_advisor`
*   **存放位置**: `/Users/bowhead/ai_dev_exercise_tdd/exercise_ai_wellness_advisor/`
*   **核心故事主题**: “AI个性化健康顾问核心服务层”
*   **主要实现目录名 (在 `story_xxx.md` 中引用，实际代码在 `ai_wellness_advisor` 中)**: `core_services` (暂定)
*   **故事文件名**: `story_ai_wellness_advisor_core_services.md`

**`story_ai_wellness_advisor_core_services.md` 将包含以下练习系列 (Features)：**

1.  **ExTDD_01_WellnessProfileBuilder**: 健康档案构建与管理
    *   **特性口语化标题**: “构建和管理用户健康档案”
    *   **核心用户需求**: “作为健康顾问系统，我需要能够整合用户的BMI、每日所需热量等基础健康数据，以及用户手动输入的生活习惯、健康目标等信息，构建一个结构化的、可持久化的用户健康档案。我还需要能够更新和检索这些档案信息。”
    *   **涉及层面**: 第1层 - 数据整合与档案构建

2.  **ExTDD_02_PersonalizedAdvisor**: 个性化健康建议生成
    *   **特性口语化标题**: “生成个性化健康与膳食建议”
    *   **核心用户需求**: “作为健康顾问系统，我需要能够基于用户的健康档案（包含BMI、DCNC计算结果、生活习惯、目标等），利用LLM的智能分析能力，为用户生成个性化的健康评估、风险提示、饮食建议和运动计划。建议需要具体、可操作，并能以友好的方式呈现给用户。”
    *   **涉及层面**: 第2层 - 个性化建议与交互

**产出物位置与原则（再次强调以避免歧义）：**

*   **`exercise_ai_wellness_advisor` 目录的铁律**：**严格作为TDD练习的静态“启动器”和“指南”**。它本身**绝对不应包含、也绝不能包含任何重复的生产代码、测试代码或最终的详细设计文档。** 其全部价值在于提供练习的上下文和入口。
*   该目录主要包含且仅应包含：
    *   `story_ai_wellness_advisor_core_services.md`：定义用户故事、TDD练习目标和高级步骤。这是练习的起点。
    *   `tdd_feature_notes/`：此目录下的 `.md` 文件（例如 `ExTDD_01_WellnessProfileBuilder.md`）**必须**作为**纯粹的占位符或高级别指引**。它们的作用是简述对应Feature的TDD练习核心要点，并**强制性地、清晰地引用或链接**到 `ai_wellness_advisor/docs/tdd_process_archive/core_services/` 中对应Feature的**唯一、权威的**详细思考、设计文档和TDD过程记录。
    *   `teaching_framework/`：包含对通用TDD教学和规划方法论文档的引用，或者在必要时存放这些文档的静态副本（如果它们不适合放在 `ai_wellness_advisor/docs` 中）。
*   **所有实际的、可执行的Python源代码** (例如 `wellness_profile_builder.py`, `personalized_advisor.py`) **和所有对应的、可运行的测试代码** (例如 `test_wellness_profile_builder.py`, `test_personalized_advisor.py`) **必须、也只能直接创建和存放在统一的 `ai_wellness_advisor` 项目的相应模块目录下** (例如 `ai_wellness_advisor/src/core_services/` 和 `ai_wellness_advisor/tests/core_services/`)。**这是不可动摇的原则。**
*   **所有TDD过程中的详细思考、设计决策、代码片段演化、遇到的问题与解决方案等文档**，在对应Feature的TDD练习过程中产生后，**必须、也只能最终整理并归档到 `ai_wellness_advisor/docs/tdd_process_archive/core_services/` 下对应的Feature目录中**。`exercise_ai_wellness_advisor/tdd_feature_notes/` 中的文件仅仅是这些权威归档文档的“路标”或“索引入口”，绝非内容副本。

## 3. LLM协作漂移风险及应对策略 (核心要点)

与LLM协作执行长周期计划时，为防范“上下文漂移”或“指令遗忘”，核心应对策略如下：

*   **目标明确与分解**: 设定清晰的阶段性目标，并将任务分解为小而可管理的单元。
*   **上下文维持**: 在多轮交互中，主动提醒LLM关键上下文信息。
*   **简洁指令**: 给予LLM简洁、聚焦的指令，避免单次任务过于复杂。
*   **增量验证与迭代**: 频繁检查LLM的输出，小步快跑，及时纠偏，利用版本控制回溯。
*   **人工监督**: 关键决策和最终确认由人工负责。