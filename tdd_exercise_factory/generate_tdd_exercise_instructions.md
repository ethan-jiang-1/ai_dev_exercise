<!-- 定义占位符 -->
<!-- 
{app_name}: 指代项目或应用的根目录名称，例如 "ai_wellness_advisor"。
{module_name}: 指代项目中的一个模块名称，例如 "bmi" 或 "user_profile"。
{FeatureName}: 指代模块下的一个具体特性名称，采用驼峰式命名，例如 "BMICalculation"。
{feature_name}: 指代模块下的一个具体特性名称，采用下划线命名，例如 "bmi_calculation"。
NN: 指代特性的两位数序号，例如 "01", "02"。
current_exercise_collection: 指代当前操作的练习集目录名称，例如 "exercise_tdd_bmi"。
-->

# AI协作生成TDD练习框架指令
> 版本: 3.0

**核心目标：** 本文档指导AI通过与用户进行**交互式、多步骤、有状态的协作流程**，逐步创建**全新的**TDD练习系列，并在关键步骤进行信息确认，确保高效产出。如需修改或调整**现有**的练习集，请参考 `tdd_exercise_factory/modify_tdd_exercise_instructions.md` (即将创建)。

## 预备对话：AI向用户阐述流程

**AI开场白示例：**
"您好！今天我们将一起以交互方式创建一个**全新的**TDD练习系列。我将引导您完成几个主要阶段，包括定义练习集、构思practice和特性、以及初始化必要的框架文档。在每个阶段，我会向您请求具体信息，并在继续之前与您确认我的理解。这样可以确保我们高效地产出您期望的结果。准备好开始了吗？"

## 第1阶段：设定新练习集 (Setting up a New Exercise Collection)

**目标**: 明确用户要创建的新练习集信息，以确定后续文件存放位置和命名空间。

**交互流程**:
1. AI向用户说明，此流程专注于创建**全新的**练习集。
2. AI请求用户提供新练习集的名称 (建议格式 `exercise_tdd_[主题]`)。
3. AI记录新练习集名称，并提示将创建对应的目录 `[新练习集名称]/`。此名称将作为 `current_exercise_collection`。

---

## 第2阶段：创建练习practice描述 (`practice_xxx.md`) (Creating the Exercise practice Description)

**上下文**: 在"第1阶段"确定 `current_exercise_collection` 后执行。

**目标**: AI与用户交互收集信息，参照 `tdd_exercise_factory/practice_tdd_template.md` 生成结构化的"练习practice描述文件"。

**交互式practice构建 (Interactive practice Building):**

**AI**: "现在我们来定义练习practice的整体信息。"

1.  **practice识别信息 (practice Identification) - 交互式收集与确认:**
    *   AI引导用户提供并确认以下信息：
        *   **主题 (practice Theme) / 应用友好名称 (APP_FRIENDLY_NAME)** (例如：'BMI Calculator')。
        *   **应用核心名称 (APP_NAME)** (AI可基于主题建议snake_case形式，例如 'bmi_calculator'，并说明其对代码、测试和文档路径的影响)。
        *   **practice文件名 (practice Filename)** (AI可基于APP_NAME建议 `practice_tdd_[APP_NAME].md`)。
    *   AI在收集完上述三项后，会进行一次总体验证，确保信息准确无误，并允许用户修正。

2.  **核心练习系列规划与定义 (Core Exercise Series Planning & Definition) - 交互式迭代收集与确认:**
    *   AI引导用户首先提供 **特性ID前缀 (FEATURE_ID_PREFIX)** (例如 `BMI` 或 `AWA_CORE`)。
    *   然后，AI会逐个引导用户定义每个特性，收集并确认以下信息：
        *   **特性名称 (FEATURE_NAME_CAMELCASE)** (驼峰式命名，例如 `calculateBmi`)。
        *   **友好标题 (FEATURE_FRIENDLY_TITLE)** (例如 'Calculate BMI')。
        *   **用户故事 (USER_STORY)** (遵循标准格式)。
        *   **验收标准 (ACCEPTANCE_CRITERIA)** (Markdown列表格式)。
        *   **技术说明 (TECHNICAL_NOTES)** (可选)。
    *   每收集完一个特性的信息，AI会进行单特性确认。
    *   用户可以决定是否继续添加更多特性。
    *   所有特性定义完毕后，AI会进行一次包含所有特性信息的总体验证，允许用户指定修改。

