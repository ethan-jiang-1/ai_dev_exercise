# AI协作生成复杂MDS练习框架指令

**重要说明：** 本文档描述了一个交互式、多步骤、有状态的AI协作流程。AI将引导用户逐步完成新MDS（Model-Driven Scenario）练习系列的创建，并在关键步骤进行信息确认。本文档的目标是生成一个基于 `exercise_md_template/story_complex_template.md` 的详细练习故事。

## 预备对话：AI向用户阐述流程

**AI开场白示例：**
"您好！今天我们将一起以交互方式创建一个新的、更复杂的MDS练习系列。这个过程会比之前的TDD练习创建更详尽，因为它涉及到定义更丰富的场景元素，如用户人设、多样化的数据输入、详细的用例步骤以及非功能性需求等。我将引导您分阶段完成信息收集，包括定义练习集、设定故事全局信息、构建核心角色、描述关键数据输入、逐个定义场景用例，并补充其他重要信息。在每个阶段，我会向您请求具体信息，并在继续之前与您确认我的理解，以确保我们高效地产出符合您期望的高质量练习。准备好开始了吗？"

## 第1阶段：设定练习集 (Setting up the Exercise Collection)
(此阶段与 `generate_tdd_exercise_instructions.md` 中的第1阶段基本一致，用于确定 `current_exercise_collection`)
1.  **AI**: "请问您希望：1. 在现有的练习集下工作？ 2. 创建一个新的练习集？"
2.  **用户**: (选择1或2)
3.  **AI**: (根据用户选择处理，记录 `current_exercise_collection`)

---

## 第2阶段：定义故事全局信息 (Defining Story Global Information)

**AI**: "现在我们来定义这个练习故事的全局信息，这些信息将构成故事的整体框架。"

1.  **故事识别与基础设定 (Story Identification & Basic Setup) - 交互式收集与确认:**
    *   **AI**: "这个练习故事的总体 **主题 (Story Theme)** 是什么？（例如：'医疗影像诊断API' 或 '金融交易风险评估系统'）"
    *   **用户**: `[提供故事主题]` (记录: `story_theme`)
    *   **AI**: "基于此主题，建议此故事的主要实现存放在名为 `mds_[主题的snake_case形式]` 的子目录中。您对 **主要实现目录建议名称 (Suggested Main Implementation Directory Name)** 有何想法？"
    *   **用户**: `[确认或提供自定义名称]` (记录: `main_implementation_dir`)
    *   **AI**: "建议故事文件名为 `story_[主题的snake_case形式].md`。您是否接受或有特定的 **故事文件名 (Story Filename)**？"
    *   **用户**: `[确认或提供自定义文件名]` (记录: `story_filename`)
    *   **AI (Verification)**: "总结一下故事识别信息：练习集名称为 `[current_exercise_collection]`，故事主题为 `[story_theme]`，主要实现目录为 `[main_implementation_dir]`，故事文件名为 `[story_filename]`。这些信息都正确吗？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应回溯并修正相应条目)

2.  **项目/产品愿景 (Project/Product Vision) - 对应模板中 `{{PROJECT_VISION_PLACEHOLDER}}`:**
    *   **AI**: "请描述这个练习希望模拟的 **项目或产品愿景 (Project/Product Vision)**。它旨在达成什么长远目标，或者为学习者提供一个怎样的宏大背景？"
    *   **用户**: `[提供项目愿景]`

3.  **核心挑战与目标 (Core Challenges & Objectives) - 对应模板中 `{{CORE_CHALLENGES_OBJECTIVES_PLACEHOLDER}}`:**
    *   **AI**: "这个练习中包含的 **核心挑战是什么？学习者通过完成此练习应掌握哪些核心技能或达成什么目标**？"
    *   **用户**: `[提供核心挑战与目标]`

4.  **目标学习者/用户 (Target Audience) - 对应模板中 `{{TARGET_AUDIENCE_PLACEHOLDER}}`:**
    *   **AI**: "这个练习主要面向 **哪些目标学习者或用户群体**？他们的背景和期望是怎样的？"
    *   **用户**: `[提供目标学习者描述]`

5.  **总体约束 (Overall Constraints) - 对应模板中 `{{ADDITIONAL_OVERALL_CONSTRAINTS_PLACEHOLDER}}`:**
    *   **AI**: "是否有需要一开始就明确的 **重要总体约束**？例如特定的技术栈限制、预算限制、时间限制或强制的合规性要求。请逐条提供，每条约束内容前会自动添加 '> '。如果暂时没有，可以回复'无'。"
    *   **用户**: `[提供约束列表，或"无"]`

---

## 第3阶段：构建核心角色/人设 (Defining Key Personas)

