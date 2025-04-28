# NovaBrain 3.0 模拟练习计划 项目立项与需求设计阶段

> **根目录说明**: 本练习计划中所有相对路径均以本文件所在目录 `exercise_full_m01/` 为根目录。例如，当看到 `./setting/` 时，实际指向的是 `exercise_full_m01/setting/` 目录。

## 模块目标与背景

**模块目标**：评估和体验 AI 助手（如 Cursor）在以下关键活动中的辅助能力：
- 商业价值评估
- 需求挖掘与分析
- 风险预测
- 可行性验证
- 资源估算

本模块使用 TechNova AI 案例作为模拟环境（已包含更新的外部设定）。

**与 LLM 的交互方式**：
- 所有输出应以中文为主；
- 推理过程可使用模型习惯语言（如英文）；
- 鼓励中文注释与中文命名。

**练习输出说明**：
- 所有练习产生的分析、草稿、日志、代码等，默认使用中文或包含中文注释，除非另有说明。

----

## 熟悉目标所需阅读材料

**案例背景**：
- `case_study_NovaBrain.md`：核心背景、项目挑战、技术栈等。

**角色与团队**：
- `case_study_people_and_teams.md`：角色画像、团队动态与决策风格。

**外部环境设定**：
- `setting_competitive_landscape.md`
- `setting_industry_adoption.md`
- `setting_technology_trends.md`

---

## 输入与输出目录说明

**输入目录**：
- `./setting/`
- `./module01/`

**输出目录**：
- 请依据每项练习中的指示进行输出，默认不在此处统一指定。

---

## 模块 01  练习: 项目立项与需求设计

### an: 从PRD提取和结构化关键功能 (入门)

*   **目标**: 练习使用 AI 从单个 PRD 片段中准确提取核心功能需求，并将其结构化展示。
*   **理论/结构**: 这是需求文档分析的基础，重点在于信息识别和格式化。步骤：阅读文档 -> 识别关键功能描述 -> 按要求格式化输出。
*   **输入**:
    *   `./module01/prd_snippet_multimodal_fusion_v0.1.md`
*   **AI 助手角色**:
    *   读取指定的 PRD 片段。
    *   识别文档中描述的核心功能点或用户故事。
    *   将这些功能点以清晰的结构化列表（例如，使用 Markdown 的项目符号列表）呈现出来，每个功能点作为列表中的一项。
*   **复杂度分析**: 低。处理单一、聚焦的文档（PRD），任务是直接的信息提取和简单的格式化，非常适合作为第一个练习。与模块主题（需求设计）紧密相关。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module01/Ex1_0_SimplePrdFeatures/`
    *   **最终产物**: 一个 Markdown 文件，包含从 PRD 中提取并用列表格式化的功能点，例如 `ex1_0_prd_features_list_v1.md`。

### Ex1_0_SimpleRoadmapSalesCompare: 对比路线图与销售宣传的关键信息 (入门)

*   **目标**: 练习使用 AI 对比两个不同文档（项目路线图片段和销售宣传材料片段），找出其中的共同点和潜在差异点。
*   **理论/结构**: 跨文档信息比对，是验证信息一致性的基础步骤。步骤：分别阅读文档 -> 提取关键信息点 -> 对比异同 -> 总结发现。
*   **输入**:
    *   `./module01/project_roadmap_snippet_novabrain_v3_2023_h2.md`
    *   `./module01/sales_pitch_deck_snippet_novabrain_v3.md`
*   **AI 助手角色**:
    *   阅读项目路线图片段和销售演示文稿片段。
    *   分别从两个文档中提取关于 NovaBrain 3.0 的关键特性、目标或价值主张。
    *   对比提取出的信息，总结：
        *   两个文档都强调的核心特性或价值点有哪些？
        *   是否存在路线图中提到但销售材料未突出（反之亦然）的关键点？
*   **复杂度分析**: 低-中。需要处理两个文档，进行信息提取和基础比较，涉及到简单的信息综合能力。考察 AI 是否能抓住不同文档中的核心信息并进行对比。与模块主题（项目立项、价值定位）相关。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module01/Ex1_0_SimpleRoadmapSalesCompare/`
    *   **最终产物**: 一个 Markdown 文件，简要总结路线图和销售材料的关键信息对比结果，例如 `ex1_0_roadmap_sales_comparison_summary_v1.md`。

### Ex1_0_SimpleFeedbackToAction: 从用户反馈和技术文档提炼改进点 (入门)

*   **目标**: 练习使用 AI 从多个来源（用户反馈、技术白皮书、产品回顾）提取信息，并初步综合，提出针对性的产品或技术改进建议点。
*   **理论/结构**: 多源信息综合，是形成初步行动项或假设的基础。步骤：阅读多个文档 -> 分别提取关键洞察（用户痛点、技术方向、历史教训） -> 结合信息提出改进建议。
*   **输入**:
    *   `./module01/user_feedback_2024.md`
    *   `./module01/technical_whitepaper_2024.md`
    *   `./module01/product_retro_meeting_notes_v2_to_v3.md`
