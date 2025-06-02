<!-- 定义占位符 -->
<!-- 
{app_name}: 指代项目或应用的根目录名称，例如 "ai_wellness_advisor"。
{module_name}: 指代项目中的一个模块名称，例如 "bmi" 或 "user_profile"。
{FeatureName}: 指代模块下的一个具体特性名称，采用驼峰式命名，例如 "BMICalculation"。
{feature_name}: 指代模块下的一个具体特性名称，采用下划线命名，例如 "bmi_calculation"。
NN: 指代特性的两位数序号，例如 "01", "02"。
-->

# AI协作生成TDD练习框架指令
> 版本: 3.0

**重要说明：** 本文档描述了一个**交互式、多步骤、有状态的AI协作流程**。AI将引导用户逐步完成新TDD练习系列的创建，并在关键步骤进行信息确认。

## 预备对话：AI向用户阐述流程

**AI开场白示例：**
"您好！今天我们将一起以交互方式创建一个新的TDD练习系列。我将引导您完成几个主要阶段，包括定义练习集、构思practice和特性、以及初始化必要的框架文档。在每个阶段，我会向您请求具体信息，并在继续之前与您确认我的理解。这样可以确保我们高效地产出您期望的结果。准备好开始了吗？"

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

## 第2阶段：创建练习practice描述 (`practice_xxx.md`) (Creating the Exercise practice Description)

**上下文**: 此阶段在"第1阶段"确定了 `current_exercise_collection` （当前练习集）之后执行。

**目标**: AI通过与用户进行一系列交互式问答和确认，收集必要信息，然后参照更新后的 `tdd_exercise_factory/practice_tdd_template.md` 作为结构蓝本，并结合本指令文档中嵌入的撰写指南，生成结构化的单个"练习practice描述文件"。

**交互式practice构建 (Interactive practice Building):**

**AI**: "现在我们来定义练习practice的整体信息。"

1.  **practice识别信息 (practice Identification) - 交互式收集与确认:**
    *   **AI**: "首先，这个练习practice的总体 **主题 (practice Theme) / 应用友好名称 (APP_FRIENDLY_NAME)** 是什么？（例如：'BMI Calculator' 或 'LLM API Caller'）"
    *   **用户**: `[提供故事主题]`
    *   **AI**: (记录主题/友好名称) "明白了，practice主题/友好名称是 `[用户提供的主题]`。"
    *   **AI**: "基于此主题，我建议此practice的 **应用核心名称 (APP_NAME)** 为 `[主题的snake_case形式]` (例如 'bmi_calculator')。主要代码实现将位于 `{app_name}/src/[APP_NAME]`，相关的测试代码将位于 `{app_name}/tests/[APP_NAME]`，开发过程文档将位于 `{app_name}/dev_cycles/[APP_NAME]`。您对此建议有什么想法或指定吗？如果同意我的建议，可以直接确认。"
    *   **用户**: `[确认建议 或 提供自定义名称，例如：my_bmi_implementation]`
    *   **AI**: (记录应用核心名称 APP_NAME) "好的，应用核心名称 (APP_NAME) 将是 `[用户确认/提供的APP_NAME]`。"
    *   **AI**: "接下来是practice文件的名称。基于应用核心名称 `[APP_NAME]`，我建议文件名为 `practice_tdd_[APP_NAME].md`。您是否接受此建议，或有特定的 **practice文件名 (practice Filename)**？"
    *   **用户**: `[确认建议 或 提供自定义文件名]`
    *   **AI (Verification)**: (记录practice文件名) "很好。总结一下practice识别信息：
        *   练习集 (Collection): `[current_exercise_collection]`
        *   practice主题/应用友好名称 (Theme/APP_FRIENDLY_NAME): `[用户提供的主题]`
        *   应用核心名称 (APP_NAME): `[用户确认/提供的APP_NAME]`
        *   practice文件名 (practice Filename): `[用户确认/提供的文件名]`
        请确认以上信息是否都正确？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应回溯并修正相应条目)

