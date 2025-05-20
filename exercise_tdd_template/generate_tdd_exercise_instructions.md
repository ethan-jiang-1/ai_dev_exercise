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

**目标**: AI通过与用户进行一系列交互式问答和确认，收集必要信息，然后参照新创建的 `exercise_tdd_template/story_tdd_template.md` 作为结构蓝本，并结合本指令文档中嵌入的撰写指南，生成结构化的单个"练习故事描述文件"。

**交互式故事构建 (Interactive Story Building):**

**AI**: "现在我们来定义练习故事的整体信息。"

1.  **故事识别信息 (Story Identification) - 交互式收集与确认:**
    *   **AI**: "首先，这个练习故事的总体 **主题 (Story Theme)** 是什么？（例如：'BMI计算器' 或 'LLM API调用'）"
    *   **用户**: `[提供故事主题]`
    *   **AI**: (记录主题) "明白了，故事主题是 `[用户提供的主题]`。"
    *   **AI**: "基于此主题，我建议此故事的主要代码实现存放在一个名为 `tdd_[主题的snake_case形式]` 的子目录中。例如，如果主题是 'BMI计算器', 目录名建议为 `tdd_bmi_calculator`。您对 **主要实现目录建议名称 (Suggested Main Implementation Directory Name)** 有什么想法或指定吗？如果同意我的建议，可以直接确认。"
    *   **用户**: `[确认建议 或 提供自定义名称，例如：my_bmi_implementation]`
    *   **AI**: (记录主要实现目录名) "好的，主要实现目录将是 `[用户确认/提供的目录名]`。"
    *   **AI**: "接下来是故事文件的名称。基于练习集 `[current_exercise_collection]` (如果名称类似 `exercise_tdd_[specific_theme]`, 我会尝试提取 `[specific_theme]` 作为建议前缀) 和主题 `[用户提供的主题]`，我建议文件名为 `story_[建议前缀]_[主题的snake_case形式].md`。或者，如果您希望省略前缀，可以是 `story_[主题的snake_case形式].md`。您是否接受此建议，或有特定的 **故事文件名 (Story Filename)**？"
    *   **用户**: `[确认建议 或 提供自定义文件名]`
    *   **AI (Verification)**: (记录故事文件名) "很好。总结一下故事识别信息：
        *   练习集 (Collection): `[current_exercise_collection]`
        *   故事主题 (Theme): `[用户提供的主题]`
        *   主要实现目录名 (Main Impl. Dir): `[用户确认/提供的目录名]`
        *   故事文件名 (Story Filename): `[用户确认/提供的文件名]`
        请确认以上信息是否都正确？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应回溯并修正相应条目)

