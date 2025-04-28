# NovaBrain 3.0 模拟练习计划 测试与质量保障阶段

> **根目录说明**: 本练习计划中所有相对路径均以本文件所在目录 `exercise_full_m03/` 为根目录。例如，当看到 `./setting/` 时，实际指向的是 `exercise_full_m03/setting/` 目录。

## 模块目标与背景

**模块目标**：评估和体验 AI 助手（如 Cursor）在以下关键活动中的辅助能力：
- 辅助进行测试策略设计
- 测试用例生成与评审
- 自动化测试支持
- 缺陷预测与分析等活动
- 提升测试效率和产品质量

本模块使用 TechNova AI 案例作为模拟环境（已包含更新的外部设定）。

**与 LLM 的交互方式**：
- 所有输出应以中文为主；
- 推理过程可使用模型习惯语言（如英文）；
- 鼓励中文注释与中文命名。

**练习输出说明**：
- 所有练习产生的分析、草稿、日志、代码等，默认使用中文或包含中文注释，除非另有说明。

---

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
- `./module03/`

**输出目录**：
- 请依据每项练习中的指示进行输出，默认不在此处统一指定。

---

## 模块 03 练习: 测试与质量保障

### Ex3_0_SimpleFeedbackCategorize: 简单反馈分类 (入门)

*   **目标**: 练习使用 AI 阅读一份简化的用户反馈列表，并根据预设的简单类别（例如：UI 问题、功能错误、新功能建议）进行分类。这是处理和理解初步反馈的基础。
*   **理论/结构**: 信息分类与标记。步骤：提供反馈列表和分类规则 -> AI 读取并应用规则 -> AI 输出分类结果。
*   **输入**:
    *   `./module03/simple_feedback_list_v1.md`
*   **AI 助手角色**:
    *   读取反馈列表。
    *   根据用户提供的简单分类标准（比如"将反馈分为 UI 问题、功能错误、新功能建议三类"），对每条反馈进行标记。
    *   输出带有分类标记的反馈列表。
*   **复杂度分析**: 低。处理单一、简单的列表文件，任务是基本的文本分类，直接对应 M03 中更复杂的 UAT 反馈分析 (Ex3_1) 的初步环节。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_0_SimpleFeedbackCategorize/`
    *   **最终产物**: 一个 Markdown 文件，包含已分类的用户反馈列表，例如 `ex3_0_categorized_feedback_v1.md`。

### Ex3_0_SimpleTestCaseIdentify: 识别基本测试用例思路 (入门)

*   **目标**: 练习使用 AI 阅读一个简单的功能规约，并基于此识别出最基本的测试用例思路（例如，至少一个正向和一个负向场景）。
*   **理论/结构**: 测试设计基础 - 等价类划分与边界值思考的简化版。步骤：提供功能规约 -> AI 理解核心功能与约束 -> AI 提出正向/负向测试点子。
*   **输入**:
    *   `./module03/feature_spec_simple_math_func.md` (复用 M02 创建的简单函数规约)。
*   **AI 助手角色**:
    *   读取指定的功能规约 (`calculate_rectangle_area` 函数)。
    *   识别核心功能（计算面积）和关键约束（处理非正数输入）。
    *   提出至少一个正向测试场景的描述（例如："输入有效的正长度和宽度"）。
    *   提出至少一个负向或边界测试场景的描述（例如："输入零或负数作为长度/宽度"、"输入非数字字符"）。
*   **复杂度分析**: 低-中。处理单一、简单的规约文件，任务聚焦于从需求描述中推导出最基础的测试角度，为 Ex3_2 中更全面的测试用例生成打下基础。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_0_SimpleTestCaseIdentify/`
    *   **最终产物**: 一个 Markdown 文件，列出识别出的基本测试用例思路，例如 `ex3_0_basic_test_ideas_v1.md`。

### Ex3_0_SimpleTestTypeSuggest: 建议相关测试类型 (入门)

*   **目标**: 练习使用 AI 基于一个简单的功能描述和一个极简的测试类型列表，建议可能相关的 *其他* 测试类型。
*   **理论/结构**: 测试策略思考的雏形 - 理解不同测试类型的适用范围。步骤：提供功能描述和已知测试类型 -> AI 理解功能特点 -> AI 基于特点建议其他相关测试类型。
*   **输入**:
    *   `./module03/feature_spec_simple_math_func.md` (简单函数规约)。
    *   `./module03/minimal_test_types.md`
