# Practice: LLM API调用练习系列 - AI个性化健康顾问

> **工作目录说明**：本文档位于 `~/ai_dev_exercise/exercise_tdd_llm/` 目录下，所有文件引用路径均基于此目录。例如，`./teaching_framework/test_driven_development_with_ai.md` 实际指向 `/Users/bowhead/ai_dev_exercise/exercise_tdd_llm/teaching_framework/test_driven_development_with_ai.md`。

(核心开发理念参考: [测试驱动开发核心理念](./teaching_framework/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](./teaching_framework/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](./teaching_framework/planning_tdd_exercise.md))

## 1. User Story (用户故事)

# LLM API调用：AI个性化健康顾问的智能核心

> **重要约束**：
> 1. 在整个实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。
> 2. 本练习系列使用项目根目录中的`utils_llm`工具包，所有练习都需要正确配置相关环境变量，特别是DEEPSEEK_API_KEY。
> 3. 在开始练习前，请确保已经正确设置了所有必要的API密钥和环境变量。

作为AI个性化健康顾问系统的开发者，我希望利用先进的LLM技术（特别是DEEPSEEK模型）来增强系统的智能分析和建议能力。具体来说，我需要实现以下核心功能：

1.  **基于DEEPSEEK的健康数据解读与建议生成**：
    *   **用户视角**：作为一名关注健康的用户，我希望在系统中输入我的身体质量指数（BMI）、基础代谢率（BMR）和每日总能量消耗（TDEE）等关键健康指标后，系统能够通过DEEPSEEK模型深入分析这些数据，并为我提供通俗易懂的解读以及个性化的、可操作的健康建议。这些建议应涵盖饮食、运动及生活方式调整等方面。
    *   **开发者视角**：我需要构建一个能够有效调用DEEPSEEK模型API的模块。该模块应能接收用户的健康指标数据，构造合适的提示（Prompt）以引导DEEPSEEK模型进行分析，并解析模型返回的建议内容，最终以友好的方式呈现给用户。

2.  **DEEPSEEK模型调用实验与优化**：
    *   **开发者视角**：为了确保健康建议的质量和模型的成本效益，我需要一个灵活的实验环境。在这个环境中，我可以方便地测试不同的DEEPSEEK模型版本、调整提示策略、比较不同参数下的输出结果，并对模型的调用方式进行优化，以达到最佳的性能和用户体验。

这些用户故事将指导我们通过TDD的方式，逐步构建和完善AI个性化健康顾问系统中与LLM交互的核心功能。

## 工具包说明

本练习系列使用的`utils_llm`工具包提供以下核心功能：

1. **基础对话功能**
   - `chat_gpt_plain`: 基础文本对话
   - `chat_gpt_json`: 结构化JSON响应

2. **多模态支持**
   - `get_gpt_messages_multimodal`: 多模态消息构造
   - `upload_image_to_cloud`: 图片上传服务

3. **模型管理**
   - `get_client_by_model`: 模型客户端选择
   - 支持多种模型：GPT、Qwen、**Deepseek**等

4. **工具特性**
   - 内置重试机制
   - 错误处理
   - 响应解析
   - 类型检查

## 基础结构说明

本实践遵循标准的TDD练习框架结构：

### 命名规范

1. **特性名称 (feature_name)**：
   - 格式：`小写字母_用下划线分隔`
   - 示例：`deepseek_health_recommendation`, `deepseek_experiment_platform`
   - 要求：描述性、简洁、表明功能

2. **目录命名**：
   - 练习系列目录：`ExTDD_XX_FeatureName`
     - XX：两位数字编号（01、02等）
     - FeatureName：驼峰式命名
     - 示例：`ExTDD_01_DeepSeekHealthRecommendation`

3. **文件命名**：
   - 思考文件：`_s{step}_{type}_{feature_name}.md`
   - 代码文件：`{feature_name}.py`
   - 测试文件：`test_{feature_name}.py`
   - 文档文件：`doc_{feature_name}.md`

### 目录结构规范

每个练习系列都必须包含：

```
ExTDD_XX_FeatureName/
├── constraints/                    # 约束条件
│   └── task_constraints.md        # 任务特定约束
├── inputs/                        # 输入文件
│   └── user_story.md             # 用户故事
├── outputs/                       # 输出文件
│   ├── _s1_think_options_{feature_name}.md
│   ├── _s2_think_design_{feature_name}.md
│   ├── _s3_think_validation_{feature_name}.md
│   ├── {feature_name}.py
│   ├── test_{feature_name}.py
│   └── doc_{feature_name}.md
└── README.md                      # 练习说明
```

## LLM API调用特定实现 (AI个性化健康顾问)

### 1. ExTDD_01_DeepSeekHealthRecommendation: 基于DEEPSEEK的健康推荐

