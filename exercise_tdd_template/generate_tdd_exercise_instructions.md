# AI协作生成TDD练习框架指令

本文档记录了通过两步指令与AI协作，生成和初始化TDD练习框架的过程。

## 第一步指令：生成详细的"练习故事描述文件" (Generate Detailed Story Description File)

**目标**: AI根据用户提供的故事主题和核心练习系列点子，参照 `planning_tdd_exercise_template.md`，生成详细的、结构化的单个"故事描述文件"（例如 `story_tdd_bmi_calculator.md`）。

**通用模板 (General Template):**

```
你好，AI。我希望你帮我创建一个新的TDD练习故事。

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

3.  **参考模板 (Reference Template)**：请严格参照 `@planning_tdd_exercise_template.md` 文件中定义的**目录结构规范 (Directory Structure Specification)**、**文件命名规范 (File Naming Convention)**（特别是 `feature_name` 的 `snake_case` 格式和 `ExTDD_XX_FeatureName` 目录的 `CamelCase` 命名）、以及每个练习系列内部应包含的**"特定需求 (Specific Requirements)"、"技术要点 (Technical Points)"、"验收标准 (Acceptance Criteria)"**等详细信息。

4.  **输出要求 (Output Requirements)**：
    *   请为这个故事生成一个详细的Markdown描述文件，文件名建议为 `story_tdd_[您的故事主题snake_case形式].md` (例如：`story_tdd_task_manager.md`)。
    *   在生成的Markdown文件中，需要包含对整个故事的简介。
    *   对于上述每一个"核心练习系列"，请按照 `@planning_tdd_exercise_template.md` 的样式，将其扩展为一个完整的 `ExTDD_XX_FeatureName` 部分，包含清晰的 `feature_name` (`snake_case`)、模拟的目录结构、以及详细的"特定需求"、"技术要点"和"验收标准"。

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

## 第二步指令：初始化项目框架文档 (Initialize Project Framework Documents)

**目标**: AI根据第一步生成的"故事描述文件"和通用的框架模板，完成项目框架文档的创建和准备。

**通用模板 (General Template):**

```
好的，AI。我们已经通过上一步生成了详细的练习故事描述文件：
`@[这里填入第一个生成的故事描述文件名，例如：story_tdd_bmi_calculator.md]`
`@[这里填入第二个生成的故事描述文件名，例如：story_tdd_pydantic.md]`
(如果有更多，继续列出)

现在，请帮我基于这些故事和我们的标准模板来初始化整个TDD练习的项目框架文档。具体操作如下：

1.  将框架模板 `@planning_tdd_exercise_template.md` 复制一份，并将其重命名为 `planning_tdd_exercise.md`。
2.  将核心理念模板 `@test_driven_development_with_ai_template.md` 复制一份，并将其重命名为 `test_driven_development_with_ai.md`。

请确保最终项目根目录下包含以下文件，并且它们的内容是最新的：
*   `planning_tdd_exercise.md` (由模板复制而来)
*   `test_driven_development_with_ai.md` (由模板复制而来)
*   `@[第一个生成的故事描述文件名]` (已生成)
*   `@[第二个生成的故事描述文件名]` (已生成)
*   ...(其他已生成的故事文件)

(可选，针对之前"内容也会变好"的期望 - Optional, addressing the expectation of "content enhancement")
关于 `planning_tdd_exercise.md`，我理想中是希望其内容（例如示例目录结构）能根据我们实际创建的练习故事（如上面列出的 `@[故事文件名]`）进行一些适配和更新。但如果这步过于复杂或者容易出错，那么直接使用模板内容复制过来也可以接受。重点是确保文件名正确，并且所有提到的文件都准备妥当。
```

---

**使用流程回顾 (Usage Workflow Recap):**

1.  **构思新故事 (Conceptualize New Story)**: 决定新的练习主题和主要的练习系列。
2.  **执行第一步指令 (Execute Step 1 Instruction)**: 与AI对话，提供主题和系列点子，AI生成详细的 `story_tdd_*.md` 文件。对每个新故事重复此步骤。
3.  **执行第二步指令 (Execute Step 2 Instruction)**: 与AI对话，提供所有已生成的 `story_tdd_*.md` 文件列表，AI复制并重命名框架模板文件。此步骤通常在所有故事文件准备好后执行一次。 