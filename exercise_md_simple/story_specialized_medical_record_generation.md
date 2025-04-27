# User Story: Specialized Medical Record Generation System

(参考核心开发理念：[思考驱动开发与AI协作](teaching_framework/thinking_driven_development_with_ai.md))

## 1. User Story (用户故事)

# 专科病历生成系统：AI+Markdown练习故事实例

> **重要约束**：在整个故事实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。

本文档描述了"专科病历生成系统"这个故事实例的背景、业务场景和相关资料，用于支持AI+Markdown练习框架。本故事聚焦于一个大型医院系统，旨在利用AI技术自动化生成特定专科（如心脏科、肿瘤科）的出院小结或门诊病历。

## 故事背景

"General Hospital System" (GHS) 是一家拥有多个专科中心的大型医疗机构。医生们普遍反映，在完成诊疗后，撰写符合规范、信息全面的专科病历报告耗时费力，且格式和术语的一致性难以保证。为了提高效率、保证病历质量并减轻医生负担，GHS 决定启动一个项目，利用 AI 从原始诊疗记录（可能包括自由文本笔记、检查结果、医嘱等）中提取关键信息，并自动生成结构化的专科病历报告。

## 业务目标

1.  **提高效率**: 显著减少医生撰写专科病历报告所需的时间。
2.  **提升一致性**: 确保生成的病历报告在格式、术语使用上符合医院和专科规范。
3.  **保证完整性**: 减少因人工疏忽导致的关键信息遗漏。
4.  **支持合规**: 生成的报告需符合医疗记录相关的法规要求（如数据隐私、内容要求）。
5.  **易于审核**: 生成的报告应清晰易懂，方便医生快速审核和修订。

## 团队角色

-   **产品经理 (赵敏)**: 负责病历生成系统的需求定义和功能规划。
-   **临床信息学专家 (孙医生)**: 提供专科医学知识、病历模板标准和术语规范。
-   **后端工程负责人 (周华)**: Python专家，负责系统架构设计和核心逻辑。
-   **NLP工程师 (吴倩)**: 负责信息提取、术语标准化和文本生成算法。
-   **数据工程师 (李刚)**: 负责处理和整合来自不同医疗系统的原始数据。
-   **QA工程师 (郑芳)**: 负责系统测试、病历内容准确性验证和合规性检查。
-   **DevOps工程师 (王磊)**: 负责系统部署、监控和维护。
-   **你**: 作为Scrum Master，负责协调团队工作，确保项目按计划进行，解决问题，并促进跨学科沟通。

## 技术栈 (建议)

-   **后端**: Python 3.9+, FastAPI / Flask
-   **NLP/文本处理**: spaCy, NLTK, Transformers (Hugging Face), Regular Expressions
-   **数据处理**: Pandas, potentially interfacing with FHIR resources or databases
-   **模板引擎**: Jinja2 (或其他Markdown兼容模板)
-   **术语/本体**: SNOMED CT, ICD-10 (需要知识库或API接入)
-   **部署**: Docker, Kubernetes (可选)
-   **监控**: Prometheus, Grafana (可选)
-   **文档**: Markdown, Mermaid

## 故事目录结构

```
exercise_md_simple/
├── teaching_framework/planning_mds_exercise_template.md         (框架设计规划与练习类型定义)
|
├── story_specialized_medical_record_generation/ (本故事)
│   ├── story_specialized_medical_record_generation.md (本文件 - 故事描述)
│   ├── inputs/                                      (故事的输入文件)
│   │   ├── raw_clinical_notes_cardiology.txt        (示例：心脏科原始诊疗笔记)
│   │   ├── lab_results_cardiology.json              (示例：心脏科相关化验结果)
│   │   ├── discharge_summary_template_cardiology.md (示例：心脏科出院小结模板)
│   │   ├── snomed_ct_subset_cardiology.csv          (示例：心脏科常用SNOMED CT术语子集)
│   │   ├── clinic_visit_notes_oncology.txt          (示例：肿瘤科门诊随访笔记)
│   │   ├── imaging_report_oncology.txt              (示例：肿瘤科影像报告文本)
│   │   ├── clinic_report_template_oncology.md       (示例：肿瘤科门诊报告模板)
│   │   ├── icd10_codes_oncology.json                (示例：肿瘤科常用ICD-10编码)
│   │   ├── user_story_sr_01_data_extraction.md      (ExSR_01 用户故事)
│   │   ├── user_story_sr_02_template_filling.md     (ExSR_02 用户故事)
│   │   ├── user_story_sr_03_terminology_mapping.md  (ExSR_03 用户故事)
│   │   ├── user_story_sr_04_summary_generation.md   (ExSR_04 用户故事)
│   │   ├── user_story_sr_05_compliance_check.md     (ExSR_05 用户故事)
│   │   └── hospital_documentation_guidelines.md     (医院病历书写规范)
│   ├── constraints/                                 (练习约束文件)
│   │   └── exercise_constraints_sr_basic.md         (本故事的基础约束指南)
│   └── outputs/                                     (故事的练习输出)
│       ├── ExSR_01_DataExtraction/                  (数据提取练习输出)
│       │   ├── s1_implementation_analysis.md
│       │   ├── s2_action_plan.md
│       │   ├── data_extractor.py
│       │   ├── test_data_extractor.py
│       │   └── s5_api_documentation.md
│       ├── ExSR_02_TemplateFilling/                 (模板填充练习输出)
│       │   ├── ... (类似结构)
│       ├── ExSR_03_TerminologyMapping/              (术语映射练习输出)
│       │   ├── ... (类似结构)
│       ├── ExSR_04_SummaryGeneration/               (摘要生成练习输出)
│       │   ├── ... (类似结构)
│       ├── ExSR_05_ComplianceCheck/                 (合规检查练习输出)
│       │   ├── ... (类似结构)
│       ├── ExMS_30_WorkflowDesign/                  (宏观任务：工作流设计输出)
│       │   └── report_generation_workflow.md
│       └── ExMS_31_QualityEvaluation/               (宏观任务：质量评估输出)
│           └── report_quality_criteria.md
└── ...                                  
```

