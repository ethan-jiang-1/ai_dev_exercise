# AI个性化健康顾问：项目迁移与演进全盘计划

本文档是项目迁移与演进的“全盘计划”，包含了核心思想、新TDD练习集规划以及通用的LLM协作风险与应对策略。此文档内容相对稳定。

详细的执行步骤请查阅：[`execution_plan.md`](./execution_plan.md)

## 1. 核心思想：从小故事到大应用，从分散到统一

当前我们拥有多个独立的TDD练习项目（`exercise_tdd_bmi`、`exercise_tdd_dcnc`、`exercise_tdd_pydantic`、`exercise_tdd_llm`），它们分别代表了“AI个性化健康顾问”这个“大故事”中的基础功能模块（可视为**第0层**的小故事）。

**核心迁移思想**是将这些分散的、独立的TDD练习产出物（源代码、测试、文档）整合到一个**统一的、新的顶级项目目录**中（暂定名为 `ai_wellness_advisor`）。这个统一的项目将承载我们构建“AI个性化健康顾问”的完整应用。

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

**产出物位置：**

*   `exercise_ai_wellness_advisor` 目录将包含 `story_ai_wellness_advisor_core_services.md` 以及遵循TDD流程产生的思考文档 (`_s1_think_options_xxx.md` 等)。
*   **但是，所有实际的Python源代码 (`wellness_profile_builder.py`, `personalized_advisor.py` 等) 和测试代码 (`test_wellness_profile_builder.py`, `test_personalized_advisor.py` 等) 将直接创建和存放在统一的 `ai_wellness_advisor` 项目的相应模块目录下** (例如 `ai_wellness_advisor/src/core_services/` 和 `ai_wellness_advisor/tests/core_services/`)。

## 3. LLM协作漂移风险及应对策略 (通用指南)

在执行这种多步骤、长周期的项目计划时，特别是与LLM深度协作时，“上下文漂移”或“指令遗忘”是一个需要关注的风险。以下是一些通用应对策略，适用于后续的执行计划：

*   **明确的阶段性目标与核对清单**: 将整个计划分解为具有明确输入、输出和验收标准的阶段。每个阶段开始前，重申该阶段的目标和关键任务。完成后，对照核对清单进行检查。
*   **状态的显式传递与持久化**: 对于跨越多轮交互的任务，可以将关键的上下文信息（如当前模块、已完成步骤、下一步骤的关键参数等）明确地传递给LLM，或者记录在共享的临时文档中，让LLM在需要时查阅。
*   **“心跳”式检查与纠偏**: 在长时间任务执行过程中，可以设置一些“心跳”式的检查点，主动询问LLM当前的任务理解、进度和遇到的问题，及时发现并纠正偏差。
*   **指令的简洁与聚焦**: 避免一次性给LLM下达过于复杂或包含过多子任务的指令。尽量让每个指令聚焦于一个可管理的操作单元。
*   **利用版本控制进行回溯**: 对于代码和文档的修改，充分利用Git等版本控制系统。在LLM执行了重要修改后，及时提交。如果发现严重漂移或错误，可以方便地回溯到上一个稳定版本。
*   **逐步构建与迭代**: 优先完成核心路径和关键模块的迁移与开发，形成一个可工作的最小版本，然后在此基础上逐步迭代和完善其他部分。这有助于降低一次性完成所有任务的复杂度和风险。
*   **日志与记录**: 详细记录与LLM的交互过程、LLM的关键输出以及人工的决策和修正，这有助于在出现问题时进行分析和追溯，也是改进协作流程的宝贵资料。