*   **AI 助手角色**:
    *   读取功能规约和极简测试类型列表。
    *   基于功能特点（例如，它是一个计算函数，有输入验证），建议 *可能* 相关的其他测试类型，并简要说明原因（例如："除了单元测试，考虑到输入验证，也许'边界值分析'这种测试技术也值得考虑？" 或 "如果这个函数会被大量调用，未来可能需要考虑'性能测试'？"）。重点是建议 *类型* 而非具体用例。
*   **复杂度分析**: 中。需要结合两个简单输入，进行初步的功能分析，并联想相关的测试 *类型*，比前两个练习需要更多一点"思考"，为 Ex3_3, Ex3_4 等测试策略和计划的制定提供入门视角。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_0_SimpleTestTypeSuggest/`
    *   **最终产物**: 一个 Markdown 文件，包含建议的其他相关测试类型及其简要理由，例如 `ex3_0_suggested_test_types_v1.md`。

### Ex3_1_UatAnalysis : UAT 反馈分析与优先级排序

*   **目标**: 处理 UAT 反馈摘要，对用户提出的问题进行分类、分析，并模拟产品和技术团队讨论修复优先级，**需考虑市场影响和特定行业的用户需求**。
*   **输入**: 
    *   `./setting/case_study_people_and_teams.md` (人物画像: 钱静, 王强, 周工, 陈浩; 团队动态)
    *   `./setting/setting_competitive_landscape.md`
    *   `./setting/setting_industry_adoption.md`
    *   `./module03/uat_feedback_summary_novabrain_pilot_v2.9.md` (UAT 反馈)
    *   `./module03/security_vulnerability_report_2024_01_10.md` (安全漏洞报告)
    *   `./module03/bug_report_example_model_accuracy_drop.md` (相关 Bug 报告)
*   **AI 助手 (Cursor) 的角色**:
    *   **反馈分类与聚合**: 将 UAT 反馈按模块、严重性、用户类型（**考虑行业属性**）进行分类和总结。
    *   **问题根源推测**: 结合其他文档（如安全报告、已知团队挑战、**行业特定问题**），推测某些 UAT 问题的潜在根源。
    *   **影响分析**: 分析不同问题对用户体验、核心功能、项目进度、安全性的影响，**并考虑竞争格局**。
    *   **优先级排序辅助**: 提供排序建议的框架（如结合严重性、影响范围、修复成本、**市场压力、行业关键需求**），辅助钱静和王强（角色扮演）进行决策。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_1_UatAnalysis/`
    *   **主要输出**: 练习中的反馈分类、根源推测、影响分析、优先级排序框架主要体现在**交互对话**记录中。
    *   **最终产物**: 最终的排序结果和决策依据（文件内容应为中文），可以整理后保存为日志文件 `exercise_3_1_uat_analysis_log.md`。

### Ex3_2_TestCaseGen : 测试用例生成与评审

*   **目标**: 基于现有测试用例和 API 变更，扩展测试覆盖面，并评审生成的用例，**确保覆盖相关技术趋势和特定行业的场景**。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (技术栈信息)
    *   `./setting/case_study_people_and_teams.md` (人物画像: QA 负责人周工, 前端负责人刘芳)
    *   `./setting/setting_technology_trends.md`
    *   `./setting/setting_industry_adoption.md`
    *   `./module03/test_case_draft_low_code_interface_v0.1.md` (低代码界面测试用例草稿)
    *   `./module03/api_changelog_lowcode_v0.1_to_v0.2.md` (API 变更日志)