2.  **核心练习系列规划与定义 (Core Exercise Series Planning & Definition) - 交互式迭代收集与确认:**
    *   **AI**: "在定义具体的练习系列之前，让我们先规划一下整个练习系列的蓝图。请思考：
        1.  **总体学习目标或产品愿景**: 通过这个系列，学习者应掌握什么？或产品要实现什么核心场景？
        2.  **分解主题为特性单元**: 如何将主题分解为逻辑递进、由简入繁的特性单元？每个单元将是一个`ExTDD_XX_FeatureName`练习。
        3.  **学习曲线和复杂度**: 特性单元的顺序是否能形成平滑的学习曲线？
        准备好后，我们将逐个定义这些特性单元。"
    *   **AI**: "现在我们来逐个定义这个故事中包含的核心练习系列。对于第一个练习系列："
    *   **AI**: "请提供一个描述性的 **建议的FeatureName (CamelCase)** (驼峰式命名)，例如 `BMICalculation` 或 `UserAuthentication`。这将用于目录和代码命名。"
    *   **用户**: `[提供FeatureName]`
    *   **AI**: (记录并确认) "好的，FeatureName是 `[用户提供的FeatureName]`。"
    *   **AI**: "这个练习系列的 **特性口语化标题 (Feature Friendly Title)** 是什么？这将用于章节标题等处，例如，如果FeatureName是 `BMICalculation`，口语化标题可以是 'BMI值计算' 或 '计算身体质量指数'。"
    *   **用户**: `[提供特性口语化标题]`
    *   **AI**: (记录并确认) "收到，口语化标题是 `[用户提供的特性口语化标题]`。"
    *   **AI**: "接下来，这个练习系列的 **功能核心目标 (Core User Goal)** 是什么？请遵循以下原则撰写：
        *   **用户视角**：始终从最终用户的角度出发。他们想完成什么？他们有什么痛点？
        *   **简洁明了**：用简单、日常的语言（"用人话说"）来描述，避免技术术语和内部行话。
        *   **关注"什么"，而非"如何"**：描述用户需要什么功能或想解决什么问题，而不是如何技术实现。
        *   **保持高层**：这是一个"粗糙的"故事，细节将在后续的TDD思考阶段中逐步明确。
        *   **避免细节**: 不要在核心用户需求中包含详尽的特定需求清单、具体技术选型、或完整的测试用例/验收标准。这些将在后续TDD步骤中展开。
        例如：'作为一名注册用户，我希望能查看我的个人资料页面，这样我可以看到我的基本信息，比如我的名字和注册时间。' 或者 '用户希望计算出自己的健康指数，如果输入无效，能得到友好提示。'
        请提供它的核心用户目标："
    *   **用户**: `[提供功能核心目标]`
    *   **AI (Verification per feature)**: "练习系列1: FeatureName=`[FeatureName]`, 口语化标题=`[特性口语化标题]`, 功能核心目标=`[核心目标]`。"
    *   **AI**: "您希望为这个故事添加更多练习系列吗？(是/否)"
    *   **用户**: `[是/否]`
        *   如果 **是**：AI重复上述步骤收集下一个练习系列的信息 (FeatureName, 口语化标题, 核心目标)，并相应增加练习系列编号。
        *   如果 **否**：AI继续。
    *   **AI (Overall Verification for series)**: "好的，我们为此故事定义了以下 `[数量]` 个练习系列：
        1.  FeatureName: `[FeatureName1]`, 口语化标题: `[FriendlyTitle1]`, 核心目标: `[Goal1]`
        2.  FeatureName: `[FeatureName2]`, 口语化标题: `[FriendlyTitle2]`, 核心目标: `[Goal2]`
        `...以此类推...`
        这些信息都正确吗？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应允许用户指定哪个系列需要修改，并重新收集该系列信息)。

3.  **可选内容收集 (Optional Content Collection) - 交互式收集:**
    *   **AI**: "核心练习系列已定义完毕。现在，您可以选择为这个故事文件补充一些可选的全局信息。如果您不需要添加某项，可以直接跳过或回复'否'。"
    *   **AI**: "是否有 **额外的总体故事约束 (Additional Overall Story Constraints)** 需要说明？（例如，特定技术栈的强制使用，或对所有练习的通用限制。对应模板中 `{{ADDITIONAL_STORY_CONSTRAINTS_PLACEHOLDER}}`）"
    *   **用户**: `[提供额外约束说明 或 否]`
    *   **AI**: (记录)
    *   **AI**: "这个练习系列是否依赖特定的 **工具包或共享库 (Toolkit or Shared Library)** 需要特别说明其功能？（对应模板中 `{{OPTIONAL_TOOLKIT_DESCRIPTION_PLACEHOLDER}}`）"
    *   **用户**: `[提供工具包说明 或 否]`
    *   **AI**: (记录)
    *   **AI**: "是否有 **通用的约束条件 (General Constraints)**，比如统一的环境配置要求、错误处理标准等，适用于所有特性？（对应模板中 `{{OPTIONAL_GENERAL_CONSTRAINTS_PLACEHOLDER}}`）"
    *   **用户**: `[提供通用约束说明 或 否]`
    *   **AI**: (记录)
    *   **AI**: "是否有建议的 **学习顺序 (Learning Order)**？（对应模板中 `{{OPTIONAL_LEARNING_ORDER_PLACEHOLDER}}`）"
    *   **用户**: `[提供学习顺序说明 或 否]`
    *   **AI**: (记录)
    *   **AI**: "是否有通用的 **技术依赖 (Tech Dependencies)**，比如Python版本、核心库列表？（对应模板中 `{{OPTIONAL_TECH_DEPENDENCIES_PLACEHOLDER}}`）"
    *   **用户**: `[提供技术依赖说明 或 否]`
    *   **AI**: (记录)
    *   **AI**: "是否有关于 **练习难度递进 (Difficulty Progression)** 的说明？（对应模板中 `{{OPTIONAL_DIFFICULTY_PROGRESSION_PLACEHOLDER}}`）"
    *   **用户**: `[提供难度递进说明 或 否]`
    *   **AI**: (记录) "好的，可选信息收集完毕。"

