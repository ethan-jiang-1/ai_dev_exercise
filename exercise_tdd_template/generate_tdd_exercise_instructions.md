# AI协作生成TDD练习框架指令

**重要说明：** 本文档描述了一个**交互式、多步骤、有状态的AI协作流程**。AI将引导用户逐步完成新TDD练习系列的创建，并在关键步骤进行信息确认。

## 预备对话：AI向用户阐述流程

**AI开场白示例：**
"您好！今天我们将一起以交互方式创建一个新的TDD练习系列。我将引导您完成几个主要阶段，包括定义练习集、构思故事和特性、以及初始化必要的框架文档。在每个阶段，我会向您请求具体信息，并在继续之前与您确认我的理解。这样可以确保我们高效地产出您期望的结果。准备好开始了吗？"

## 第1阶段：设定练习集 (Setting up the Exercise Collection)

**目标**: 用户指定当前操作是针对现有的练习集，还是创建一个新的练习集。这将决定后续生成的故事文件的存放位置和可能的命名空间。

**交互式设定 (Interactive Setup):**

1.  **AI**: "请问您希望：
    1.  在现有的练习集下工作？
    2.  创建一个新的练习集？"
2.  **用户**: (选择1或2)
3.  **AI**: (根据用户选择处理)
    *   **如果用户选择1 (现有练习集):**
        *   **AI**: "好的，请输入您要工作的练习集名称（例如：`exercise_tdd_simple` 或 `exercise_tdd_llm`）。"
        *   **用户**: `[输入练习集名称，例如：exercise_tdd_llm]`
        *   **AI**: "明白了，我们将在 `[练习集名称]` 下进行操作。" (AI记录此上下文：`current_exercise_collection = 'exercise_tdd_llm'`)
    *   **如果用户选择2 (创建新练习集):**
        *   **AI**: "好的，请输入新练习集的名称（建议格式 `exercise_tdd_[主题]`，例如：`exercise_tdd_robotics`）。"
        *   **用户**: `[输入新练习集名称，例如：exercise_tdd_robotics]`
        *   **AI**: "明白了，我们将创建一个新的练习集 `[新练习集名称]` 并在此之下操作。" (AI记录此上下文：`current_exercise_collection = 'exercise_tdd_robotics'`, 并应提示用户或自行创建对应的目录 `[新练习集名称]/`)

---

## 第2阶段：创建练习故事描述 (`story_xxx.md`) (Creating the Exercise Story Description)

**上下文**: 此阶段在"第1阶段"确定了 `current_exercise_collection` （当前练习集）之后执行。

**目标**: AI通过与用户进行一系列交互式问答和确认，收集必要信息，然后参照项目内的指导文档，生成结构化的单个"练习故事描述文件"。

**交互式故事构建 (Interactive Story Building):**

**AI**: "现在我们来定义练习故事的整体信息。"

1.  **故事识别信息 (Story Identification) - 交互式收集与确认:**
    *   **AI**: "首先，这个练习故事的总体 **主题 (Story Theme)** 是什么？（例如：'BMI计算器' 或 'LLM API调用'）"
    *   **用户**: `[提供故事主题]`
    *   **AI**: (记录主题) "明白了，故事主题是 `[用户提供的主题]`。"
    *   **AI**: "基于此主题，我建议此故事的主要代码实现存放在一个名为 `tdd_[主题的snake_case形式]` 的子目录中。例如，如果主题是 'BMI计算器', 目录名建议为 `tdd_bmi_calculator`。您对 **主要实现目录建议名称 (Suggested Main Implementation Directory Name)** 有什么想法或指定吗？如果同意我的建议，可以直接确认。"
    *   **用户**: `[确认建议 或 提供自定义名称，例如：my_bmi_implementation]`
    *   **AI**: (记录主要实现目录名) "好的，主要实现目录将是 `[用户确认/提供的目录名]`。"
    *   **AI**: "接下来是故事文件的名称。基于练习集 `[current_exercise_collection]` 和主题 `[用户提供的主题]`，我建议文件名为 `story_[可选练习集前缀]_[主题的snake_case形式].md`。您是否接受此建议，或有特定的 **故事文件名 (Story Filename)**？"
    *   **用户**: `[确认建议 或 提供自定义文件名]`
    *   **AI (Verification)**: (记录故事文件名) "很好。总结一下故事识别信息：
        *   练习集 (Collection): `[current_exercise_collection]`
        *   故事主题 (Theme): `[用户提供的主题]`
        *   主要实现目录名 (Main Impl. Dir): `[用户确认/提供的目录名]`
        *   故事文件名 (Story Filename): `[用户确认/提供的文件名]`
        请确认以上信息是否都正确？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应回溯并修正相应条目)