*   **AI 助手 (Cursor) 的角色**:
    *   **用例生成**: 根据 API Changelog 或 PRD 需求，生成新的测试用例（正向、负向、边界），**需考虑新技术特性和行业特定工作流/数据（如 HIPAA 合规检查点）**。
    *   **用例评审**: 检查现有或新生成的测试用例是否覆盖了关键逻辑、边界条件、错误处理场景，**特别是涉及新技术和行业需求的场景**。
    *   **测试数据建议**: 为特定测试用例建议需要准备的测试数据，**考虑行业数据的特征**。
    *   **测试文档更新**: 协助周工（角色扮演）更新测试用例集文档。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_2_TestCaseGen/`
    *   **主要输出**: 练习中生成的测试用例、评审意见、测试数据建议主要体现在**交互对话**记录中。
    *   **最终产物**: 更新后的测试用例集（或新增部分，文件内容应为中文），建议保存为文件 `exercise_3_2_test_cases_update_draft_v1.md`。

### Ex3_3_AutomationStrategy : 自动化测试策略与实现

*   **目标**: 为 Low-Code 引擎和模型推理服务设计自动化测试策略，并模拟实现关键功能的自动化测试代码框架，**需考虑技术趋势和潜在的行业特定自动化需求**。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (技术栈信息)
    *   `./setting/case_study_people_and_teams.md` (人物画像: QA负责人周工, DevOps专家赵工)
    *   `./setting/setting_technology_trends.md`
    *   `./setting/setting_industry_adoption.md`
    *   `./module03/test_plan_lowcode_engine_v0.2.md` (测试计划)
    *   `./module03/test_cases_lowcode_api_v0.2.md` (测试用例)
    *   `./module03/qa_team_capabilities_assessment_202311.md` (QA团队能力评估)
    *   `./module03/api_design_review_lowcode_engine_v0.1.md` (API 设计)
*   **AI 助手 (Cursor) 的角色**:
    *   **测试可自动化程度评估**: 分析现有测试用例，评估哪些适合自动化，哪些需手动，**需考虑行业特定要求（如合规检查）是否适合自动化**。
    *   **自动化测试框架选型建议**: 基于技术栈和团队能力，推荐框架和工具，**需考虑对新技术（如 AI 模型测试）和行业特定场景的支持**。
    *   **测试脚本实现示例**: 为核心功能编写自动化测试脚本示例或框架，**可包含行业合规断言示例**。
    *   **CI/CD 集成方案设计**: 设计自动化测试如何集成到 CI/CD 流程，**考虑与技术趋势相关的最佳实践**。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_3_AutomationStrategy/`
    *   **主要输出**: 练习中的可自动化评估、框架选型建议、测试脚本示例和 CI/CD 集成方案主要体现在**交互对话**记录中。
    *   **最终产物**: 自动化测试策略和实现建议（文件内容应为中文，代码示例需包含中文注释），建议保存为文件 `exercise_3_3_automation_test_strategy_v1.md`。

### Ex3_4_PerformanceTest : 性能与负载测试设计

*   **目标**: 针对 NovaBrain 3.0 的模型推理服务和 Low-Code 引擎制定性能测试计划，并设计压力测试场景，**需反映真实的行业使用模式、竞争基准及技术趋势的潜在影响**。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (技术栈和系统组件)
    *   `./setting/case_study_people_and_teams.md` (人物画像: 工程负责人王强, QA负责人周工, SRE工程师赵工)
    *   `./setting/setting_industry_adoption.md`
    *   `./setting/setting_competitive_landscape.md`
    *   `./setting/setting_technology_trends.md`
    *   `./module03/performance_test_requirements_draft_v0.1.md` (性能测试需求草稿)
    *   `./module03/release_notes.md` (v3.0 发布说明，可能包含性能目标)