## 如何使用本故事进行练习

1.  **准备**: 熟悉本故事背景、业务目标和技术栈建议。
2.  **学习核心理念**: 阅读[思考驱动开发与AI协作](teaching_framework/thinking_driven_development_with_ai.md)，理解分步骤思考的重要性。
3.  **查阅约束**: 阅读 `constraints/exercise_constraints_sr_basic.md` 文件，了解本故事练习的基本要求和简化假设。
4.  **选择练习**: 查阅下方练习列表，选择你想尝试的练习（建议从 ExSR 系列开始）。
5.  **定位输入**: 根据练习描述，在本故事的 `inputs/` 目录下找到对应的输入文件。注意区分心脏科(`_cardiology`)和肿瘤科(`_oncology`)的示例文件。
6.  **执行练习**: 使用 AI 助手，根据练习要求处理输入文件，遵循思考驱动开发的步骤。
7.  **保存结果**: 将生成的输出保存到 `outputs/` 目录下对应的子目录中。
8.  **反思**: 评估生成内容的质量，思考 AI+Markdown 在专科病历生成流程中的应用价值和挑战。

## 练习列表与描述

> **注意**：本故事包含两类练习:
> 1.  **ExSR_01 到 ExSR_05 系列**是微功能开发练习，专注于病历生成过程中的关键 NLP 和文本处理任务。**强烈建议按顺序完成**，体验完整的开发流程。
> 2.  **ExMS_30 到 ExMS_31 系列**是宏观任务练习，侧重于整体设计和评估。

### 微功能开发练习 (ExSR 系列 - 建议按序完成)

#### ExSR_01系列: 从非结构化笔记中提取结构化信息
> **系列目标**: 练习使用AI从自由文本的临床笔记中提取关键的结构化信息（如症状、诊断、药物、检查结果关键值）。这是病历自动生成的第一步。

##### ExSR_01_1: 从用户故事到实现思考
> **目标**: 分析从原始笔记提取信息的用户故事，提出基于NLP技术的实现思路。
> **输入**: `inputs/user_story_sr_01_data_extraction.md`, `inputs/raw_clinical_notes_cardiology.txt` (作为分析示例)
> **AI助手角色**: 分析需求，识别挑战(文本多样性、缩写、否定词)，探索方案(NER、规则、Regex)，提出实现思路。
> **复杂度**: 中。
> **输出**: `outputs/ExSR_01_DataExtraction/s1_implementation_analysis.md`

##### ExSR_01_2: 从实现思考到行动计划
> **目标**: 将信息提取思路转化为任务列表、函数接口和初始代码框架。
> **输入**: `outputs/ExSR_01_DataExtraction/s1_implementation_analysis.md`
> **AI助手角色**: 分解任务，设计函数签名(输入文本，输出结构化数据如字典或对象)，创建初始 Python 文件。
> **复杂度**: 中低。
> **输出**: `outputs/ExSR_01_DataExtraction/s2_action_plan.md`, `outputs/ExSR_01_DataExtraction/data_extractor.py` (初始框架)

##### ExSR_01_3: 单元测试设计与审查
> **目标**: 为信息提取功能设计单元测试。
> **输入**: `outputs/ExSR_01_DataExtraction/s2_action_plan.md`, `outputs/ExSR_01_DataExtraction/data_extractor.py`
> **AI助手角色**: 设计测试用例(不同类型信息、含糊表达、边界情况)，编写 `unittest` 或 `pytest` 代码。
> **复杂度**: 中。
> **输出**: `outputs/ExSR_01_DataExtraction/test_data_extractor.py`