**AI**: "接下来，我们来定义这个故事场景中涉及的核心用户角色或人设 (Personas)。每个人设都将有其独特的目标和行为。对应模板中 `{{#each PERSONAS}}` 部分。"
**AI**: "您希望现在定义第一个人设吗？(是/否)"
**用户**: `[是]`

*   **(迭代开始 - 对于每个人设，AI记录序号 persona_index 从1开始)**
    *   **AI**: "请输入 **人设名称 (Persona Name)** (例如：'放射科医生张三', '风控分析师李四')。这是第 `[persona_index]` 个人设。"
    *   **用户**: `[提供人设名称]`
    *   **AI**: "请提供此人设的 **简介 (Description)**。"
    *   **用户**: `[提供简介]`
    *   **AI**: "此人设在场景中的 **主要目标 (Goals)** 是什么？"
    *   **用户**: `[提供主要目标]`
    *   **AI**: "为了达成目标，此人设通常会执行哪些 **关键任务 (Key Tasks)**？（请使用Markdown列表，例如：\n- 任务1\n- 任务2）"
    *   **用户**: `[提供关键任务列表]`
    *   **AI**: "此人设有哪些 **痛点或特定需求 (Pain Points/Needs)** 是这个练习场景试图解决或满足的？"
    *   **用户**: `[提供痛点/需求]`
    *   **AI (Verification per persona)**: "人设 `[persona_index]` (`[人设名称]`) 信息: \n  简介: `[简介]`\n  目标: `[目标]`\n  任务: `[任务]`\n  痛点: `[痛点]`。\n确认无误？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应允许用户指定哪个条目需要修改，并重新收集该条目信息)
    *   **AI**: "是否要添加另一个人设？(是/否)"
    *   **用户**: `[是/否]` (若是，则重复迭代，persona_index递增；若否，则结束人设定义)
*   **(迭代结束)**
**AI**: "人设定义完毕。如果后续发现需要调整或补充，我们随时可以回来修改。"

---

## 第4阶段：描述主要输入数据与环境 (Describing Key Inputs & Environment)

**AI**: "现在我们来明确这个练习场景所依赖的主要输入数据和整体环境配置。"

1.  **数据源 (Data Sources) - 对应模板中 `{{#each DATA_SOURCES}}`:**
    **AI**: "这个场景会用到哪些主要的数据源？请逐个提供。"
    **AI**: "您希望现在定义第一个数据源吗？(是/否)"
    **用户**: `[是]`
    *   **(迭代开始 - 对于每个数据源)**
        *   **AI**: "请输入 **数据源名称 (Data Source Name)** (例如：'患者影像数据集', '实时股票行情API')。"
        *   **用户**: `[提供数据源名称]`
        *   **AI**: "此数据源的 **类型/格式 (Type/Format)** 是什么？(例如：'DICOM文件集合', 'JSON API', 'CSV文件', 'PostgreSQL数据库')"
        *   **用户**: `[提供类型/格式]`
        *   **AI**: "请提供关于此数据源的 **简要描述、其在场景中的作用，或指向示例数据/文档的链接 (Description/Example Link)**。"
        *   **用户**: `[提供描述或链接]`
        *   **AI (Verification per data source)**: "数据源 (`[数据源名称]`) 信息: \n  类型/格式: `[类型/格式]`\n  描述/链接: `[描述/链接]`。\n确认无误？(是/否)"
        *   **用户**: `[是/否]`
        *   **AI**: "是否要添加另一个数据源？(是/否)"
        *   **用户**: `[是/否]` (若是，则重复迭代；若否，则结束数据源定义)
    *   **(迭代结束)**

2.  **技术栈与工具 (Tech Stack & Tools) - 对应模板中 `{{TECH_STACK_TOOLS_PLACEHOLDER}}`:**
    *   **AI**: "这个练习建议或强制使用哪些特定的 **技术栈、编程语言、框架或工具**？请以列表形式提供。"
    *   **用户**: `[提供技术栈和工具列表]`

3.  **环境配置要求 (Environment Setup) - 对应模板中 `{{ENVIRONMENT_SETUP_PLACEHOLDER}}`:**
    *   **AI**: "是否有推荐或必须的 **环境配置要求**？（例如：特定操作系统、Python版本、依赖库安装说明、虚拟机配置等）请详细说明。"
    *   **用户**: `[提供环境配置说明]`

---

## 第5阶段：逐个定义场景片段/核心用例 (Defining Scenario Segments / Core Use Cases)

**AI**: "这是核心部分。我们将把整个故事分解为若干个逻辑连贯的场景片段或核心用例 (Use Cases)。每个用例都将有其明确的目标、步骤和产出。对应模板中 `{{#each SCENARIO_SEGMENTS}}` 部分。"
**AI**: "在开始定义第一个用例前，请先思考：\n1. **总体蓝图**：整个故事如何通过这些用例串联起来？它们之间是否有依赖关系？\n2. **学习曲线**：用例的顺序是否能形成平滑的难度递进或知识构建路径？\n准备好后，我们开始定义第一个用例。"