*   **AI 助手 (Cursor) 的角色**:
    *   **性能指标定义**: 明确关键性能指标，并设定合理目标值，**参考行业标准和竞品表现**。
    *   **测试场景设计**: 设计模拟真实负载的场景（常规、峰值、长时间），**需基于特定行业（MediScan/FinSecure）的用户行为模式**。
    *   **测试数据生成策略**: 提出生成和管理大量测试数据的策略，**确保数据能代表行业特征**。
    *   **性能瓶颈预测**: 基于系统架构、**技术趋势**和历史事件，预测瓶颈，设计针对性测试。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_4_PerformanceTest/`
    *   **主要输出**: 练习中的性能指标定义、测试场景设计、数据生成策略和瓶颈预测主要体现在**交互对话**记录中。
    *   **最终产物**: 性能测试计划和关键场景设计（文件内容应为中文），建议保存为文件 `exercise_3_4_performance_test_plan_v1.md`。

### Ex3_5_SecurityCompliance : 中国医疗法规合规性测试与安全评估

*   **目标**: 基于中国医疗器械软件监管要求和金融 (FinSecure) 与医疗 (MediScan) 行业客户需求，设计安全测试计划并进行合规性分析，**明确考虑中国特定行业法规（如NMPA、医疗器械软件分类管理办法）和数据安全法对医疗AI系统的监管要求**。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (客户案例: FinSecure, MediScan)
    *   `./setting/case_study_people_and_teams.md` (人物画像: QA负责人周工, 工程负责人王强, SRE工程师赵工, 数据科学家陈浩作为咨询)
    *   `./setting/setting_industry_adoption.md`
    *   `./setting/setting_technology_trends.md`
    *   `./module03/bug_report_example_model_accuracy_drop.md` (Bug 报告示例: 模型准确率下降)
    *   `./module03/china_medical_device_software_regulations_summary_202311.md` (中国医疗器械软件法规摘要)
    *   `./module03/security_vulnerability_report_2024_01_10.md` (最新安全漏洞报告)
    *   `./module03/security_audit_report_202311.md` (安全审计报告)
    *   `./module03/internal_memo_ai_ethics_guidelines_draft.md` (AI 伦理备忘录草稿)
*   **AI 助手 (Cursor) 的角色**:
    *   **中国合规要求解析**: 分析NMPA医疗器械软件监管要求、网络安全等级保护、数据安全法等对医疗AI系统的影响，**提取具体合规测试点**。
    *   **安全测试方法建议**: 针对不同监管要求，推荐符合中国标准的测试方法和工具，**关注医疗AI领域的特殊要求**。
    *   **合规要求与测试映射**: 将中国医疗法规要求（如软件分类管理、备案流程、数据本地化等）**明确地**映射到具体测试项目。
    *   **风险缓解建议**: 基于测试结果，提出符合中国监管环境的风险缓解策略和优先级，**结合国内医疗行业现状**。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_5_SecurityCompliance/`
    *   **主要输出**: 练习中的中国合规要求解析、测试方法建议、合规映射和风险缓解建议主要体现在**交互对话**记录中。
    *   **最终产物**: 中国医疗法规合规性测试计划和安全评估报告（文件内容应为中文），建议保存为文件 `exercise_3_5_security_compliance_plan_v1.md`。

### Ex3_6_TestEnvData : 测试环境管理与测试数据准备

*   **目标**: 设计测试环境策略和测试数据管理计划，解决 Sprint 回顾中的环境不稳定问题，**确保符合行业数据隐私规定并利用现代基础设施趋势**。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (技术栈和系统组件)
    *   `./setting/case_study_people_and_teams.md` (人物画像: 周工, DevOps专家赵工)
    *   `./setting/setting_industry_adoption.md`
    *   `./setting/setting_technology_trends.md`
    *   `./module04/deployment_strategy_novabrain_v3.md` (部署策略, 注意来自Module04)
    *   `./module03/test_data_current_status_202311.md` (现有测试数据状况)
    *   `./module03/deployment_checklist_v1.md` (部署检查清单)
    *   `./module03/sprint_retrospective_notes_2023_11_15.md` (Sprint 回顾中的环境问题)
