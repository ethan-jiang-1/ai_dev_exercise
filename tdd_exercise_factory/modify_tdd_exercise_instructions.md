<!-- 定义核心占位符 (供AI交互收集信息时参考，最终会映射到模板中的 {{placeholder}} ) -->
<!-- 
{{app_name}}: 项目/应用根目录名 (例如: "ai_wellness_advisor")。
{{module_name}}: {{app_name}} 内的模块名 (例如: "bmi", "wellness_profile")。
{{FeatureName}}: 驼峰式特性名 (例如: "BMICalculation", "ComprehensiveProfileModel")。
{{feature_name}}: 下划线式特性名 (例如: "bmi_calculation", "comprehensive_profile_model")。
{{NN}}: 特性两位数序号 (例如: "01", "02")。
{{current_exercise_collection}}: 当前操作的练习集目录名称 (例如: "exercise_tdd_llm", "exercise_tdd_awa_core")。
-->

# AI协作修改TDD练习框架指令
> 版本: 4.0

**核心目标：** 本文档指导AI通过与用户进行**交互式、多步骤、有状态的协作流程**，逐步修改或调整**现有**的TDD练习系列中的`practice_xxx.md`文件，并在关键步骤进行信息确认。

## 预备对话：AI向用户阐述修改流程

**AI开场白示例：**
"您好！今天我们将一起以交互方式修改一个现有的TDD练习。我将引导您完成几个主要阶段，包括定位您想修改的练习集和practice文件，然后逐项确认您希望调整的内容，最后更新对应的文件。准备好开始了吗？"

## 第1阶段：定位待修改的练习集与Practice (Locating the Exercise Collection and Practice to Modify)

**目标**: 明确用户希望修改的现有练习集及其中的具体 `practice_xxx.md` 文件。

**交互流程**:
1.  AI询问用户希望修改的**现有练习集名称** (例如 `exercise_tdd_llm`)。
2.  AI记录练习集名称 (`current_exercise_collection`)。
3.  AI尝试列出 `[current_exercise_collection]/` 目录下的 `practice_*.md` 文件，供用户选择。
    *   如果文件过多或不便列出，AI会请求用户直接提供**待修改的practice文件名** (例如 `practice_tdd_bmi_calculator.md`)。
4.  AI记录并与用户确认目标 `practice_xxx.md` 文件。

---

## 第2阶段：加载并展示Practice当前核心内容 (Loading and Presenting Current Practice Core Content)

**上下文**: 在"第1阶段"确定目标 `practice_xxx.md` 文件后执行。

**目标**: AI读取目标practice文件的核心内容，并向用户展示，以便用户明确修改的起点。

**交互流程**:
1.  AI告知用户将读取并分析选定的 `[practice文件名]`。
2.  AI读取文件内容，并向用户总结展示以下关键信息（如果存在）：
    *   当前的 **练习PRACTICE标题 (PRACTICE_TITLE)**。
    *   当前的 **练习总体用户故事 (PRACTICE_USER_STORY_MAIN_TITLE)**。
    *   当前的 **练习对应模块名 (MODULE_NAME)**。
    *   **特性列表** (FEATURE_ID_PREFIX, FEATURE_NAME_CAMELCASE, feature_name_snakecase, FEATURE_FRIENDLY_TITLE, user_story_for_feature, acceptance_criteria, important_notes_for_feature)。
    *   其他主要的可选全局信息摘要。
3.  AI询问用户是否确认基于这些信息进行修改。

---

## 第3阶段：交互式修改Practice内容 (Interactively Modifying Practice Content)

**上下文**: 在"第2阶段"用户确认当前practice内容后执行。

**目标**: AI与用户交互，逐项收集需要修改的信息，并实时确认。

**交互式修改流程**:

1.  **Practice识别信息修改 (Practice Identification Modification) - 交互式收集与确认:**
    *   AI询问用户是否需要修改以下信息，并逐项引导修改和确认：
        *   **练习PRACTICE标题 (PRACTICE_TITLE)**。
        *   **练习总体用户故事 (PRACTICE_USER_STORY_MAIN_TITLE)**。
        *   **练习对应模块名 (MODULE_NAME)** (AI提醒，若修改此项，可能影响关联路径和文件名，建议谨慎)。
        *   **(可选) Practice文件名 (Practice Filename)** (若MODULE_NAME更改，AI可建议新文件名)。
    *   AI在收集完修改后的上述信息（如果有修改）后，进行一次总体验证。

