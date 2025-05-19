# AI协作生成TDD练习框架指令

本文档记录了通过多步指令与AI协作，生成和初始化TDD练习框架的过程。

## 步骤 0: 确定或创建练习集 (Determine or Create Exercise Collection)

**目标**: 用户指定当前操作是针对现有的练习集，还是创建一个新的练习集。这将决定后续生成的故事文件的存放位置和可能的命名空间。

**交互示例 (Interaction Example):**

AI: "您好！今天我们来创建TDD练习。请问您希望：
    1. 在现有的练习集下工作？
    2. 创建一个新的练习集？"

用户: (选择1或2)

*   **如果用户选择1 (现有练习集):**
    AI: "好的，请输入您要工作的练习集名称（例如：`exercise_tdd_simple` 或 `exercise_tdd_llm`）。"
    用户: `[输入练习集名称，例如：exercise_tdd_llm]`
    AI: "明白了，我们将在 `[练习集名称]` 下进行操作。" (AI记录此上下文：`current_exercise_collection = 'exercise_tdd_llm'`)

*   **如果用户选择2 (创建新练习集):**
    AI: "好的，请输入新练习集的名称（建议格式 `exercise_tdd_[主题]`，例如：`exercise_tdd_robotics`）。"
    用户: `[输入新练习集名称，例如：exercise_tdd_robotics]`
    AI: "明白了，我们将创建一个新的练习集 `[新练习集名称]` 并在此之下操作。" (AI记录此上下文：`current_exercise_collection = 'exercise_tdd_robotics'`, 并准备创建对应目录，可能还会询问是否要将通用的 `teaching_framework` 复制到新目录中)

---

## 第一步指令：生成详细的"练习故事描述文件" (Generate Detailed Story Description File)

**上下文**: 此步骤在"步骤 0"确定了 `current_exercise_collection` （当前练习集）之后执行。

**目标**: AI根据用户提供的故事主题和核心练习系列点子，参照 **位于 `exercise_tdd_template/teaching_framework/planning_tdd_exercise_template.md` 的主模板**，生成详细的、结构化的单个"练习故事描述文件"（例如 `story_tdd_bmi_calculator.md`）。

**通用模板 (General Template):**

```
你好，AI。在当前的练习集 `[AI应自动填充 current_exercise_collection]` 下，我希望你帮我创建一个新的TDD练习故事。

1.  **故事主题 (Story Theme)**：`[请在这里填写您的故事主题，例如："一个简单的任务管理应用"或"一个基于文件的博客生成器"]`

2.  **核心练习系列 (Core Exercise Series)**：我希望这个故事包含以下几个主要的微功能练习系列（请尽可能详细地构思每个系列的名称和它要实现的核心功能点，AI会基于此进行扩展）：
    *   练习系列1:
        *   **建议的FeatureName (CamelCase)**：`[例如：UserAuthentication]`
        *   **功能核心点 (Core Functionality)**：`[例如：实现用户注册和登录功能]`
    *   练习系列2:
        *   **建议的FeatureName (CamelCase)**：`[例如：TaskCreation]`
        *   **功能核心点 (Core Functionality)**：`[例如：允许用户创建新任务，包含任务标题和描述]`
    *   练习系列3 (如果需要更多):
        *   **建议的FeatureName (CamelCase)**：`[例如：TaskListDisplay]`
        *   **功能核心点 (Core Functionality)**：`[例如：展示用户的所有任务列表]`
    *   `... (可以根据需要添加更多练习系列)`

3.  **参考模板 (Reference Template)**：请严格参照位于项目顶层 `exercise_tdd_template/teaching_framework/planning_tdd_exercise_template.md` 的**主规划模板**中的目录结构规范、文件命名规范（特别是 `feature_name` 的 `snake_case` 格式和 `ExTDD_XX_FeatureName` 目录的 `CamelCase` 命名）、以及每个练习系列内部应包含的**"特定需求 (Specific Requirements)"、"技术要点 (Technical Points)"、"验收标准 (Acceptance Criteria)"**等详细信息。
    *   **重要说明**：生成的 `ExTDD_XX_FeatureName` 相关的目录结构（如 `constraints/`, `inputs/`, `outputs/`）应创建在当前练习集 `[AI应自动填充 current_exercise_collection]` 下的对应故事功能模块内 (例如: `[current_exercise_collection]/tdd_[feature_name_lowercase]/ExTDD_XX_FeatureName/`)。

4.  **输出要求 (Output Requirements)**：
    *   请为这个故事生成一个详细的Markdown描述文件。
        *   **文件名建议**: `story_[可选的练习集前缀]_[您的故事主题snake_case形式].md` (例如，如果练习集是 `llm`，主题是 `content_validation`，则为 `story_llm_content_validation.md`；或者直接 `story_content_validation.md` 如果练习集名称已经足够区分)。**AI应与用户确认最终文件名。**
        *   **文件存放路径**: 该文件应直接存放在 `[AI应自动填充 current_exercise_collection]/` 目录下。
    *   在生成的Markdown文件中，需要包含对整个故事的简介。
    *   对于上述每一个"核心练习系列"，请按照项目顶层 `exercise_tdd_template/teaching_framework/planning_tdd_exercise_template.md` 的样式，将其扩展为一个完整的 `ExTDD_XX_FeatureName` 部分，包含清晰的 `feature_name` (`snake_case`)、模拟的目录结构、以及详细的"特定需求"、"技术要点"和"验收标准"。

目标是生成一个像 `@story_tdd_bmi_calculator.md` 或 `@story_tdd_pydantic.md` 那样可以直接用于指导学员进行TDD练习的详细文档。请确保内容丰富、结构清晰。
```

