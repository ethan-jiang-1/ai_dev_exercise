> **Note:** All file paths in this document are relative to the exercise's root directory: `exercise_md_fr/` (unless otherwise specified).

# User Story: Financial Risk Assessment System - part 3

(参考核心开发理念：[思考驱动开发与AI协作](teaching_framework/thinking_driven_development_with_ai_complex.md))
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
├─ teaching_framework/planning_mds_exercise_complex.md               (框架设计规划与练习类型定义)
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
2. **选择练习**：查阅下方"详细练习说明"或 `teaching_framework/planning_mds_exercise_complex.md` 中定义的练习类型，选择你想尝试的练习。
3. **定位输入**：根据练习类型的要求，在本故事的 `inputs/` 目录下找到对应的输入文件。
4. **执行练习**：使用AI助手，根据练习要求处理输入文件。
5. **保存结果**：将生成的输出保存到 `outputs/` 目录下对应的子目录中。
6. **反思**：评估生成内容的质量，思考AI+Markdown在金融风控平台开发流程中的应用价值。

## 详细练习说明

以下是本故事中的详细练习说明：

### ExFS_03系列: 基本账户限额交叉检查

> **系列目标**: 演示一个涉及多数据源输入的简单交叉检查功能的完整开发流程。
> **系列约束**: 详细约束参见 `constraints/exercise_constraints_fs_03.md` 文件。

#### ExFS_03_1: 从用户故事到实现思考

> **目标**: 分析账户限额交叉检查的用户故事，提出实现思路。
> **理论/结构**: 需求分析 -> 方案设计。
> **输入**: `dt_financial_risk_assessment/inputs/user_story_fs_03_limit_crosscheck.md`
> **AI助手角色**: 分析需求，识别挑战(数据合并、边界处理)，提出函数实现方案，建议数据结构。
> **复杂度**: 中。
> **输出位置与方式**: `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/s1_implementation_analysis.md`

#### ExFS_03_2: 从实现思考到行动计划

> **目标**: 将实现思路转化为任务列表和代码框架。
> **理论/结构**: 方案具体化 -> 任务分解 -> 代码框架设计。
> **输入**: `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/s1_implementation_analysis.md`
> **AI助手角色**: 分解任务，设计函数签名，创建包含函数定义的初始Python文件。
> **复杂度**: 中低。
> **输出位置与方式**: 
>   * `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/s2_action_plan.md`
>   * `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/account_limit_check.py` (初始框架)

#### ExFS_03_3: 单元测试设计与审查

> **目标**: 为账户限额检查功能设计单元测试。
> **理论/结构**: 测试设计。
> **输入**: `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/s2_action_plan.md`, `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/account_limit_check.py`, `dt_financial_risk_assessment/constraints/exercise_constraints_fs_03.md` (含数据结构示例)
> **AI助手角色**: 设计测试用例（超限、未超限、等于限额、无效输入），编写 `unittest` 代码。
> **复杂度**: 中。
> **输出位置与方式**: `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/test_account_limit_check.py`

#### ExFS_03_4: 测试驱动开发实现

> **目标**: 基于测试用例实现账户限额检查功能。
> **理论/结构**: TDD实践。
> **输入**: `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/test_account_limit_check.py`, `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/account_limit_check.py`
> **AI助手角色**: 编写通过所有测试的函数代码，实现加法和比较逻辑，处理边界情况。
> **复杂度**: 中。
> **输出位置与方式**: `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/account_limit_check.py` (完整实现)

#### ExFS_03_5: 函数文档完善

> **目标**: 完善代码文档和使用说明。
> **理论/结构**: 文档编写。
> **输入**: `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/account_limit_check.py`
> **AI助手角色**: 完善函数文档字符串，提供使用示例。
> **复杂度**: 低。
> **输出位置与方式**: 
>   * `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/account_limit_check.py` (带文档)
>   * (可选) `dt_financial_risk_assessment/outputs/ExFS_03_LimitCrossCheck/s5_api_documentation.md`