2.  **核心练习系列规划与定义 (Core Exercise Series Planning & Definition) - 交互式迭代收集与确认:**
    *   **AI**: "在定义具体的特性之前，请先提供 **特性ID前缀 (FEATURE_ID_PREFIX)**，例如 `BMI` 或 `AWA_CORE`。这个前缀将用于构成完整的特性ID。"
    *   **用户**: `[提供FEATURE_ID_PREFIX]`
    *   **AI**: (记录并确认) "好的，特性ID前缀是 `[用户提供的FEATURE_ID_PREFIX]`。"
    *   **AI**: "现在我们来逐个定义这个practice中包含的特性。对于第一个特性："
    *   **AI**: "请提供一个描述性的 **特性名称 (FEATURE_NAME_CAMELCASE)** (驼峰式命名)，例如 `calculateBmi` 或 `authenticateUser`。这将用于目录和代码命名。我稍后会自动为其生成补零的索引。"
    *   **用户**: `[提供FeatureName]`
    *   **AI**: (记录并确认) "好的，特性名称 (FEATURE_NAME_CAMELCASE) 是 `[用户提供的特性名称]`。"
    *   **AI**: "这个特性的 **友好标题 (FEATURE_FRIENDLY_TITLE)** 是什么？这将用于章节标题等处，例如，如果特性名称是 `calculateBmi`，友好标题可以是 'Calculate BMI' 或 '计算身体质量指数'。"
    *   **用户**: `[提供特性口语化标题]`
    *   **AI**: (记录并确认) "收到，友好标题是 `[用户提供的友好标题]`。"
    *   **AI**: "接下来，这个特性的 **用户故事 (USER_STORY)** 是什么？请遵循敏捷开发中用户故事的格式，例如：'作为一名[角色]，我想要[行为]，以便[价值]。'"
    *   **用户**: `[提供用户故事]`
    *   **AI**: (记录并确认) "好的，用户故事是：`[用户提供的用户故事]`。"
    *   **AI**: "请提供这个特性的 **验收标准 (ACCEPTANCE_CRITERIA)**，使用Markdown列表格式。"
    *   **用户**: `[提供验收标准]`
    *   **AI**: (记录并确认) "好的，验收标准已记录。"
    *   **AI**: "是否有关于此特性的 **技术说明 (TECHNICAL_NOTES)**？（可选）"
    *   **用户**: `[提供技术说明 或 否]`
    *   **AI**: (记录技术说明，如果提供)
    *   **用户**: `[提供功能核心目标]`
    *   **AI (Verification per feature)**: "特性1: 名称=`[FEATURE_NAME_CAMELCASE]`, 友好标题=`[FEATURE_FRIENDLY_TITLE]`, 用户故事=`[USER_STORY]`, 验收标准记录完毕, 技术说明(如有)=`[TECHNICAL_NOTES]`。"
    *   **AI**: "您希望为此practice添加更多特性吗？(是/否)"
    *   **用户**: `[是/否]`
        *   如果 **是**：AI重复上述步骤收集下一个特性的信息 (FEATURE_NAME_CAMELCASE, FEATURE_FRIENDLY_TITLE, USER_STORY, ACCEPTANCE_CRITERIA, TECHNICAL_NOTES)，并自动为其生成补零的索引。
        *   如果 **否**：AI继续。
    *   **AI (Overall Verification for features)**: "好的，我们为此practice定义了以下 `[数量]` 个特性 (特性ID前缀为 `[FEATURE_ID_PREFIX]`)：
        1.  名称: `[FEATURE_NAME_CAMELCASE_1]`, 友好标题: `[FRIENDLY_TITLE_1]`, 用户故事: `[USER_STORY_1]`, ...
        2.  名称: `[FEATURE_NAME_CAMELCASE_2]`, 友好标题: `[FRIENDLY_TITLE_2]`, 用户故事: `[USER_STORY_2]`, ...
        `...以此类推...`
        这些信息都正确吗？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应允许用户指定哪个系列需要修改，并重新收集该系列信息)。