*   **AI 助手 (Cursor) 的角色**:
    *   **环境配置管理建议**: 针对环境不稳定，提出改进建议，如 IaC、容器化，**参考技术趋势中的最佳实践**。
    *   **测试数据生成与管理策略**: 设计数据生成、维护、版本控制策略，**需强调符合行业隐私规定（HIPAA, GDPR）**。
    *   **环境分离与隔离方案**: 提出开发、测试、预生产、生产环境分离方案，明确配置差异和同步机制。
    *   **数据脱敏与安全处理建议**: 针对敏感测试数据，提出脱敏和安全处理方案，**需依据行业合规要求**。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_6_TestEnvData/`
    *   **主要输出**: 练习中的环境管理建议、数据策略、环境分离方案和安全处理建议主要体现在**交互对话**记录中。
    *   **最终产物**: 测试环境和数据管理计划（文件内容应为中文），建议保存为文件 `exercise_3_6_test_env_data_management_plan_v1.md`。

### Ex3_7_TDD_CI_Integration : TDD 与 CI 集成实践

*   **目标**: 通过实践练习理解测试驱动开发（TDD）与持续集成（CI）的结合点，探索"红-绿-重构"工作流在团队协作环境中的实现方式，**特别关注医疗数据验证场景下的特殊需求**。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (技术栈信息)
    *   `./setting/case_study_people_and_teams.md` (人物画像: QA负责人周工, DevOps专家赵工)
    *   `./setting/setting_technology_trends.md`
    *   `./module03/qa_team_capabilities_assessment_202311.md` (QA团队能力评估)
    *   `./module03/tdd_example_code.py` (TDD示例代码)
    *   `./module03/tdd_example_code_java.java` (TDD示例代码Java版本)
*   **AI 助手 (Cursor) 的角色**:
    *   **TDD实践练习设计**: 设计一系列实操练习，帮助团队成员理解和体验TDD流程与CI的结合方式。
    *   **工具选型与配置建议**: 为TDD流程自动化和可视化推荐工具和配置方案，**考虑团队现有技术栈和能力水平**。
    *   **医疗场景特殊测试设计**: 为医疗数据验证场景设计符合行业要求的TDD实践模式，**关注合规性和数据敏感性**。
    *   **团队协作流程设计**: 设计团队如何围绕TDD与CI协同工作的流程，模拟团队成员间的协作方式。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_7_TDD_CI_Integration/`
    *   **主要输出**: 练习中的TDD实践练习设计、工具选型、医疗场景特殊测试设计和团队协作流程设计主要体现在**交互对话**记录中。
    *   **最终产物**: TDD与CI集成实践练习指南（文件内容应为中文），建议保存为文件 `exercise_3_7_tdd_ci_practice.md`，以及完成练习后基于实践经验形成的TDD-CI集成方案（文件内容应为中文），建议保存为文件 `exercise_3_7_tdd_ci_integration_plan_v1.md`。

### Ex3_8_CICD_Pipeline : 医疗AI系统的CI/CD管道设计与实践

*   **目标**: 设计适合医疗AI系统的CI/CD管道，探索符合行业合规要求的自动化部署流程，**重点关注变更验证、灰度发布、回滚策略和审计跟踪**，解决传统CI/CD在医疗关键系统中的应用难题。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (技术栈和系统组件)
    *   `./setting/case_study_people_and_teams.md` (人物画像: DevOps专家赵工, 工程负责人王强或CTO张弓, QA负责人周工, CTO张弓)
    *   `./setting/setting_industry_adoption.md` (医疗行业特定要求)
    *   `./setting/setting_technology_trends.md` (DevOps最新趋势)
    *   `./setting/setting_competitive_landscape.md` (竞争对手的发布周期)
    *   `./module04/deployment_strategy_novabrain_v3.md` (部署策略, 注意来自Module04)
    *   `./module03/current_release_process_202311.md` (当前发布流程文档)
    *   `./module03/deployment_checklist_v1.md` (部署检查清单)
    *   `./module03/release_notes.md` (v3.0 发布说明)
    *   `./module03/sprint_retrospective_notes_2023_11_15.md` (Sprint回顾中的部署问题)