*   **AI 助手角色**:
    *   阅读用户反馈、技术白皮书和 V2 到 V3 的产品回顾会议纪要。
    *   从用户反馈中识别 1-2 个突出的痛点或需求。
    *   从技术白皮书中了解相关的技术方向或能力。
    *   从回顾纪要中了解过去的经验教训或改进动力。
    *   结合这三方面的信息，提出 1-2 个具体的、可操作的产品功能改进建议或技术调查方向，并简要说明理由（例如："鉴于用户反馈中提到的 X 问题，结合白皮书中提到的 Y 技术，并考虑到上次回顾中关于 Z 的教训，建议我们探索..."）。
*   **复杂度分析**: 中。需要处理三个不同类型的文档，提取关键信息并进行初步的综合与推理，以提出建议。比前两个练习更需要 AI 的"思考"能力，但仍然聚焦于信息整合而非深度战略分析。与模块主题（需求挖掘、可行性、持续改进）相关。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module01/Ex1_0_SimpleFeedbackToAction/`
    *   **最终产物**: 一个 Markdown 文件，包含 1-2 个基于三份文档信息综合得出的改进建议点及其简要理由，例如 `ex1_0_feedback_improvement_points_v1.md`。

### Ex1_1_PriorityDecision : 功能优先级与决策模拟

*   **目标**: 模拟在 CEO (李明宇) 强调快速市场占领 (Low-Code) 与 CTO (张弓) 关注长期架构/基础 (MLOps) 之间的早期功能优先级决策会议，并考虑关键的竞争压力、市场需求和技术趋势。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (主案例 M01 挑战)
    *   `./setting/case_study_people_and_teams.md` (人物画像: CEO, CTO, 产品负责人钱静; 团队动态: 产品 vs 技术冲突)
    *   `./setting/setting_competitive_landscape.md`
    *   `./setting/setting_industry_adoption.md`
    *   `./setting/setting_technology_trends.md`
    *   `./module01/project_roadmap_snippet_novabrain_v3_2023_h2.md` (项目路线图片段)
    *   `./module01/sales_pitch_deck_snippet_novabrain_v3.md` (销售演示文稿片段)
*   **AI 助手 (Cursor) 的角色**:
    *   **信息整合**: 快速总结各方（CEO, CTO, 产品）的主要诉求和依据。
    *   **论点生成**: 基于人物画像，并明确引入来自设定文件（竞争、技术、行业）的外部论据来支持不同观点，分别草拟支持优先开发 Low-Code 或 MLOps 基础的论点。
    *   **风险分析**: 分析两种不同优先级策略可能带来的短期和长期风险，需结合外部环境（如竞争对手反应、技术过时风险）。
    *   **会议纪要草拟**: 模拟记录会议讨论要点和最终（假设的）决策。
    *   **(可选) 模拟外部事件**: 在讨论中引入模拟的突发外部信息（如竞争对手行动），观察其对决策的影响。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module01/Ex1_1_PriorityDecision/`
    *   **主要输出**: 练习中的信息整合、论点生成、风险分析结果主要体现在交互对话记录中。
    *   **最终产物**: 模拟的会议纪要草稿（文件内容应为中文），建议保存为文件 `exercise_1_1_priority_meeting_minutes_draft_v1.md`。

### Ex1_2_PrdRequirements : PRD 深化与需求挖掘 (**聚焦医疗场景**)

*   **目标**: 基于已聚焦于**医疗影像与文本融合**的 PRD 片段，进一步挖掘和细化需求，特别是结合 **MediScan 客户案例**和相关行业及技术背景。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (**注意：本次练习仅关注此文件中的 MediScan 案例部分**)
    *   `./setting/case_study_people_and_teams.md` (人物画像: 产品负责人钱静, 内部数据科学家陈浩)
    *   `./setting/setting_industry_adoption.md`
    *   `./setting/setting_technology_trends.md`
    *   `./setting/setting_competitive_landscape.md`
    *   `./module01/mrd_multimodal_fusion_v0.1_zh.md` (MRD 片段: 多模态融合 - **医疗影像与报告** v0.1)
    *   `./module01/prd_snippet_multimodal_fusion_v0.1.md` (PRD 片段: 多模态融合 - **医疗影像与文本** v0.1)
*   **AI 助手 (Cursor) 的角色**: 
    *   **用户故事扩展**: 基于 **MediScan** 的需求，生成更具体的多模态用户故事（**仅限医疗场景**）。
    *   **非功能需求深化**: 基于 setting 文件（特别是行业和技术趋势）深化非功能性需求（**重点关注医疗场景下的高可靠性、HIPAA 合规性、数据隐私保护策略、模型可解释性要求等**）。
    *   **技术可行性与挑战提示**: 基于技术趋势提示**医疗影像与文本**多模态融合（特别是涉及敏感数据时）可能的技术挑战（如 LLM 可靠性、联邦学习效率、XAI 实现难度）或不同的实现路径。
    *   **需求澄清**: 模拟向内部数据科学家 (陈浩) 提问，以澄清与**医疗场景相关的**模糊技术需求或使用场景。
    *   **PRD 更新草拟**: 协助钱静（角色扮演）更新 PRD 文档，加入新的用户故事和需求点（**聚焦医疗场景**）。