##### ExSR_01_4: 测试驱动开发实现
> **目标**: 基于测试用例实现信息提取功能。
> **输入**: `outputs/ExSR_01_DataExtraction/test_data_extractor.py`, `outputs/ExSR_01_DataExtraction/data_extractor.py`
> **AI助手角色**: 编写通过测试的代码(可能涉及 spaCy NER, Regex等)，处理测试中发现的问题。
> **复杂度**: 中高。
> **输出**: `outputs/ExSR_01_DataExtraction/data_extractor.py` (完整实现)

##### ExSR_01_5: 函数文档完善
> **目标**: 完善代码文档和使用说明。
> **输入**: `outputs/ExSR_01_DataExtraction/data_extractor.py`
> **AI助手角色**: 完善函数文档字符串，说明提取逻辑和输出格式，提供示例。
> **复杂度**: 低。
> **输出**: `outputs/ExSR_01_DataExtraction/data_extractor.py` (带文档), (可选) `outputs/ExSR_01_DataExtraction/s5_api_documentation.md`

---

#### ExSR_02系列: 将提取的数据填充到Markdown报告模板
> **系列目标**: 练习使用AI将上一步提取的结构化数据，准确地填充到预定义的Markdown病历模板中。

##### ExSR_02_1: 从用户故事到实现思考
> **目标**: 分析模板填充需求，提出实现思路。
> **输入**: `inputs/user_story_sr_02_template_filling.md`, `inputs/discharge_summary_template_cardiology.md` (作为模板示例), 假设的结构化数据(来自ExSR_01)
> **AI助手角色**: 分析需求，识别挑战(数据格式匹配、缺失值处理、条件渲染)，探索方案(模板引擎如Jinja2)，提出实现思路。
> **复杂度**: 低。
> **输出**: `outputs/ExSR_02_TemplateFilling/s1_implementation_analysis.md`

##### ExSR_02_2: 从实现思考到行动计划
> **目标**: 转化为任务列表、函数接口和代码框架。
> **输入**: `outputs/ExSR_02_TemplateFilling/s1_implementation_analysis.md`
> **AI助手角色**: 分解任务，设计函数签名(输入结构化数据、模板路径，输出填充后的Markdown文本)，创建初始 Python 文件。
> **复杂度**: 低。
> **输出**: `outputs/ExSR_02_TemplateFilling/s2_action_plan.md`, `outputs/ExSR_02_TemplateFilling/template_filler.py` (初始框架)

##### ExSR_02_3: 单元测试设计与审查
> **目标**: 为模板填充功能设计单元测试。
> **输入**: `outputs/ExSR_02_TemplateFilling/s2_action_plan.md`, `outputs/ExSR_02_TemplateFilling/template_filler.py`
> **AI助手角色**: 设计测试用例(完整数据、部分缺失数据、不同模板部分)，编写测试代码，验证输出Markdown的正确性。
> **复杂度**: 中低。
> **输出**: `outputs/ExSR_02_TemplateFilling/test_template_filler.py`

##### ExSR_02_4: 测试驱动开发实现
> **目标**: 基于测试用例实现模板填充功能。
> **输入**: `outputs/ExSR_02_TemplateFilling/test_template_filler.py`, `outputs/ExSR_02_TemplateFilling/template_filler.py`
> **AI助手角色**: 编写通过测试的代码(使用模板引擎)，处理数据和模板的交互。
> **复杂度**: 中。
> **输出**: `outputs/ExSR_02_TemplateFilling/template_filler.py` (完整实现)

##### ExSR_02_5: 函数文档完善
> **目标**: 完善代码文档和使用说明。
> **输入**: `outputs/ExSR_02_TemplateFilling/template_filler.py`
> **AI助手角色**: 完善文档字符串，说明输入数据结构要求、模板语法约定，提供示例。
> **复杂度**: 低。
> **输出**: `outputs/ExSR_02_TemplateFilling/template_filler.py` (带文档), (可选) `outputs/ExSR_02_TemplateFilling/s5_api_documentation.md`

---

#### ExSR_03系列: 将提取的医学术语映射到标准本体 (如SNOMED CT)
> **系列目标**: 练习使用AI将从文本中提取的、可能不规范的医学术语，映射到标准的医学本体（提供一个简化的术语子集作为输入），以提高报告的标准化程度。

##### ExSR_03_1: 从用户故事到实现思考
> **目标**: 分析术语标准化需求，提出实现思路。
> **输入**: `inputs/user_story_sr_03_terminology_mapping.md`, `