**示例应用 (Example Application for BMI Calculator):**

```
你好，AI。我希望你帮我创建一个新的TDD练习故事。

1.  **故事主题 (Story Theme)**：`BMI计算器`

2.  **核心练习系列 (Core Exercise Series)**：
    *   练习系列1:
        *   **建议的FeatureName (CamelCase)**：`BMICalculation`
        *   **功能核心点 (Core Functionality)**：`实现BMI值的计算，接收身高体重，处理无效输入，控制精度`
    *   练习系列2:
        *   **建议的FeatureName (CamelCase)**：`BMICategorization`
        *   **功能核心点 (Core Functionality)**：`根据BMI值进行分类，支持不同标准，提供分类说明`

3.  **参考模板 (Reference Template)**：请严格参照 `@planning_tdd_exercise_template.md` 文件中定义的**目录结构规范 (Directory Structure Specification)**、**文件命名规范 (File Naming Convention)**（特别是 `feature_name` 的 `snake_case` 格式和 `ExTDD_XX_FeatureName` 目录的 `CamelCase` 命名）、以及每个练习系列内部应包含的**"特定需求 (Specific Requirements)"、"技术要点 (Technical Points)"、"验收标准 (Acceptance Criteria)"**等详细信息。

4.  **输出要求 (Output Requirements)**：
    *   请为这个故事生成一个详细的Markdown描述文件，文件名建议为 `story_tdd_bmi_calculator.md`。
    *   在生成的Markdown文件中，需要包含对整个故事的简介。
    *   对于上述每一个"核心练习系列"，请按照 `@planning_tdd_exercise_template.md` 的样式，将其扩展为一个完整的 `ExTDD_XX_FeatureName` 部分，包含清晰的 `feature_name` (`snake_case`)、模拟的目录结构、以及详细的"特定需求"、"技术要点"和"验收标准"。

目标是生成一个像 `@story_tdd_bmi_calculator.md` 那样可以直接用于指导学员进行TDD练习的详细文档。请确保内容丰富、结构清晰。
```

---

## 第二步指令：初始化或更新练习集框架文档 (Initialize or Update Exercise Collection Framework Documents)

**上下文**: 此步骤在"步骤 0"确定了 `current_exercise_collection` 之后执行，并且通常在第一步为一个或多个故事生成了描述文件之后。

