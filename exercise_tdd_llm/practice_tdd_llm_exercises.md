# Practice: LLM API 调用与健康顾问集成

> **工作目录说明**：本文档位于 `exercise_tdd_llm/` 目录下（相对于项目根目录）。所有文件引用路径均基于此目录。例如，`../tdd_rules/tdd_ai_thinking.md` 指向的是项目根目录下的 `tdd_rules/tdd_ai_thinking.md`。

(核心开发理念参考: [测试驱动开发核心理念](../tdd_rules/tdd_ai_thinking.md))
(单元测试设计参考: [TDD单元测试设计技巧](../tdd_rules/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](../tdd_rules/planning_tdd_exercise.md))
(目录结构核心原则参考: [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

## User Story (原始用户故事)
> 作为AI个性化健康顾问系统的开发者，我希望利用LLM技术（特别是DEEPSEEK模型）来增强系统的智能分析和建议能力，为用户提供基于其健康数据的个性化解读和指导。

## 功能需求 (Feature Requirements)
1.  **基于DEEPSEEK的健康数据解读与建议生成**：系统能够接收用户的健康指标（BMI、BMR、TDEE等），通过调用DEEPSEEK模型进行分析，并生成通俗易懂的解读及个性化的健康建议（涵盖饮食、运动、生活方式）。
2.  **DEEPSEEK模型调用实验与优化**：提供一个灵活的环境，方便测试不同的DEEPSEEK模型版本、调整提示策略、比较参数效果，以优化建议质量和成本效益。
3.  确保所有与LLM的交互均通过项目根目录的 `utils_llm` 工具包进行。
4.  正确配置和管理API密钥（如 `DEEPSEEK_API_KEY`）。

## LLM API 调用与健康顾问集成：AI+TDD练习实践实例

> **重要约束**：
> 1. 在整个实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。
> 2. 本练习系列使用项目根目录中的`utils_llm`工具包，所有练习都需要正确配置相关环境变量，特别是DEEPSEEK_API_KEY。
> 3. 在开始练习前，请确保已经正确设置了所有必要的API密钥和环境变量。

### 基础结构说明

在本练习中，涉及到的占位符具体含义如下：
*   `{app_name}`: `ai_wellness_advisor`
*   `{module_name}`: `llm_integration` (具体在各特性实现部分会再次明确)

本实践遵循标准的TDD练习框架结构。详细的目录结构、文件命名规范以及TDD周期产出物的组织方式，请严格遵循以下权威文档：
*   [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md) (定义了特性研发周期内，如 `dev_cycles`, `src`, `tests` 中各产出物的具体组织和命名)
*   [项目整体目录结构](../README_folders.md) (定义了项目根目录及 `{app_name}` 应用的整体结构)

#### 核心命名原则摘要

1.  **特性名称 (feature_name)**：
    *   格式：`小写字母_用下划线分隔`
    *   示例：`deepseek_health_recommendation`, `deepseek_experiment_platform`
    *   要求：描述性、简洁、表明功能

**工作目录说明**：本文档（用户故事）位于 `exercise_tdd_llm/` 目录下。所有与本用户故事直接相关的文件引用路径均基于此目录。例如，`../tdd_rules/tdd_ai_thinking.md`。

**TDD周期产出物归档核心路径**：
本练习相关的每个TDD周期（例如 `ExTDD_01_DeepSeekHealthRecommendation`）的详细思考过程、约束等文档，将统一归档到主应用项目 `{app_name}` 的开发周期记录区内，具体路径为 `../{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` (例如 `../ai_wellness_advisor/dev_cycles/llm_integration/ExTDD_01_DeepSeekHealthRecommendation/`)。对应的代码和测试则位于 `../{app_name}/src/{module_name}/` 和 `../{app_name}/tests/{module_name}/`。

本项目中的 `practice_*.md` 文件主要作为TDD练习的起点和高级别需求描述。

本练习中定义的各特性对应的详细用户故事文档 (`_user_story_{feature_name}.md`) 位于上述 `{app_name}` 项目的相应特性开发周期目录中，例如：
*   DEEPSEEK健康推荐特性 (`deepseek_health_recommendation`): `../{app_name}/dev_cycles/llm_integration/ExTDD_01_DeepSeekHealthRecommendation/_user_story_deepseek_health_recommendation.md`
*   DEEPSEEK模型调用实验平台特性 (`deepseek_experiment_platform`): `../{app_name}/dev_cycles/llm_integration/ExTDD_02_DeepSeekExperimentPlatform/_user_story_deepseek_experiment_platform.md`

### TDD周期产出物遵循的规范

所有TDD练习周期的产出物，包括思考文档、源代码和测试代码的目录结构、文件命名及存放位置，均严格遵循以下权威文档的规定：
*   [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md)
*   [项目整体目录结构](../README_folders.md)

**核心要点回顾**：
*   **思考与设计文档**：位于 `{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/` 目录下，详细文件列表（如 `_user_story_{feature_name}.md`, `_s1_think_options_{feature_name}.md`, `_s2_think_design_{feature_name}.md`, `_s3_think_validation_{feature_name}.md` 等）请参见上述规范文档。这些文档记录了TDD周期的关键思考过程，是确保AI辅助开发过程透明化和可追溯性的重要环节，**强烈建议在每个TDD周期中按规范创建，以完整体现思考和决策过程**。
*   **源代码**：位于 `{app_name}/src/{module_name}/{feature_name}.py`。
*   **特性代码说明**：位于 `{app_name}/src/{module_name}/README_{feature_name}.md`。
*   **测试代码**：位于 `{app_name}/tests/{module_name}/test_{feature_name}.py`。

**重要提示**：
- 本文档 (`practice_tdd_llm_exercises.md`) 作为练习的起点，提供了高级别的用户故事。
- 各特性更详细的用户故事阐述和演进记录位于其对应的 `dev_cycles` 目录下的 `_user_story_{feature_name}.md` 文件中。
- `dev_cycles` 目录专注于记录思考、设计和演进过程的文档，实际的代码和测试产出物位于 `src` 和 `tests` 目录中。
- 在每个TDD周期中，务必创建 `_s1_think_options_{feature_name}.md`, `_s2_think_design_{feature_name}.md`, 和 `_s3_think_validation_{feature_name}.md` 这三个中间思考文档。

## LLM API 调用特定实现 (两个Feature)

### 1. ExTDD_01_DeepSeekHealthRecommendation: 基于DEEPSEEK的健康推荐

> **重要提示**：开始此特性练习时，请务必遵循完整的TDD五步循环，包括创建用户故事 (`_user_story_deepseek_health_recommendation.md`) 以及所有相关的思考文档 (`_s1_think_options_deepseek_health_recommendation.md`, `_s2_think_design_deepseek_health_recommendation.md`, `_s3_think_validation_deepseek_health_recommendation.md` 等)，然后再编写测试、实现代码和重构。

module_name: llm_integration
feature_name: deepseek_health_recommendation

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_01_DeepSeekHealthRecommendation/`
(其内部文件结构及对应的代码/测试路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_01_DeepSeekHealthRecommendation) 针对Feature_01
> 作为用户，我希望输入我的BMI、BMR、TDEE数据后，系统能通过DEEPSEEK模型分析这些数据，并给出针对性的健康指导和生活方式建议。作为开发者，我需要构建一个模块，该模块能够接收用户的健康指标，构造合适的提示调用DEEPSEEK模型，并解析返回的建议。

### 2. ExTDD_02_DeepSeekExperimentPlatform: DEEPSEEK模型调用实验平台

> **重要提示**：开始此特性练习时，请务必遵循完整的TDD五步循环，包括创建用户故事 (`_user_story_deepseek_experiment_platform.md`) 以及所有相关的思考文档 (`_s1_think_options_deepseek_experiment_platform.md`, `_s2_think_design_deepseek_experiment_platform.md`, `_s3_think_validation_deepseek_experiment_platform.md` 等)，然后再编写测试、实现代码和重构。

module_name: llm_integration
feature_name: deepseek_experiment_platform

对应的TDD周期文档存放路径：`../{app_name}/dev_cycles/{module_name}/ExTDD_02_DeepSeekExperimentPlatform/`
(其内部文件结构及对应的代码/测试路径遵循项目统一规范，详见 [ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md))

#### 核心用户故事 (ExTDD_02_DeepSeekExperimentPlatform) 针对Feature_02
> 作为开发者，我需要一个灵活的环境来测试不同的DEEPSEEK模型、提示策略和参数，以便优化健康建议的质量和调用成本。

## 补充说明与资源

### 工具包 (`utils_llm`) 说明
本练习系列使用的`utils_llm`工具包提供以下核心功能：
1. **基础对话功能** (`chat_gpt_plain`, `chat_gpt_json`)
2. **多模态支持** (`get_gpt_messages_multimodal`, `upload_image_to_cloud`)
3. **模型管理** (`get_client_by_model` 支持GPT、Qwen、Deepseek等)
4. **工具特性** (内置重试、错误处理、响应解析、类型检查)

### 通用约束
1. **环境配置**: 正确配置 `DEEPSEEK_API_KEY` 等环境变量，使用 `.env` 文件管理。
2. **错误处理**: API调用包含错误处理和重试机制，提供清晰错误信息。
3. **测试要求**: 单元测试覆盖核心功能，模拟外部API调用，测试不同输入和错误场景。
4. **文档要求**: 清晰的API文档，使用示例说明数据传入，性能和限制说明。

### 技术依赖
1. **Python环境**: Python 3.8+, pip
2. **核心依赖包**: `openai>=1.0.0`, `python-dotenv`, `tenacity`, `httpx`, `rich`, `json-repair` (及 `utils_llm/requirements.txt` 中其他依赖)
3. **环境变量**: `DEEPSEEK_API_KEY`, 可能还有其他模型API Key。

### 建议学习顺序与难度
1.  **ExTDD_01_DeepSeekHealthRecommendation** (难度：★★★☆☆): 掌握DEEPSEEK API调用基础。
2.  **ExTDD_02_DeepSeekExperimentPlatform** (难度：★★★★☆): 构建测试优化环境。