2.  **核心练习系列 (Core Exercise Series) - 交互式迭代收集与确认:**
    *   **AI**: "现在我们来逐个定义这个故事中包含的核心练习系列。对于第一个练习系列："
    *   **AI**: "请提供一个描述性的 **建议的FeatureName (CamelCase)** (驼峰式命名)，例如 `BMICalculation` 或 `UserAuthentication`。"
    *   **用户**: `[提供FeatureName]`
    *   **AI**: "好的，FeatureName是 `[用户提供的FeatureName]`。这个练习系列的 **功能核心目标 (Core User Goal)** 是什么？请用一两句简洁的用户视角描述，例如：'用户希望计算出自己的健康指数' 或 '用户需要能安全地创建账户并登录系统'。"
    *   **用户**: `[提供功能核心目标]`
    *   **AI (Verification per feature)**: "练习系列1: FeatureName=`[FeatureName]`, 功能核心目标=`[核心目标]`。"
    *   **AI**: "您希望为这个故事添加更多练习系列吗？(是/否)"
    *   **用户**: `[是/否]`
        *   如果 **是**：AI重复上述步骤收集下一个练习系列的信息 (FeatureName, 核心目标)，并相应增加练习系列编号。
        *   如果 **否**：AI继续。
    *   **AI (Overall Verification for series)**: "好的，我们为此故事定义了以下 `[数量]` 个练习系列：
        1.  FeatureName: `[FeatureName1]`, 核心目标: `[Goal1]`
        2.  FeatureName: `[FeatureName2]`, 核心目标: `[Goal2]`
        `...以此类推...`
        这些信息都正确吗？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应允许用户指定哪个系列需要修改，并重新收集该系列信息)。

3.  **AI生成`story_xxx.md`文件 - AI执行与告知:**
    *   **AI**: "非常好！我已经收集了所有必要的信息。现在我将根据这些信息生成 `[故事文件名]` 文件。在生成过程中，我会：
        1.  使用您确认的识别信息（主题、实现目录名、文件名）。
        2.  为每个定义的练习系列（FeatureName 和核心目标），**严格遵循 `exercise_tdd_template/writing_story_files.md` 中的指导原则** 来撰写其"核心用户需求"部分，确保聚焦于高层级、用户视角的需求。
        3.  `story_xxx.md` 文件的整体结构（如标准头部信息、章节标题、`ExTDD_XX_FeatureName` 部分的布局等）将参考 `exercise_tdd_template/teaching_framework/planning_tdd_exercise.md` 作为基础模板，并结合您提供的"主要实现目录名称"调整相关路径。
        4.  文件将保存在 `[current_exercise_collection]/[故事文件名]`。
        我现在开始生成，请稍候。"
    *   **(AI执行文件生成)**
    *   **AI**: "文件 `[故事文件名]` 已成功生成并存放在 `[current_exercise_collection]/` 目录下。建议您稍后抽空检查一下内容。"

