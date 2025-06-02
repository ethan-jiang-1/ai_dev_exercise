# Practice: AI Wellness Advisor - Core Components Development

> **工作目录说明**：本文档位于 `exercise_tdd_awa_core/` 目录下（相对于项目根目录）。所有文件引用路径均基于此目录或项目根目录。例如，`../tdd_rules/test_driven_development_with_ai.md` 指向的是项目根目录下的 `tdd_rules/test_driven_development_with_ai.md`。

(核心开发理念参考: [测试驱动开发核心理念](../tdd_rules/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](../tdd_rules/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](../tdd_rules/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

## 1. User Story (用户故事)

本项目旨在通过一系列TDD练习，逐步构建AI个性化健康顾问 (`{app_name}`: `ai_wellness_advisor`) 的核心后端组件。这些组件将协同工作，为用户提供全面的健康档案管理和个性化的健康建议。

> **重要约束**：在整个实践过程中，请确保所有在Cursor/Trae中的交互对话均使用中文，这是出于演示目的的要求。

## 基础结构说明

在本练习系列中，涉及到的占位符具体含义如下：
*   `{app_name}`: `ai_wellness_advisor`
*   `{module_name}`: 具体模块名将在各练习系列中定义 (例如 `wellness_profile`, `personalized_advisor`, `app_logic`)

本实践遵循标准的TDD练习框架结构。详细的目录结构、文件命名规范以及TDD周期产出物的组织方式，请严格遵循以下权威文档：
*   [ExTDD 特性研发目录结构：核心原则与详解](../../README_folder_feature.md) (定义了特性研发周期内，如 `dev_cycles`, `src`, `tests` 中各产出物的具体组织和命名)
*   [项目整体目录结构](../../README_folders.md) (定义了项目根目录及 `{app_name}` 应用的整体结构)

#### 核心命名原则摘要

1.  **特性名称 (feature_name)**：
    *   格式：`小写字母_用下划线分隔`
    *   示例：`comprehensive_profile_model`, `integrated_advice_generation`
    *   要求：描述性、简洁、表明功能

**工作目录说明**：本文档（用户故事）位于 `exercise_tdd_awa_core/` 目录下。所有与本用户故事直接相关的文件引用路径均基于此目录。例如，`../tdd_rules/test_driven_development_with_ai.md`。

**TDD周期产出物归档核心路径**：
本练习系列相关的每个TDD周期（例如 `ExTDD_01_ComprehensiveProfileModel`）的详细思考过程、约束等文档，将统一归档到主应用项目 `{app_name}` 的开发周期记录区内，具体路径为 `../../{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` (例如 `../../ai_wellness_advisor/dev_cycles/wellness_profile/ExTDD_01_ComprehensiveProfileModel/`)。对应的代码和测试快照则位于 `../../{app_name}/src/{module_name}/` 和 `../../{app_name}/tests/{module_name}/`。

本项目中的 `practice_*.md` 文件主要作为TDD练习的起点和高级别需求描述。

## 核心组件开发练习系列

为了构建 `ai_wellness_advisor` 的核心功能，我们将开展以下三个练习系列：

### 练习系列 1: `ExTDD_WellnessProfileBuilder` - 构建完整的健康档案模块
*   **目标**：实现一个健壮的健康档案构建和管理模块。
*   **对应 `README_prj.md` 模块**: `WellnessProfileBuilder` (第1层模块)
*   **建议模块名 (`{module_name}`)**: `wellness_profile`
*   **包含特性 (Features)**:
    1.  **`Feature_WPB_01_ComprehensiveProfileModel`**:
        *   **用户故事**: 作为开发者，我希望定义一个全面的Pydantic模型 (`UserProfile`)，用于存储用户的个人信息、健康指标（BMI, BMR, TDEE）、活动水平及潜在的健康目标，确保数据的完整性和类型安全。
        *   **核心任务**: 设计并实现 `UserProfile` Pydantic模型；编写针对模型验证、默认值、序列化/反序列化的单元测试。
    2.  **`Feature_WPB_02_ProfileCreationAndManagement`**:
        *   **用户故事**: 作为系统，我需要能够创建新的用户档案，用新数据（如新的体重记录）更新现有档案，并能检索用户完整的健康档案。
        *   **核心任务**: 实现创建、读取、更新用户档案的功能，集成BMI/DCNC计算逻辑；测试档案的创建、更新和检索流程。
    3.  **`Feature_WPB_03_ProfilePersistence`**:
        *   **用户故事**: 作为系统，我需要将用户档案持久化（例如，保存为JSON文件）并在需要时加载回来，确保数据在会话间不丢失。
        *   **核心任务**: 实现 `UserProfile` 实例的保存与加载；考虑多用户档案的管理方式；测试保存、加载及错误处理（如文件未找到）。

### 练习系列 2: `ExTDD_PersonalizedAdvisor` - 实现个性化健康顾问核心逻辑
*   **目标**：构建一个能够根据用户健康档案，通过LLM提供个性化健康建议的模块。
*   **对应 `README_prj.md` 模块**: `PersonalizedAdvisor` (第2层模块)
*   **建议模块名 (`{module_name}`)**: `personalized_advisor`
*   **包含特性 (Features)**:
    1.  **`Feature_PA_01_IntegratedAdviceGeneration`**:
        *   **用户故事**: 作为拥有完整健康档案的用户，我希望能基于我的所有数据（BMI, BMR, TDEE, 活动水平等），从个性化顾问处获得由LLM生成的覆盖饮食、运动和生活方式的个性化建议。
        *   **核心任务**: 设计并实现接收 `UserProfile` 对象，构造针对LLM的综合性提示（Prompt），调用LLM，并将返回结果解析为结构化建议的功能；通过模拟LLM调用来测试提示构建和响应解析。
    2.  **`Feature_PA_02_ContextualPromptEngineering`**:
        *   **用户故事**: 作为开发者，我希望能在个性化顾问中试验不同的提示工程策略，以优化LLM生成建议的质量和相关性，充分利用用户档案中的上下文信息。
        *   **核心任务**: 优化提示生成逻辑，支持不同的提示模板或策略；测试不同提示变体及其预期（模拟的）LLM输出。
    3.  **`Feature_PA_03_AdviceStructuringAndPresentation`**:
        *   **用户故事**: 作为用户，我希望个性化建议能以清晰、结构化且易于理解的方式呈现，最好能分类为饮食、运动和综合健康等。
        *   **核心任务**: 定义用于组织从LLM获取的建议的Pydantic模型；实现将此结构化建议格式化以便显示（即便实际UI非当前重点，其数据结构仍很重要）；测试从原始LLM输出（模拟）到定义的建议结构的转换。

### 练习系列 3: `ExTDD_AppIntegration` - 应用层逻辑与初步集成
*   **目标**：将各个独立开发的模块整合起来，形成一个初步可用的应用流程。
*   **对应 `README_prj.md` 模块**: 顶层应用逻辑与集成
*   **建议模块名 (`{module_name}`)**: `app_logic` (或直接在 `{app_name}/src/` 下的主应用逻辑部分)
*   **包含特性 (Features)**:
    1.  **`Feature_AI_01_MainWorkflow`**:
        *   **用户故事**: 作为用户，我希望能通过一个简单的流程与系统交互：输入我的数据，创建/更新我的档案，然后获得个性化建议。
        *   **核心任务**: 创建一个主应用脚本或外观类来编排整个工作流程：接收用户输入 -> 使用 `WellnessProfileBuilder` 管理档案 -> 使用 `PersonalizedAdvisor` 获取建议 ->呈现建议（例如，打印到控制台）；编写集成测试，模拟用户输入并验证端到端流程，重点测试模块间的交互。
    2.  **`Feature_AI_02_BasicCLI`**:
        *   **用户故事**: 作为开发者或测试者，我需要一个基础的命令行界面（CLI）来与 `ai_wellness_advisor` 系统交互，以便测试核心功能，如创建档案、查看档案和获取建议。
        *   **核心任务**: 使用如 `argparse` 或 `click` 库实现一个简单的CLI，暴露主要工作流程；测试CLI命令及其预期输出。

通过这三个练习系列，我们将逐步构建出 `ai_wellness_advisor` 的核心框架。每个练习都将强调TDD方法，确保代码质量和系统的可维护性。