feature_name: `deepseek_health_recommendation`

```
ExTDD_01_DeepSeekHealthRecommendation/
├── constraints/
│   └── task_constraints.md        # DEEPSEEK健康推荐的特定约束
├── inputs/
│   └── user_story.md             # DEEPSEEK健康推荐的用户故事
└── outputs/
    ├── _s1_think_options_deepseek_health_recommendation.md
    ├── _s2_think_design_deepseek_health_recommendation.md
    ├── _s3_think_validation_deepseek_health_recommendation.md
    ├── deepseek_health_recommendation.py
    ├── test_deepseek_health_recommendation.py
    └── doc_deepseek_health_recommendation.md
```

#### 核心用户需求 (ExTDD_01_DeepSeekHealthRecommendation)
> 作为用户，我希望输入我的BMI、BMR、TDEE数据后，系统能通过DEEPSEEK模型分析这些数据，并给出针对性的健康指导和生活方式建议。
> 作为开发者，我需要构建一个模块，该模块能够接收用户的健康指标，构造合适的提示调用DEEPSEEK模型，并解析返回的建议。

### 2. ExTDD_02_DeepSeekExperimentPlatform: DEEPSEEK模型调用实验平台

feature_name: `deepseek_experiment_platform`

```
ExTDD_02_DeepSeekExperimentPlatform/
├── constraints/
│   └── task_constraints.md        # DEEPSEEK实验平台的特定约束
├── inputs/
│   └── user_story.md             # DEEPSEEK实验平台的用户故事
└── outputs/
    ├── _s1_think_options_deepseek_experiment_platform.md
    ├── _s2_think_design_deepseek_experiment_platform.md
    ├── _s3_think_validation_deepseek_experiment_platform.md
    ├── deepseek_experiment_platform.py
    ├── test_deepseek_experiment_platform.py
    └── doc_deepseek_experiment_platform.md
```

#### 核心用户需求 (ExTDD_02_DeepSeekExperimentPlatform)
> 作为开发者，我需要一个灵活的环境来测试不同的DEEPSEEK模型、提示策略和参数，以便优化健康建议的质量和调用成本。

## 通用约束

1. 环境配置
   - 所有练习都需要正确配置环境变量，特别是 `DEEPSEEK_API_KEY`。
   - 使用.env文件管理API密钥。
   - 遵循最佳安全实践。

2. 错误处理
   - 所有API调用都需要适当的错误处理。
   - 实现重试机制。
   - 提供清晰的错误信息。

3. 测试要求
   - 单元测试覆盖核心功能。
   - 模拟外部API调用（DEEPSEEK API）。
   - 测试不同的输入数据和错误场景。

4. 文档要求
   - 清晰的API文档。
   - 使用示例，说明如何传入BMI, BMR, TDEE等数据。
   - 性能和限制说明。

## 建议学习顺序

1. 从`ExTDD_01_DeepSeekHealthRecommendation`开始，掌握使用DEEPSEEK模型根据健康数据生成推荐的基本流程。
2. 通过`ExTDD_02_DeepSeekExperimentPlatform`学习如何构建灵活的测试和优化环境，以改进模型调用效果。

每个练习都会逐步增加复杂度，帮助学习者全面理解如何将LLM（特别是DEEPSEEK）应用于实际的健康顾问场景中。

## 技术依赖

1. **Python环境**
   - Python 3.8+
   - pip 包管理器

2. **核心依赖包**
   ```
   openai>=1.0.0  # utils_llm可能依赖此包的结构或接口
   python-dotenv
   tenacity
   httpx
   rich
   json-repair
   # 根据utils_llm/requirements.txt的具体内容，可能还有其他依赖
   ```

3. **环境变量**
   ```
   DEEPSEEK_API_KEY=your_deepseek_api_key
   # 其他在 utils_llm 中可能需要的环境变量，如OPENAI_API_KEY等，根据实际使用情况配置
   # 例如，如果utils_llm的get_client_by_model也支持其他模型，可能需要配置它们的KEY
   OPENAI_API_KEY=your_openai_key # (如果需要对比或备用)
   # ... 其他模型API Key ...
   ```

## 练习难度递进

1. **ExTDD_01_DeepSeekHealthRecommendation**
   - 基础难度：★★★☆☆
   - 重点：调用DEEPSEEK API，处理特定领域（健康指标）的输入，生成结构化或半结构化的建议。
   - 依赖：基础环境配置，DEEPSEEK API密钥。

2. **ExTDD_02_DeepSeekExperimentPlatform**
   - 基础难度：★★★★☆
   - 重点：构建可配置的调用流程，实现不同模型/提示/参数的对比测试，结果评估。
   - 依赖：ExTDD_01的基础功能，对LLM评估有一定理解。