3.  **可选内容收集 (Optional Content Collection) - 交互式收集:**
    *   **AI**: "特性列表已定义完毕。现在，您可以选择为这个practice文件补充一些可选的全局信息。如果您不需要添加某项，可以直接跳过或回复'否'。这些信息将用于填充模板中的相应占位符。"
    *   **AI**: "这是否是一个系列练习 (IS_SERIES_EXERCISE)？（是/否）如果是，请提供系列ID (SERIES_ID) 和系列友好名称 (SERIES_FRIENDLY_NAME)。"
    *   **用户**: `[是/否，以及可选的系列信息]`
    *   **AI**: (记录IS_SERIES_EXERCISE, SERIES_ID, SERIES_FRIENDLY_NAME)
    *   **AI**: "如果这是一个系列练习，并且有共享的核心实现路径说明 (MAIN_IMPLEMENTATION_PATH_INFO)，请提供。例如，`awa_core_components` 目录是做什么的。"
    *   **用户**: `[提供MAIN_IMPLEMENTATION_PATH_INFO 或 否]`
    *   **AI**: (记录MAIN_IMPLEMENTATION_PATH_INFO)
    *   **AI**: "是否有 **额外的总体practice约束 (Additional Overall practice Constraints)** 需要说明？（例如，特定技术栈的强制使用，或对所有练习的通用限制。此内容将加入文件头部的约束说明中，每一行都会以'> '开头保持格式。）对应模板中 `{{ADDITIONAL_PRACTICE_CONSTRAINTS_PLACEHOLDER}}`）"
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

4.  **AI生成`practice_xxx.md`文件 - AI执行与告知:**
    *   **AI**: "非常好！我已经收集了所有必要的信息。现在我将根据这些信息生成 `[practice文件名]` 文件。在生成过程中，我会：
        1.  使用您确认的识别信息（APP_NAME, APP_FRIENDLY_NAME, practice文件名, IS_SERIES_EXERCISE, SERIES_ID, SERIES_FRIENDLY_NAME, MAIN_IMPLEMENTATION_PATH_INFO, FEATURE_ID_PREFIX, 以及 FEATURES 数组中的所有字段）。
        2.  `practice_xxx.md` 文件的整体结构将基于 `tdd_exercise_factory/practice_tdd_template.md` 文件。我会用收集到的信息填充所有相关占位符。
        3.  确保特性列表 (`FEATURES`) 以正确的数组对象格式传递给模板渲染引擎。
        4.  所有可选内容占位符将根据您的输入填充，模板中的条件渲染逻辑 (`{{#if ...}}`) 会处理不存在值的字段。
        4.  文件将保存在 `[current_exercise_collection]/[practice文件名]`。
        我现在开始生成，请稍候。"
    *   **(AI执行文件生成)**
    *   **AI**: "文件 `[practice文件名]` 已成功生成并存放在 `[current_exercise_collection]/` 目录下。建议您稍后抽空检查一下内容。"