**AI生成`story_xxx.md`的核心遵循原则 (AI's Core Principles for Generating `story_xxx.md`):**

*   **输入源 (Input Sources)**: 用户通过上述交互确认的所有信息 (练习集, 故事主题, 主要实现目录名, 故事文件名, 各练习系列的FeatureName和核心用户目标)。
*   **核心指南1 - 故事内容与风格 (`writing_story_files.md`)**: 为每个练习系列撰写"核心用户需求"时，严格遵循此文件。
*   **核心指南2 - 整体文件结构与Boilerplate (`planning_tdd_exercise.md`)**: 使用此文件作为 `story_xxx.md` 的基础结构模板。AI必须使用用户确认的"主要实现目录名称"来正确填充模板中所有指向实际代码存放目录的相对路径（例如，在"实现目录说明"中填写 `./[主要实现目录名称]/`，以及在每个 `ExTDD_XX_FeatureName` 部分的路径展示中填写 `./[主要实现目录名称]/ExTDD_XX_FeatureName/`）。
*   **核心指南3 - 目录结构指示 (Path representation inside `story_xxx.md`)**: 生成的 `story_xxx.md` 文件应描述每个 `ExTDD_XX_FeatureName` 系列建议的目录结构。这些路径在 `story_xxx.md` 内部应表示为相对于 `story_xxx.md` 文件自身位置的路径，并结合用户确认的"主要实现目录名称"（如 `./[主要实现目录名称]/ExTDD_XX_FeatureName/`）。
*   **输出文件**: 用户确认的文件名，存放在 `[current_exercise_collection]/` 目录下。

---

## 第3阶段：初始化框架文档 (Initializing Framework Documents)

**上下文**: 此阶段在"第1阶段"确定了 `current_exercise_collection` 之后执行，并且通常在"第2阶段"为一个或多个故事生成了描述文件之后。

**目标**: AI通过与用户交互，确认并将通用的框架文档模板从 `exercise_tdd_template/teaching_framework/` 复制到当前的 `current_exercise_collection` 目录下，并可选择性创建练习集顶级的规划与理念文档。

**交互式文档同步 (Interactive Document Sync):**

1.  **AI**: "现在，我们来处理 `[current_exercise_collection]` 练习集的教学框架文档。首先，我会检查并确保核心框架文件已同步。这包括将 `planning_tdd_exercise.md` 和 `test_driven_development_with_ai.md` 从主模板复制到 `[current_exercise_collection]/teaching_framework/` 目录（如果目录或文件不存在，我会创建它们）。是否继续？(是/否)"
2.  **用户**: `[是/否]`
3.  **AI**: (如果用户同意)
    *   **(AI执行文件检查与复制操作)**
    *   **AI**: "核心框架文件已同步完毕。"
4.  **AI**: "接下来，您可以选择为此练习集 `[current_exercise_collection]` 创建顶级的、专属的规划文档 (基于 `planning_tdd_exercise.md` 模板，例如命名为 `planning_this_collection.md` 或 `planning_[current_exercise_collection].md`)。创建后，我可以尝试根据此练习集内已有的故事对其进行初步内容适配。您是否希望创建此练习集专属规划文档？(是/否)"
5.  **用户**: `[是/否]`
6.  **AI**: (如果用户同意)
    *   **AI**: "好的，请建议一个文件名，或者接受默认的 `planning_this_collection.md`？"
    *   **用户**: `[提供文件名或确认默认]`
    *   **(AI执行复制、重命名及可能的初步内容适配)**
    *   **AI**: "练习集专属规划文档 `[文件名]` 已创建。"
7.  **AI**: "类似地，您也可以选择为此练习集 `[current_exercise_collection]` 创建顶级的、专属的核心理念文档 (基于 `test_driven_development_with_ai.md` 模板，例如命名为 `philosophy_this_collection.md`)。您是否希望创建此练习集专属核心理念文档？(是/否)"
8.  **用户**: `[是/否]`
9.  **AI**: (如果用户同意)
    *   **AI**: "好的，请建议一个文件名，或者接受默认的 `philosophy_this_collection.md`？"
    *   **用户**: `[提供文件名或确认默认]`
    *   **(AI执行复制与重命名)**
    *   **AI**: "练习集专属核心理念文档 `[文件名]` 已创建。"
10. **AI**: "练习集框架文档处理完毕。"

---

## 总体交互流程概览 (Overall Interactive Workflow Overview)

1.  **AI开场**: AI解释交互式流程。
2.  **第1阶段 - 设定练习集**: AI与用户对话，确定当前要操作的"练习集" (是现有还是新建)，并确认。
3.  **第2阶段 - 创建练习故事描述 (`story_xxx.md`)**: AI通过交互式问答和逐层确认，与用户共同定义故事识别信息 (主题、主要实现目录名、故事文件名) 和所有核心练习系列 (FeatureName、核心用户目标)。然后，AI声明将遵循 `writing_story_files.md` (内容风格) 和 `planning_tdd_exercise.md` (结构模板，结合实现目录名) 来生成 `story_xxx.md` 文件，并告知用户生成结果。对每个新故事重复此步骤。
4.  **第3阶段 - 初始化框架文档**: AI与用户交互确认，同步通用的教学框架模板 (`planning_tdd_exercise.md` 和 `test_driven_development_with_ai.md`) 到练习集内部，并可选择性地为该练习集创建顶级的规划与理念文档，每一步操作都进行沟通。

目标是生成一个像 `@story_tdd_bmi_calculator.md` 或 `@story_tdd_pydantic.md` (已按 `writing_story_files.md` 原则调整后的版本) 那样，可以直接用于指导学员进行TDD练习的文档。请确保内容满足用户输入，并严格遵循所引用的文档指南，实现结构清晰、风格一致。 