2.  **核心练习系列规划与定义修改 (Core Exercise Series Planning & Definition Modification) - 交互式迭代收集与确认:**
    *   AI询问用户是否需要修改 **特性ID前缀 (FEATURE_ID_PREFIX)**，并确认。
    *   AI展示现有特性列表，并询问用户希望进行的操作：
        *   **修改现有特性**: 用户选择特性，AI引导逐项修改（**特性名称 (FEATURE_NAME_CAMELCASE)**, **特性名 (feature_name_snakecase)**, **友好标题 (FEATURE_FRIENDLY_TITLE)**, **针对此特性的用户故事 (user_story_for_feature)**, **验收标准 (acceptance_criteria)**, **技术说明/重要提示 (important_notes_for_feature)**）。每次修改后单特性确认。
        *   **添加新特性**: AI引导用户定义新特性（同创建流程中的特性定义，参考 `generate_tdd_exercise_instructions.md`，包含FEATURE_NAME_CAMELCASE, feature_name_snakecase, FEATURE_FRIENDLY_TITLE, user_story_for_feature, acceptance_criteria, important_notes_for_feature）。
        *   **删除特性**: 用户选择特性，AI确认后标记为待删除。
    *   所有特性修改/添加/删除操作完毕后，AI会进行一次包含所有更新后特性信息的总体验证。

3.  **可选内容修改 (Optional Content Modification) - 交互式收集与确认:**
    *   AI询问用户是否需要修改或补充可选的全局信息。
    *   对已有的可选信息，AI可展示当前值并询问是否修改。
    *   对未填写的可选信息，AI可引导用户补充（同创建流程中的可选内容收集，参考 `generate_tdd_exercise_instructions.md`）。
    *   AI记录用户提供的各项修改或新增的可选信息。

---

## 第4阶段：AI更新`practice_xxx.md`文件 (AI Updates `practice_xxx.md` File)

**上下文**: 在"第3阶段"收集并确认所有修改后执行。

**目标**: AI根据用户确认的所有修改，更新目标`practice_xxx.md`文件。

**执行与告知**:
1.  AI声明已收集所有修改信息，将根据这些信息更新 `[current_exercise_collection]/[practice文件名]`。
2.  AI简述更新过程要点：
    *   基于用户确认的修改，调整原有内容。
    *   确保特性数组的增删改正确反映。
    *   可选内容按用户输入更新。
    *   文件将原地更新 (或者，如果文件名更改，则保存为新文件并提示用户旧文件处理方式)。
3.  AI执行更新，并告知用户结果。

---

## 第5阶段：(可选) 更新框架文档 (Optionally Updating Framework Documents)

**上下文**: 在"第4阶段"成功更新`practice_xxx.md`文件后执行。

**目标**: AI与用户交互，根据`practice_xxx.md`的修改，可选更新练习集专属的规划与理念文档。

**交互式文档同步**:
1.  AI询问用户，鉴于practice文件的修改，是否需要检查并更新练习集专属的规划文档。用户确认后，AI可引导进行相应调整（可能需要用户指明修改点）。
2.  AI询问用户是否需要检查并更新练习集专属的核心理念文档。用户确认后，AI可引导进行相应调整。
3.  AI告知框架文档处理完毕。

---

## 总体交互流程概览 (Overall Interactive Workflow Overview)

1.  **AI开场**: 解释修改流程。
2.  **第1阶段 - 定位练习集与Practice**: 确定待修改的练习集和`practice_xxx.md`文件。
3.  **第2阶段 - 加载并展示内容**: AI读取并展示practice核心信息。
4.  **第3阶段 - 交互式修改**: 逐项修改Practice识别信息、特性、可选内容。
5.  **第4阶段 - 更新文件**: AI根据修改更新`practice_xxx.md`。
6.  **第5阶段 - (可选) 更新框架文档**: 根据需要调整练习集专属规划与理念文档。

**最终目标**: 生成结构和内容符合用户修改预期的 `practice_xxx.md` 文件，确保修改准确反映。