**AI生成`practice_xxx.md`的核心遵循原则 (AI's Core Principles for Generating `practice_xxx.md`):**

*   **输入源 (Input Sources)**: 用户通过上述交互确认的所有信息，包括 `APP_NAME`, `APP_FRIENDLY_NAME`, `IS_SERIES_EXERCISE`, `SERIES_ID`, `SERIES_FRIENDLY_NAME`, `MAIN_IMPLEMENTATION_PATH_INFO`, `FEATURE_ID_PREFIX`, 以及包含每个特性详情的 `FEATURES` 数组 (`FEATURE_INDEX_PADDED`, `FEATURE_NAME_CAMELCASE`, `FEATURE_FRIENDLY_TITLE`, `USER_STORY`, `ACCEPTANCE_CRITERIA`, `TECHNICAL_NOTES`)，还有所有可选部分的说明等。
*   **核心指南1 - 数据结构**: 确保传递给模板渲染引擎的数据结构与 `practice_tdd_template.md` 中的占位符和逻辑 (如 `{{#each FEATURES}}`, `{{#if IS_SERIES_EXERCISE}}`) 相匹配。
*   **核心指南2 - 整体文件结构与Boilerplate (`practice_tdd_template.md`)**: 使用 `tdd_exercise_factory/practice_tdd_template.md` 文件作为 `practice_xxx.md` 的基础结构模板。AI必须：
    *   使用收集到的信息正确填充模板中的所有占位符。
    *   根据用户系统信息提供的绝对路径填充 `{{USER_WORKSPACE_ROOT}}`。
    *   确保特性ID (`{{FEATURE_ID_PREFIX}}_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}`) 能被正确构建和渲染。
    *   模板中的条件渲染逻辑将处理可选字段的显示。
*   **核心指南3 - 目录结构指示 (Path representation inside `practice_xxx.md`)**: 生成的 `practice_xxx.md` 文件应清晰地描述每个特性 (`{{FEATURE_ID_PREFIX}}_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}`) 的源代码、测试代码和开发过程文档的存放位置。所有这些路径都**必须**明确指向 `../{{APP_NAME}}` 项目的相应子目录（例如 `../{{APP_NAME}}/src/{{APP_NAME}}/{{FEATURE_ID_PREFIX}}_{{FEATURE_INDEX_PADDED}}_{{FEATURE_NAME_CAMELCASE}}/`）。模板已更新以使用正确的相对路径，AI只需确保 `APP_NAME` 和特性相关的占位符被正确替换。
*   **输出文件**: 用户确认的文件名，存放在 `[current_exercise_collection]/` 目录下。

---

## 第3阶段：初始化框架文档 (Initializing Framework Documents)

**上下文**: 此阶段在"第1阶段"确定了 `current_exercise_collection` 之后执行，并且通常在"第2阶段"为一个或多个practice生成了描述文件之后。

**目标**: AI通过与用户交互，确认并将通用的框架文档模板从 `factory_exercise_tdd/teaching_framework/` 复制到当前的 `current_exercise_collection` 目录下，并可选择性创建练习集顶级的规划与理念文档。

**交互式文档同步 (Interactive Document Sync):**

1.  **AI**: "现在，我们来处理 `[current_exercise_collection]` 练习集的教学框架文档。首先，我会检查并确保核心框架文件已同步。这包括将 `planning_tdd_exercise.md` 和 `test_driven_development_with_ai.md` 从主模板复制到 `[current_exercise_collection]/teaching_framework/` 目录（如果目录或文件不存在，我会创建它们）。是否继续？(是/否)"
2.  **用户**: `[是/否]`
3.  **AI**: (如果用户同意)
    *   **(AI执行文件检查与复制操作)**
    *   **AI**: "核心框架文件已同步完毕。"
4.  **AI**: "接下来，您可以选择为此练习集 `[current_exercise_collection]` 创建顶级的、专属的规划文档 (基于 `planning_tdd_exercise.md` 模板，例如命名为 `planning_this_collection.md` 或 `planning_[current_exercise_collection].md`)。创建后，我可以尝试根据此练习集内已有的practice对其进行初步内容适配。您是否希望创建此练习集专属规划文档？(是/否)"
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
3.  **第2阶段 - 创建练习practice描述 (`practice_xxx.md`)**: AI通过交互式问答和逐层确认，与用户共同定义practice识别信息 (`APP_NAME`, `APP_FRIENDLY_NAME`, practice文件名) 和所有特性 (`FEATURE_ID_PREFIX`, `FEATURES` 数组包含 `FEATURE_NAME_CAMELCASE`, `FEATURE_FRIENDLY_TITLE`, `USER_STORY`, `ACCEPTANCE_CRITERIA`, `TECHNICAL_NOTES`)。AI还会收集可选的系列信息 (`IS_SERIES_EXERCISE`, `SERIES_ID`, `SERIES_FRIENDLY_NAME`, `MAIN_IMPLEMENTATION_PATH_INFO`)。然后，AI声明将使用 `tdd_exercise_factory/practice_tdd_template.md` 作为结构模板生成 `practice_xxx.md` 文件，并告知用户生成结果。对每个新practice重复此步骤。
4.  **第3阶段 - 初始化框架文档**: AI与用户交互确认，同步通用的教学框架模板 (`planning_tdd_exercise.md` 和 `test_driven_development_with_ai.md`) 到练习集内部，并可选择性地为该练习集创建顶级的规划与理念文档，每一步操作都进行沟通。

目标是生成一个结构和内容都符合预期的 `practice_xxx.md` 文件，可以直接用于指导学员进行TDD练习。请确保内容满足用户输入，并严格遵循所引用的模板和本文档内的撰写指南，实现结构清晰、风格一致。