**目标**: AI根据用户指定，将通用的框架文档模板从 `exercise_tdd_template/teaching_framework/` 复制到当前的 `current_exercise_collection` 目录下 (如果尚未存在或需要更新)，并可选择性创建练习集顶级的规划与理念文档。

**通用模板 (General Template):**

```
好的，AI。针对当前的练习集 `[AI应自动填充 current_exercise_collection]`：

我们可能已经通过上一步生成了以下详细的练习故事描述文件：
`@[current_exercise_collection]/[故事描述文件名1.md]`
`@[current_exercise_collection]/[故事描述文件名2.md]`
(如果有更多，继续列出)

现在，请帮我确保 `[AI应自动填充 current_exercise_collection]` 练习集拥有最新的项目框架文档。具体操作如下：

1.  **同步教学框架模板 (Sync Teaching Framework Templates)**:
    *   检查 `[AI应自动填充 current_exercise_collection]/teaching_framework/` 目录是否存在。如果不存在，请创建它。
    *   将项目顶层 `exercise_tdd_template/teaching_framework/planning_tdd_exercise_template.md` 复制到 `[AI应自动填充 current_exercise_collection]/teaching_framework/planning_tdd_exercise_template.md` (如果不存在或用户要求更新)。
    *   将项目顶层 `exercise_tdd_template/teaching_framework/test_driven_development_with_ai_template.md` 复制到 `[AI应自动填充 current_exercise_collection]/teaching_framework/test_driven_development_with_ai_template.md` (如果不存在或用户要求更新)。

2.  **(可选) 创建练习集专属的规划与理念文档 (Optionally Create Collection-Specific Planning & Philosophy Documents)**:
    *   询问用户是否希望为此练习集 `[AI应自动填充 current_exercise_collection]` 创建顶级的规划文档。
    *   如果用户同意，则将项目顶层 `exercise_tdd_template/teaching_framework/planning_tdd_exercise_template.md` (或一个更简洁的规划文档模板) 复制并重命名为 `[AI应自动填充 current_exercise_collection]/planning_this_collection.md` (或类似名称，例如 `planning_exercise_tdd_llm.md`)。
        *   (理想情况) AI可以尝试基于 `[current_exercise_collection]` 内已有的 `story_*.md` 文件，对此新规划文档的示例部分进行初步填充。
    *   询问用户是否希望为此练习集 `[AI应自动填充 current_exercise_collection]` 创建顶级的核心理念文档。
    *   如果用户同意，则将项目顶层 `exercise_tdd_template/teaching_framework/test_driven_development_with_ai_template.md` 复制并重命名为 `[AI应自动填充 current_exercise_collection]/philosophy_this_collection.md` (或类似名称)。

请确保在 `[AI应自动填充 current_exercise_collection]` 目录下，相关的框架文档已准备就绪，并且所有 `story_*.md` 文件都已按预期生成并放置。

(针对"内容也会变好"的期望 - Addressing the expectation of "content enhancement")
如果创建了练习集专属的规划文档 (如 `planning_this_collection.md`)，我理想中是希望其内容（例如示例目录结构或提及的故事列表）能根据 `[current_exercise_collection]` 内已有的具体故事进行一些自动化的初步适配和更新。
```

---

**使用流程回顾 (Usage Workflow Recap):**

1.  **执行步骤0 (Execute Step 0)**: 与AI对话，确定当前要操作的"练习集" (是现有还是新建)。
2.  **执行第一步指令 (Execute Step 1 Instruction)**: 在已确定的练习集上下文中，与AI对话，提供新故事的主题和系列点子，AI生成详细的 `story_*.md` 文件。对每个新故事重复此步骤。
3.  **执行第二步指令 (Execute Step 2 Instruction)**: 在已确定的练习集上下文中，与AI对话，同步通用的教学框架模板到练习集内部，并可选择性地为该练习集创建顶级的规划与理念文档。 