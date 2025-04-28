# User Story: Financial Risk Assessment System - part 4

(参考核心开发理念：[思考驱动开发与AI协作](teaching_framework/thinking_driven_development_with_ai.md))
> **实现目录说明**：本练习的实际实现位于 `./exercise_md_fr/` 目录下。

## 1. User Story (用户故事)

# 金融风险评估平台：AI+Markdown练习故事实例

> **重要约束**：在整个故事实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。


本文档描述了"金融风险评估平台"的故事实例的背景、业务场景和相关资料，用于支持AI+Markdown练习框架。本故事聚焦于一个面向金融机构的风险评估平台的开发和部署场景。

## 故事背景

"FinSecure"是一家专注于金融科技的创新公司，正在开发下一代金融风险评估平台，该平台将提供实时交易分析、欺诈检测、信用风险评估和监管合规验证。这个平台将服务于各种规模的银行、金融科技公司和金融机构，帮助它们在满足日益严格的监管要求的同时，实现风险评估流程的现代化。

## 业务目标

1. 实时检测潜在欺诈（处理时间低于100毫秒）
2. 提供比传统模型更高准确度的信用风险评估
3. 确保符合GDPR、PSD2和反洗钱指令等法规
4. 提供可解释的AI洞察，满足监管透明度要求
5. 扩展支持每小时处理数百万笔交易

## 团队角色

- **产品经理 (Sarah Chen)**: 负责平台需求定义、路线图规划和跨团队协调
- **首席架构师 (David Lee)**: 负责整体系统架构设计，确保满足性能、安全和可扩展性要求
- **数据科学负责人 (Maria Garcia)**: 领导风险模型的设计、训练和评估
- **后端工程负责人 (Raj Patel)**: 管理核心处理引擎、API和集成的开发
- **安全架构师 (Kevin White)**: 负责设计和实施平台的安全框架
- **合规官 (Emily Jones)**: 确保平台设计和运营符合所有相关金融法规
- **DevOps工程师 (Michael Brown)**: 负责CI/CD、部署、监控和基础设施管理
- **后端工程师 (Alex Zhang)**: 负责风险评估系统核心功能实现
- **你**: 作为Scrum Master，负责协调团队工作，确保项目顺利进行，解决团队遇到的问题和困惑，调查系统疑点

## 技术栈

- **后端**: Java/Kotlin/Go (高性能场景), Python (模型服务)
- **框架**: Spring Boot, FastAPI, gRPC
- **数据处理**: Apache Kafka, Apache Flink/Spark Streaming
- **数据库**: PostgreSQL/Oracle/SQL Server (客户选项), Cassandra/ScyllaDB (高性能存储), Redis (缓存)
- **机器学习**: Python, Scikit-learn, TensorFlow/PyTorch, MLflow
- **部署**: Docker, Kubernetes, Terraform
- **监控**: Prometheus, Grafana, ELK Stack
- **文档**: Markdown, OpenAPI (Swagger), Confluence

## 故事目录结构