**AI**: "您希望现在定义第一个核心用例吗？(是/否)"
**用户**: `[是]`

*   **(迭代开始 - 对于每个核心用例，AI记录序号 segment_index 从1开始)**
    *   **AI**: "请输入此用例的 **描述性名称 (CamelCase)**，例如 `ProcessNewReferral` 或 `GenerateRiskScore`。这将用于目录命名。这是第 `[segment_index]` 个用例。"
    *   **用户**: `[提供UseCaseNameCamelCase]` (记录: `segment_name_camelcase`)
    *   **AI**: "请输入此用例的 **口语化标题 (Friendly Title)**，这将用于章节标题，例如 '处理新的转诊请求' 或 '生成风险评分报告'。"
    *   **用户**: `[提供口语化标题]`
    *   **AI**: "此用例的 **核心用户/业务目标 (Core User/Business Goal)** 是什么？请从用户或业务价值角度描述。"
    *   **用户**: `[提供核心目标]`
    *   **AI**: "请选择 **涉及的主要人设 (Involved Personas)** (从第3阶段定义的人设列表中选择，可多选，用逗号分隔)。"
    *   **用户**: `[选择人设列表]`
    *   **AI**: "此用例的 **触发条件 (Triggers)** 是什么？什么事件或情况会启动这个用例？"
    *   **用户**: `[提供触发条件]`
    *   **AI**: "请详细描述此用例的 **主要步骤或交互流程 (Key Steps / Interaction Flow)**。建议使用Markdown列表格式 (每行以 '-' 或 '* ' 开头)。"
    *   **用户**: `[提供步骤列表]` (记录为 `segment_key_steps_markdown_list`)
    *   **AI**: "此用例的 **预期结果或主要产出物 (Expected Outcomes / Artifacts)** 是什么？(例如：'更新后的数据库记录', '生成的PDF报告', 'API成功响应码200并返回JSON数据')。建议使用Markdown列表格式，并指明产出物类型和大致内容/位置。"
    *   **用户**: `[提供预期结果列表]` (记录为 `segment_expected_outcomes_markdown_list`)
    *   **AI**: "此用例的 **关键验收标准 (Key Acceptance Criteria)** 是什么？如何判断这个用例被成功完成？建议使用Markdown列表格式。"
    *   **用户**: `[提供验收标准列表]` (记录为 `segment_acceptance_criteria_markdown_list`)
    *   **AI (Verification per use case)**: "用例 `[segment_index]` (`[segment_name_camelcase]`) 信息: \n  口语化标题: `[口语化标题]`\n  核心目标: `[核心目标]`\n  涉及人设: `[人设列表]`\n  触发条件: `[触发条件]`\n  主要步骤: \n`[步骤列表]`\n  预期结果: \n`[预期结果列表]`\n  验收标准: \n`[验收标准列表]`。\n确认无误？(是/否)"
    *   **用户**: `[是/否]` (如果不正确，AI应允许用户指定哪个条目需要修改，并重新收集该条目信息)
    *   **AI**: "是否要添加另一个核心用例？(是/否)"
    *   **用户**: `[是/否]` (若是，则重复迭代，segment_index递增；若否，则结束用例定义)
*   **(迭代结束)**

---

## 第6阶段：定义全局非功能性需求 (Defining Global Non-Functional Requirements - NFRs)

**AI**: "现在我们来考虑一些适用于整个练习场景的全局非功能性需求。如果某些NFR仅适用于特定用例，可以在该用例的约束中说明。对应模板中 `{{NFR_..._PLACEHOLDER}}` 系列占位符。如果某项不适用或暂无要求，可以回复'无'或跳过。"
*   **AI**: "关于 **性能 (Performance)** 有什么要求？ (例如：响应时间、并发用户数、吞吐量)"
*   **用户**: `[提供性能要求 或 无]`
*   **AI**: "关于 **安全 (Security)** 有什么要求？ (例如：数据加密、访问控制、认证机制)"
*   **用户**: `[提供安全要求 或 无]`
*   **AI**: "关于 **合规性 (Compliance)** 有什么要求？ (例如：HIPAA, GDPR, SOX)"
*   **用户**: `[提供合规性要求 或 无]`
*   **AI**: "关于 **可用性 (Usability)** 有什么要求？ (例如：易用性标准、无障碍访问)"
*   **用户**: `[提供可用性要求 或 无]`
*   **AI**: "关于 **可靠性 (Reliability)** 有什么要求？ (例如：平均无故障时间MTBF、错误恢复机制)"
*   **用户**: `[提供可靠性要求 或 无]`
*   **AI**: "关于 **可扩展性 (Scalability)** 有什么要求？ (例如：系统如何应对增长的用户量或数据量)"
*   **用户**: `[提供可扩展性要求 或 无]`
*   **AI**: "关于 **可维护性 (Maintainability)** 有什么要求？ (例如：代码规范、模块化程度、文档要求)"
*   **用户**: `[提供可维护性要求 或 无]`
*   **AI**: "是否还有其他重要的 **非功能性需求** 需要补充？（对应 `{{ADDITIONAL_NFRS_PLACEHOLDER}}`）"
*   **用户**: `[提供补充NFRs 或 无]`