4.  **AI生成`story_xxx.md`文件 - AI执行与告知:**
    *   **AI**: "非常好！我已经收集了所有必要的信息。现在我将根据这些信息生成 `[故事文件名]` 文件。在生成过程中，我会：
        1.  使用您确认的识别信息（主题、实现目录名、文件名、特性列表、核心用户目标、口语化标题、以及所有可选部分的说明等）。
        2.  为每个定义的练习系列，**严格遵循本指令文档中关于"功能核心目标"的撰写指导原则** 来填充"核心用户需求"部分。
        3.  `story_xxx.md` 文件的整体结构将基于 `exercise_tdd_template/story_tdd_template.md` 文件。我会用收集到的信息填充所有相关占位符，例如：
            *   `{{USER_WORKSPACE_ROOT}}` 将使用您系统信息中的工作区绝对路径。
            *   `{{EXAMPLE_FEATURE_NAME_SNAKECASE_1}}`, `{{EXAMPLE_FEATURE_NAME_SNAKECASE_2}}`, `{{EXAMPLE_FEATURE_NAME_CAMELCASE}}` 等示例将根据当前故事主题生成相关的或通用的例子。
            *   所有特性相关的占位符如 `{{FEATURE_NAME_CAMELCASE}}`, `{{FEATURE_NAME_SNAKECASE}}`, `{{CORE_USER_NEED}}`, `{{FEATURE_FRIENDLY_TITLE}}` 等都将被正确填充。
            *   所有可选内容占位符将根据您的输入填充，如果某项无输入，则该占位符及其所在行（如果合适）将被移除或留空。
        4.  文件将保存在 `[current_exercise_collection]/[故事文件名]`。
        我现在开始生成，请稍候。"
    *   **(AI执行文件生成)**
    *   **AI**: "文件 `[故事文件名]` 已成功生成并存放在 `[current_exercise_collection]/` 目录下。建议您稍后抽空检查一下内容。"

**AI生成`story_xxx.md`的核心遵循原则 (AI's Core Principles for Generating `story_xxx.md`):**

*   **输入源 (Input Sources)**: 用户通过上述交互确认的所有信息 (练习集, 故事主题, 主要实现目录名, 故事文件名, 各练习系列的FeatureName、口语化标题、核心用户目标，以及所有可选部分的说明等)。
*   **核心指南1 - "核心用户需求"内容与风格**: 为每个练习系列撰写"核心用户需求"时，严格遵循本指令文档"第2阶段"中"核心练习系列规划与定义"部分所列出的撰写原则和指导。
*   **核心指南2 - 整体文件结构与Boilerplate (`story_tdd_template.md`)**: 使用 `exercise_tdd_template/story_tdd_template.md` 文件作为 `story_xxx.md` 的基础结构模板。AI必须：
    *   使用用户确认的各项信息（如"主要实现目录名称"、特性列表、核心用户需求、口语化标题、可选内容等）来正确填充此模板中的所有占位符。
    *   根据用户系统信息提供的绝对路径填充 `{{USER_WORKSPACE_ROOT}}`。
    *   确保 `FeatureName` 的 `CamelCase` 和 `snake_case` 形式根据用户输入（通常是CamelCase）正确派生并用于相应的占位符。
    *   基于故事主题为模板中的 `{{EXAMPLE_FEATURE_NAME_...}}` 占位符生成具有上下文相关性的示例。
    *   智能处理可选内容的占位符：如果用户没有为某个可选部分提供内容，AI应确保不输出空的或不完整的Markdown结构（例如，移除占位符及其所在的行，或确保该部分在最终文档中被合理地省略）。
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
3.  **第2阶段 - 创建练习故事描述 (`story_xxx.md`)**: AI通过交互式问答和逐层确认，与用户共同定义故事识别信息 (主题、主要实现目录名、故事文件名) 和所有核心练习系列 (FeatureName、核心用户目标)。在此过程中，AI会提供关于规划练习系列和撰写"核心用户需求"的指导。然后，AI声明将使用 `exercise_tdd_template/story_tdd_template.md` 作为结构模板，并结合本指令文档中的撰写指南来生成 `story_xxx.md` 文件，并告知用户生成结果。对每个新故事重复此步骤。
4.  **第3阶段 - 初始化框架文档**: AI与用户交互确认，同步通用的教学框架模板 (`planning_tdd_exercise.md`