```
exercise_md_fr/
├─ teaching_framework/planning_mds_exercise_template.md               (框架设计规划与练习类型定义)
│
├─ dt_financial_risk_assessment/            (本故事)
│   ├─ constraints/                            (练习约束文件目录)
│   │   ├─ exercise_constraints_fs_01.md         (ExFS_01 系列约束)
│   │   ├─ exercise_constraints_fs_02.md         (ExFS_02 系列约束)
│   │   ├─ exercise_constraints_fs_03.md         (ExFS_03 系列约束)
│   ├─ inputs/                                 (故事的输入文件)
│   │   ├─ user_story_fs_01_amount_check.md      (ExFS_01 用户故事)
│   │   ├─ user_story_fs_02_field_validation.md  (ExFS_02 用户故事)
│   │   ├─ user_story_fs_03_limit_crosscheck.md  (ExFS_03 用户故事)
│   │   ├─ regulatory_requirements.md          (监管合规要求详情)
│   │   ├─ risk_model_specs.py                 (风险模型规格说明)
│   │   ├─ transaction_data_schema.json        (交易数据架构定义)
│   │   ├─ stakeholder_interviews.txt          (利益相关者访谈记录)
│   │   ├─ legacy_system_integration.md        (遗留系统集成文档)
│   │   ├─ security_compliance_checklist.md    (安全合规检查清单)
│   │   ├─ performance_benchmarks.csv          (性能基准测试数据)
│   │   └─ system_test_cases.md                (系统测试用例)
│   └─ outputs/                                (故事的练习输出)
│       ├─ ExFS_01_AmountCheck/                (ExFS_01 系列输出)
│       │   ├─ s1_implementation_analysis.md     (步骤1: 实现分析)
│       │   ├─ s2_action_plan.md                 (步骤2: 行动计划)
│       │   ├─ amount_check.py                   (步骤2,4,5: 代码实现)
│       │   ├─ test_amount_check.py              (步骤3: 单元测试)
│       │   └─ s5_api_documentation.md           (步骤5: API文档，可选)
│       ├─ ExFS_02_FieldValidation/            (ExFS_02 系列输出)
│       │   ├─ s1_implementation_analysis.md     (步骤1: 实现分析)
│       │   ├─ s2_action_plan.md                 (步骤2: 行动计划)
│       │   ├─ field_validation.py               (步骤2,4,5: 代码实现)
│       │   ├─ test_field_validation.py          (步骤3: 单元测试)
│       │   └─ s5_api_documentation.md           (步骤5: API文档，可选)
│       ├─ ExFS_03_LimitCrossCheck/            (ExFS_03 系列输出)
│       │   ├─ s1_implementation_analysis.md     (步骤1: 实现分析)
│       │   ├─ s2_action_plan.md                 (步骤2: 行动计划)
│       │   ├─ account_limit_check.py            (步骤2,4,5: 代码实现)
│       │   ├─ test_account_limit_check.py       (步骤3: 单元测试)
│       │   └─ s5_api_documentation.md           (步骤5: API文档，可选)
│       ├─ ExMS_10_RequirementsModel/          (ExMS_10 输出)
│       │   └─ risk_assessment_data_model_v1.md  (数据模型文档)
│       ├─ ExMS_11_SystemArchitecture/         (ExMS_11 输出)
│       │   └─ system_architecture_v1.md         (系统架构文档)
│       ├─ ExMS_12_AIModelEvaluation/          (ExMS_12 输出)
│       │   └─ model_evaluation_criteria_v1.md   (模型评估标准文档)
│       └─ ExMS_13_SecurityAudit/              (ExMS_13 输出)
│           └─ security_audit_plan_v1.md         (安全审计计划文档)
└─ ...
```


## 工程练习

本故事包含以下练习系列：

**微功能开发系列 (ExFS - 推荐用于逐步演示):**

1.  **ExFS_01_AmountCheck**: 实现基本交易金额阈值检查功能 (5步系列)
2.  **ExFS_02_FieldValidation**: 实现简单客户数据字段验证功能 (5步系列)
3.  **ExFS_03_LimitCrossCheck**: 实现基本账户限额交叉检查功能 (5步系列)

**宏观视角/独立任务练习 (ExMS):**

4.  **ExMS_10_RequirementsModel**: 基于监管和业务需求开发全面的数据模型。
5.  **ExMS_11_SystemArchitecture**: 设计满足性能和安全要求的可扩展系统架构。
6.  **ExMS_12_AIModelEvaluation**: 为风险评估ML模型创建评估标准，考虑偏差、准确性和可解释性。
7.  **ExMS_13_SecurityAudit**: 制定安全审计计划，确保符合金融行业法规的同时保持系统性能。


## 如何使用本故事进行练习

1. **准备**：熟悉本故事背景、业务目标和技术栈。
2. **选择练习**：查阅下方"详细练习说明"或 `teaching_framework/planning_mds_exercise_template.md` 中定义的练习类型，选择你想尝试的练习。
3. **定位输入**：根据练习类型的要求，在本故事的 `inputs/` 目录下找到对应的输入文件。
4. **执行练习**：使用AI助手，根据练习要求处理输入文件。
5. **保存结果**：将生成的输出保存到 `outputs/` 目录下对应的子目录中。
6. **反思**：评估生成内容的质量，思考AI+Markdown在金融风控平台开发流程中的应用价值。

## 详细练习说明

以下是本故事中的详细练习说明：