*   **AI 助手 (Cursor) 的角色**:
    *   **当前部署流程分析**: 分析团队现有部署实践中的痛点和风险，**特别关注医疗系统特有的挑战**，如合规审核、变更验证等。
    *   **CI/CD流程设计**: 设计适合医疗AI系统的CI/CD流程图和阶段定义，**包含必要的合规检查点、审批流程和验证步骤**。
    *   **灰度发布与回滚策略**: 设计适合医疗系统的灰度发布模式和应急回滚机制，**确保服务可靠性和数据一致性**。
    *   **自动化脚本示例**: 提供关键步骤的自动化脚本示例（如部署脚本、验证脚本、回滚脚本），**关注医疗特定场景**。
    *   **合规与审计支持**: 设计CI/CD流程中的合规检查点和审计日志方案，**满足医疗行业的监管要求**。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_8_CICD_Pipeline/`
    *   **主要输出**: 练习中的部署流程分析、CI/CD流程设计、灰度发布与回滚策略、自动化脚本示例和合规审计支持设计主要体现在**交互对话**记录中。
    *   **最终产物**: 
        * CI/CD部署实践练习指南（文件内容应为中文），建议保存为文件 `exercise_3_8_cicd_practice.md`
        * 完整的医疗AI系统CI/CD管道设计方案（文件内容应为中文，包含流程图和关键脚本示例），建议保存为文件 `exercise_3_8_cicd_pipeline_design_v1.md`

### Ex3_9_ChineseMedicalNLP : 中文医疗自然语言处理测试

*   **目标**: 设计和实施中文医疗自然语言处理能力的测试方案，验证系统对中文医学术语、病历文本、医嘱和诊断报告的理解和处理能力，**特别关注中文医学词汇的特殊性和中文表达习惯**。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (系统架构和NLP组件)
    *   `./setting/case_study_people_and_teams.md` (人物画像: 数据科学家陈浩, 相关临床专家顾问)
    *   `./setting/setting_industry_adoption.md` (中国医院信息化现状)
    *   `./setting/setting_technology_trends.md` (NLP技术趋势)
    *   `./module03/chinese_medical_corpus_sample.md` (中文医学语料样本)
    *   `./module03/medical_nlp_requirements_spec_v1.md` (医疗NLP需求规格)
*   **AI 助手 (Cursor) 的角色**:
    *   **中文医学语料特点分析**: 分析中文医学术语、病历书写习惯的特点，**明确中文医疗NLP的挑战点**。
    *   **测试数据集设计**: 设计多层次的中文医疗测试语料集，覆盖不同专科、不同难度的医疗文本，**关注中西医结合的表述特点**。
    *   **评估指标体系建立**: 建立适合中文医疗NLP的评估指标体系，**包括准确率、召回率、F1值和特定医学概念提取能力**。
    *   **测试自动化实现**: 设计中文医疗NLP自动化测试框架，**建议测试工具和方法**。
    *   **临床验证方案**: 设计与医生协作的临床验证方案，**评估系统理解中文医学表达的实际效果**。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_9_ChineseMedicalNLP/`
    *   **主要输出**: 练习中的中文医学语料分析、测试数据集设计、评估指标体系、自动化测试框架和临床验证方案主要体现在**交互对话**记录中。
    *   **最终产物**: 中文医疗NLP测试方案（文件内容应为中文，包含测试数据样例和评估指标），建议保存为文件 `exercise_3_9_chinese_medical_nlp_test_plan_v1.md`。

### Ex3_10_RegionalInterconnection : 区域医疗互联互通测试

*   **目标**: 设计验证NovaBrain 3.0在中国区域医疗协同场景下的互联互通能力测试方案，评估系统与不同医院信息系统、区域平台的数据交换和业务流程协同能力，**特别关注中国特色的分级诊疗、远程会诊等协作场景**。
*   **输入**: 
    *   `./setting/case_study_NovaBrain.md` (系统架构和集成能力)
    *   `./setting/case_study_people_and_teams.md` (人物画像: 工程负责人王强或CTO张弓, 模拟的外部合作方/医院代表)
    *   `./setting/setting_industry_adoption.md` (中国区域医疗现状)
    *   `./module03/regional_health_platform_requirements_v1.md` (区域医疗平台需求)
    *   `./module03/health_information_exchange_standards_v1.1.md` (医疗信息交换标准)
    *   `./module03/api_design_review_lowcode_engine_v0.1.md` (API设计)
*   **AI 助手 (Cursor) 的角色**:
    *   **互联互通需求分析**: 分析中国区域医疗场景下的互联互通需求，**明确分级诊疗、双向转诊、远程会诊等特色业务场景**。
    *   **测试环境设计**: 设计模拟多家医院和区域平台的测试环境，**包括常见的HIS、EMR、PACS等系统**。
    *   **接口测试用例生成**: 基于中国卫健委相关标准，生成数据交换接口测试用例，**验证系统符合国家医疗数据交换规范**。
    *   **业务流程测试设计**: 设计覆盖完整诊疗流程的端到端测试场景，**验证跨机构业务协同能力**。
    *   **性能与可靠性测试**: 针对区域平台高并发场景，设计性能测试方案，**确保在中国医疗实际负载下的系统稳定性**。
*   **输出位置与方式**:
    *   **输出目录**: `./output_module03/Ex3_10_RegionalInterconnection/`
    *   **主要输出**: 练习中的互联互通需求分析、测试环境设计、接口测试用例、业务流程测试设计和性能测试方案主要体现在**交互对话**记录中。
    *   **最终产物**: 区域医疗互联互通测试方案（文件内容应为中文，包含测试环境拓扑图和关键测试场景），建议保存为文件 `exercise_3_10_regional_interconnection_test_plan_v1.md`。

--- 