*   **输出位置与方式**: 
    *   **输出目录**: `./output_module01/Ex1_2_PrdRequirements/`
    *   **主要输出**: 练习中的用户故事扩展、非功能需求建议、需求澄清问题主要体现在交互对话记录中。
    *   **最终产物**: 更新后的 PRD 草稿（或相关片段，文件内容应为中文，**仅包含医疗场景需求**），建议保存为文件 `exercise_1_2_prd_medical_update_draft_v1.md`。

### Ex1_3_MarketAnalysis : 市场与竞品情报分析

*   **目标**: 模拟利用 AI 助手快速分析全面的市场、竞争和技术环境，为 NovaBrain 3.0 的功能规划和市场定位提供情报支持。
*   **输入**:
    *   `./setting/case_study_NovaBrain.md` (主案例 M01)
    *   `./setting/setting_competitive_landscape.md`
    *   `./setting/setting_industry_adoption.md`
    *   `./setting/setting_technology_trends.md`
    *   (可选) `./module01/ai_market_research_2024.md` (补充)
    *   (可选) `./module01/competitor_analysis_summary_2024_q1.md` (补充)
    *   (可选) 利用 Cursor 的 `@web` 功能搜索最新的 AI 平台行业新闻或特定竞品信息。
*   **AI 助手 (Cursor) 的角色**:
    *   **设定文件解读**: 深入理解并整合 setting 文件提供的多维度信息。
    *   **信息提取与总结**: 从设定文件或网页中提取关键信息（如特定对手策略、行业痛点、关键技术机遇）。
    *   **趋势与模式识别**: 结合多份材料，识别市场机会、竞争威胁、技术应用模式。
    *   **SWOT 分析辅助**: 基于更全面的 setting 文件，协助产品负责人（钱静）或 CEO（李明宇）草拟 NovaBrain 3.0 相对于市场的初步 SWOT 分析。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module01/Ex1_3_MarketAnalysis/`
    *   **主要输出**: 练习中的报告总结、信息提取、趋势识别结果主要体现在交互对话记录中。
    *   **最终产物**: 市场与竞品分析的关键洞察摘要或初步的 SWOT 分析草稿（文件内容应为中文），建议保存为文件 `exercise_1_3_market_competitive_analysis_summary_v1.md`。

### Ex1_4_RiskBrainstorming : 全方位风险头脑风暴与分类

*   **目标**: 模拟在项目早期，利用 AI 助手引导进行更全面的风险识别，超越优先级冲突，充分考虑外部环境带来的技术、市场、合规、伦理等多维度风险。
*   **输入**:
    *   `./setting/case_study_NovaBrain.md` (主案例 M01 挑战, 技术栈)
    *   `./setting/case_study_people_and_teams.md` (人物画像，团队动态中的潜在冲突点或技能短板)
    *   `./setting/setting_competitive_landscape.md`
    *   `./setting/setting_industry_adoption.md`
    *   `./setting/setting_technology_trends.md`
    *   `./module01/prd_snippet_multimodal_fusion_v0.1.md` (初步需求，暗示技术复杂度)
    *   `./module01/technical_whitepaper_2024.md` (平台技术方向)
*   **AI 助手 (Cursor) 的角色**:
    *   **风险提示 (基于设定)**: 明确基于新的 setting 文件（竞争、行业、技术）提示常见的相关风险领域和具体风险点。
    *   **引导提问 (基于设定)**: 提出更具针对性的引导性问题，例如："考虑到 Horizon AI 的技术优势和潜在的降维打击，我们最大的技术路线风险是什么？" "医疗行业对数据隐私和 HIPAA 合规的严格要求，给我们的联邦学习和多模态功能带来哪些具体的合规及实施风险？" "LLM 技术的幻觉问题和 XAI 的不成熟性，可能给产品的市场信任度带来哪些风险？"
    *   **风险分类**: 对头脑风暴产生的风险点进行初步的分类（如按技术、市场、资源、外部依赖、合规、伦理等）。
    *   **结构化记录**: 将识别和分类的风险结构化地记录下来。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module01/Ex1_4_RiskBrainstorming/`
    *   **主要输出**: 练习中的风险提示、引导提问、分类讨论主要体现在交互对话记录中。
    *   **最终产物**: 初步的、分类结构化的风险列表 (Risk Register，文件内容应为中文)，建议保存为文件 `exercise_1_4_initial_risk_register_draft_v1.md`。

--- 