### ExMS_10: 从需求文档生成数据模型 (Mermaid ERD)

> **目标**: 练习使用AI从结构化和非结构化的需求文档中提取关键实体、属性和关系，并生成符合要求的实体关系图(ERD)。这有助于在早期阶段可视化数据结构，促进团队沟通和数据库设计。
>
> **理论/结构**: 信息提取与建模。步骤：分析需求文档 -> 识别核心实体 -> 确定实体属性和类型 -> 定义实体间关系 -> 生成Mermaid ERD代码 -> 添加解释。
>
> **输入**:
> * `dt_financial_risk_assessment/inputs/regulatory_requirements.md`
> * `dt_financial_risk_assessment/inputs/transaction_data_schema.json`
> * `dt_financial_risk_assessment/inputs/stakeholder_interviews.txt`
> * (可选) 本文件中的业务背景和目标 (`## 故事背景`, `## 业务目标`)
>
> **AI助手角色**:
> * 仔细阅读并理解所有输入文档中关于数据存储和处理的需求
> * 识别核心业务实体（如Transaction, Customer, Account, Alert, Regulation等）
> * 提取每个实体的关键属性，并推断其数据类型
> * 确定实体之间的主要关系（一对一、一对多、多对多）
> * 生成符合Mermaid语法的ER图代码
> * 确保ER图反映了关键的业务规则和监管要求（如数据保留、审计追踪）
> * 为生成的ER图提供简要的说明
>
> **复杂度分析**: 中到高。需要整合来自多个不同格式文档的信息，理解金融领域的特定概念（如AML, KYC），并将其准确地映射到数据模型。需要较强的抽象和结构化能力。
>
> **输出位置与方式**:
> * **输出目录**: `dt_financial_risk_assessment/outputs/ExMS_10_RequirementsModel/`
> * **最终产物**: `risk_assessment_data_model_v1.md` - 包含Mermaid ER图代码及其解释说明的Markdown文件

### ExMS_11: 从需求生成系统架构图 (Mermaid)

> **目标**: 练习使用AI基于项目概述、技术要求和约束，设计一个高层次的系统架构，并使用Mermaid图表进行可视化。这有助于快速勾勒系统蓝图，识别关键组件和交互。
>
> **理论/结构**: 系统设计与可视化。步骤：理解业务目标和技术要求 -> 识别关键系统组件 -> 定义组件职责和交互 -> 选择合适的架构模式 -> 生成Mermaid架构图代码 -> 添加架构说明。
>
> **输入**:
> * 本文件中的项目概述、技术要求、技术栈和约束 (`## 故事背景`, `## 业务目标`, `## 技术栈`, `## 技术要求`)
> * (可选) `dt_financial_risk_assessment/inputs/legacy_system_integration.md`
>
> **AI助手角色**:
> * 分析项目需求，特别是性能（低延迟、高吞吐）、安全、合规和集成要求
> * 设计一个包含关键组件（如API Gateway, Real-time Processing Engine, Risk Model Service, Data Store, Reporting Service, Integration Adapters）的系统架构
> * 定义组件之间的主要交互方式（同步API调用、异步消息传递）
> * 考虑可扩展性（如微服务架构）、容错性和安全性
> * 选择合适的Mermaid图表类型（如`graph TD`或`C4 Model`的简化表示）来展示架构
> * 生成清晰、准确的Mermaid代码
> * 提供架构图的文字说明，解释关键组件和设计决策
>
> **复杂度分析**: 高。需要综合理解业务需求、技术约束和常见的架构模式（如事件驱动、微服务）。需要做出合理的设计权衡，并将复杂的系统关系简化为清晰的图表。
>
> **输出位置与方式**:
> * **输出目录**: `dt_financial_risk_assessment/outputs/ExMS_11_SystemArchitecture/`
> * **最终产物**: `system_architecture_v1.md` - 包含Mermaid架构图代码及其解释说明的Markdown文件

### ExMS_12: 从模型规格生成评估标准文档