3.  **可选内容收集 (Optional Content Collection) - 交互式收集:**
    *   AI告知用户可以补充可选的全局信息，用于填充模板中的占位符，用户可选择跳过。
    *   收集的信息点包括（但不限于，对应模板中的占位符）：
        *   是否系列练习 (`IS_SERIES_EXERCISE`), 系列ID (`SERIES_ID`), 系列友好名称 (`SERIES_FRIENDLY_NAME`)。
        *   系列练习的共享核心实现路径说明 (`MAIN_IMPLEMENTATION_PATH_INFO`)。
        *   额外的总体practice约束 (`ADDITIONAL_PRACTICE_CONSTRAINTS_PLACEHOLDER`)。
        *   工具包或共享库说明 (`OPTIONAL_TOOLKIT_DESCRIPTION_PLACEHOLDER`)。
        *   通用约束条件 (`OPTIONAL_GENERAL_CONSTRAINTS_PLACEHOLDER`)。
        *   建议学习顺序 (`OPTIONAL_LEARNING_ORDER_PLACEHOLDER`)。
        *   通用技术依赖 (`OPTIONAL_TECH_DEPENDENCIES_PLACEHOLDER`)。
        *   练习难度递进说明 (`OPTIONAL_DIFFICULTY_PROGRESSION_PLACEHOLDER`)。
    *   AI记录用户提供的各项可选信息。

4.  **AI生成`practice_xxx.md`文件 - AI执行与告知:**
    *   AI声明已收集所有必要信息，将根据这些信息和 `tdd_exercise_factory/practice_tdd_template.md` 模板生成 `[practice文件名]`。
    *   AI简述生成过程要点：
        1.  使用用户确认的识别信息和特性数据。
        2.  基于模板结构，填充所有占位符。
        3.  确保 `FEATURES` 数组格式正确，可选内容按用户输入填充，利用模板的条件渲染。
        4.  文件保存至 `[current_exercise_collection]/[practice文件名]`。
    *   AI执行生成，并告知用户结果和文件位置。

**AI生成`practice_xxx.md`的核心遵循原则 (AI's Core Principles for Generating `practice_xxx.md`):**

*   **输入源**: 用户交互确认的所有信息（核心识别信息、特性数组、可选说明等）。
*   **数据结构**: 传递给模板的数据结构需与 `practice_tdd_template.md` 的占位符和逻辑（如 `{{#each FEATURES}}`, `{{#if IS_SERIES_EXERCISE}}`）匹配。
*   **模板应用**: 严格使用 `tdd_exercise_factory/practice_tdd_template.md` 作为基础结构，正确填充所有占位符，包括 `{{USER_WORKSPACE_ROOT}}`，并确保特性ID和条件渲染正确处理。
*   **路径表示**: 生成的 `practice_xxx.md` 中，所有特性相关的代码、测试、文档路径均指向 `../{{APP_NAME}}` 项目的相应子目录，AI需确保 `APP_NAME` 和特性占位符正确替换。
*   **输出**: 用户确认的文件名，存放于 `[current_exercise_collection]/`。

---

## 第3阶段：初始化框架文档 (Initializing Framework Documents)

**上下文**: 在"第1阶段"确定 `current_exercise_collection` 后，通常在"第2阶段"生成一个或多个practice描述文件后执行。

**目标**: AI与用户交互，并可选创建练习集专属的规划与理念文档。

**交互式文档同步 (Interactive Document Sync):**
1.  AI询问用户是否要创建练习集专属的规划文档 (基于模板，可自定义文件名，AI可尝试初步内容适配)，用户确认后执行。
2.  AI询问用户是否要创建练习集专属的核心理念文档 (基于模板，可自定义文件名)，用户确认后执行。
3.  AI告知框架文档处理完毕。

---

## 总体交互流程概览 (Overall Interactive Workflow Overview)

1.  **AI开场**: 解释交互流程。
2.  **第1阶段 - 设定新练习集**: 确定要创建的新练习集信息。
3.  **第2阶段 - 创建练习practice描述 (`practice_xxx.md`)**: 交互式定义practice识别信息、特性（含ID前缀、名称、用户故事、验收标准等）、可选系列信息。AI基于 `practice_tdd_template.md` 生成文件。
4.  **第3阶段 - 初始化框架文档**: 同步通用教学框架模板，可选创建练习集专属规划与理念文档。

**最终目标**: 生成结构和内容符合预期的 `practice_xxx.md` 文件，指导TDD练习，确保遵循用户输入、模板和本指南，实现清晰一致。