---

## 第7阶段：补充可选信息 (Adding Optional Supplementary Information)

**AI**: "最后，我们可以为这个练习故事补充一些可选的全局信息。如果不需要某项，可以直接跳过或回复'无'。"
*   **AI**: "是否有建议的 **学习/执行顺序 (Suggested Learning/Execution Order)**？（对应 `{{OPTIONAL_LEARNING_ORDER_PLACEHOLDER}}`）"
*   **用户**: `[提供说明 或 无]`
*   **AI**: "是否有关于 **练习难度递进 (Difficulty Progression)** 的说明？（对应 `{{OPTIONAL_DIFFICULTY_PROGRESSION_PLACEHOLDER}}`）"
*   **用户**: `[提供说明 或 无]`
*   **AI**: "是否需要 **常见问题解答 (FAQ)**？（对应 `{{OPTIONAL_FAQ_PLACEHOLDER}}`）"
*   **用户**: `[提供FAQ内容 或 无]`
*   **AI**: "是否需要一个 **术语表 (Glossary)** 来解释特定领域的术语？（对应 `{{OPTIONAL_GLOSSARY_PLACEHOLDER}}`）"
*   **用户**: `[提供术语表内容 或 无]`

---

## 第8阶段：AI生成 `story_xxx.md` 文件

**AI**: "非常好！我已经收集了所有必要（及可选）的信息。现在我将根据这些信息，并严格参照 `exercise_md_template/story_complex_template.md` 的结构和占位符，来生成 `[故事文件名]` 文件。在生成过程中，我会确保：
    1.  所有您确认的信息都正确填充到对应的占位符。
    2.  对于迭代收集的部分 (人设、数据源、用例)，会按照 `{{#each ...}}` 的逻辑正确展开，并确保索引正确（例如 `{{PERSONA_INDEX}}`, `{{SEGMENT_INDEX_PADDED}}`）。
    3.  如果某可选部分没有提供内容，相应的占位符及其引导文本将被合理移除或标记为空 (例如，模板中 `{{NO_PERSONAS_DEFINED_PLACEHOLDER}}` 等占位符的处理)。
    4.  模板中的示例名称（如 `{{EXAMPLE_USECASE_NAME_SNAKECASE}}`）将根据实际用例或主题生成更具体的示例，或者使用一个通用的占位符名称。
    5.  用例的目录结构示意图会根据每个用例的名称 (`{{SEGMENT_NAME_CAMELCASE}}` 和 `{{SEGMENT_NAME_SNAKECASE}}`) 动态生成。
    6.  文件将保存在 `[current_exercise_collection]/[故事文件名]`。
    我现在开始生成，请稍候。"
*   **(AI执行文件生成)**
**AI**: "文件 `[故事文件名]` 已成功生成并存放在 `[current_exercise_collection]/` 目录下。强烈建议您仔细检查生成的内容，特别是各个用例的细节和整体流程的连贯性。由于场景复杂，可能需要进一步的手动调整和润色。"

---

## 第9阶段：初始化框架文档 (Initializing Framework Documents)
(此阶段与 `generate_tdd_exercise_instructions.md` 中的第3阶段类似，但使用的是 `exercise_md_template/teaching_framework/` 下的文件，如 `planning_mds_exercise_complex.md` 和 `thinking_driven_development_with_ai_complex.md`)
1.  **AI**: "最后，我们来处理 `[current_exercise_collection]` 练习集的教学框架文档。我会检查并确保核心框架文件已从主模板 (`exercise_md_template/teaching_framework/`) 同步到 `[current_exercise_collection]/teaching_framework/` 目录（如果目录或文件不存在，我会创建它们）。这些核心框架文件包括 `planning_mds_exercise_complex.md` 和 `thinking_driven_development_with_ai_complex.md`。是否继续？(是/否)"
2.  **用户**: `[是/否]`
3.  **AI**: (执行同步) "核心框架文件已同步。"
4.  **(可选)** AI引导用户创建此练习集专属的规划文档和理念文档（基于 `teaching_framework` 中的模板进行复制和重命名，例如命名为 `planning_this_collection.md` 或 `thinking_this_collection.md`）。

--- 