> **目标**: 练习使用AI基于机器学习模型的规格说明和业务背景，创建一份全面的模型评估标准文档。这有助于确保模型评估不仅关注技术指标，也紧密结合业务目标和风险考量（如公平性、可解释性）。
>
> **理论/结构**: 模型评估与文档生成。步骤：理解模型目标和业务场景 -> 识别关键评估维度 -> 定义具体评估指标 -> 设定验收阈值 -> 考虑偏见和公平性 -> 规划评估流程 -> 结构化文档。
>
> **输入**:
> * `dt_financial_risk_assessment/inputs/risk_model_specs.py`
> * 本文件中的业务背景、成功标准和开发挑战 (`## 故事背景`, `## 成功标准`, `## 开发挑战`)
> * (可选) `dt_financial_risk_assessment/inputs/regulatory_requirements.md` (关于模型解释性和公平性的要求)
>
> **AI助手角色**:
> * 分析模型规格和相关需求，理解每个模型（欺诈检测、信用评分等）的目标
> * 为每个模型定义一套评估指标，包括：
>   * 准确性指标 (Accuracy, Precision, Recall, F1-score, AUC-ROC, AUC-PR)
>   * 业务相关指标 (如False Positive Rate / False Negative Rate对业务的影响)
>   * 性能指标 (预测延迟)
>   * 公平性与偏见指标 (如不同受保护群体的表现差异)
>   * 可解释性评估方法 (如SHAP, LIME的应用计划)
> * 根据成功标准设定每个指标的验收阈值
> * 描述模型验证方法（如交叉验证、回测）
> * 规划模型监控和再训练策略
> * 将所有内容组织成结构清晰的Markdown文档
>
> **复杂度分析**: 中到高。需要理解机器学习模型评估的各种指标及其在金融风控场景下的具体含义。需要特别关注公平性、可解释性等非技术性但至关重要的方面。
>
> **输出位置与方式**:
> * **输出目录**: `dt_financial_risk_assessment/outputs/ExMS_12_AIModelEvaluation/`
> * **最终产物**: `model_evaluation_criteria_v1.md` - 包含详细模型评估标准的Markdown文档

### ExMS_13: 从合规清单生成安全审计计划

> **目标**: 练习使用AI基于安全合规要求清单和系统技术细节，生成一份结构化的安全审计计划。这有助于系统化地规划审计活动，确保覆盖所有关键合规点，并为审计执行提供清晰指引。
>
> **理论/结构**: 合规理解与审计规划。步骤：分析合规要求 -> 映射到系统组件/流程 -> 设计审计测试用例 -> 规划审计范围和方法 -> 确定审计频率和负责人 -> 组织为审计计划文档。
>
> **输入**:
> * `dt_financial_risk_assessment/inputs/security_compliance_checklist.md`
> * 本文件中的技术要求（特别是 `安全框架` 部分）和技术栈信息 (`## 技术要求`, `## 技术栈`)
> * (可选) `dt_financial_risk_assessment/inputs/regulatory_requirements.md`
> * (可选) ExMS_11生成的系统架构图 (`dt_financial_risk_assessment/outputs/ExMS_11_SystemArchitecture/system_architecture_v1.md`)
>
> **AI助手角色**:
> * 解析安全合规清单中的每一项要求
> * 将抽象的合规要求映射到具体的系统组件、配置、流程或策略上
> * 为关键要求设计具体的审计步骤或测试用例（例如，"验证数据传输是否全程使用TLS 1.2+加密"、"检查访问控制策略是否遵循最小权限原则"、"审计日志是否完整且防篡改"）
> * 定义审计范围（涵盖哪些系统、数据、流程）
> * 建议审计方法（如配置审查、渗透测试、代码审计、访谈）
> * 规划审计频率（如季度、年度、按需）
> * 建议各项审计活动的负责人（内部安全团队、第三方审计机构）
> * 将审计计划组织成结构化的Markdown文档，包含审计目标、范围、方法、时间表、资源需求等部分
>
> **复杂度分析**: 高。需要深入理解金融行业的安全合规标准（非常具体和严格），并能将其与现代云原生技术栈（K8s, Kafka等）的实践相结合。需要将策略性要求转化为可操作的审计步骤。
>
> **输出位置与方式**:
> * **输出目录**: `dt_financial_risk_assessment/outputs/ExMS_13_SecurityAudit/`
> * **最终产物**: `security_audit_plan_v1.md` - 包含详细安全审计计划的Markdown文档