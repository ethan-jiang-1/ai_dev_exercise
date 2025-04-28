# User Story: LLM API调用练习系列

> **工作目录说明**：本文档位于 `~/ai_dev_exercise/exercise_tdd_llm/` 目录下，所有文件引用路径均基于此目录。例如，`./teaching_framework/test_driven_development_with_ai.md` 实际指向 `/Users/bowhead/ai_dev_exercise/exercise_tdd_llm/teaching_framework/test_driven_development_with_ai.md`。

(核心开发理念参考: [测试驱动开发核心理念](./teaching_framework/test_driven_development_with_ai.md))
(练习框架规划参考: [TDD练习框架设计规划](./teaching_framework/planning_tdd_exercise_template.md))

## 1. User Story (用户故事)

# LLM API调用：AI+TDD练习故事实例

> **重要约束**：
> 1. 在整个故事实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。
> 2. 本练习系列使用项目根目录中的`utils_llm`工具包，所有练习都需要正确配置相关环境变量。
> 3. 在开始练习前，请确保已经正确设置了所有必要的API密钥和环境变量。

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
   - 支持多种模型：GPT、Qwen、Deepseek等

4. **工具特性**
   - 内置重试机制
   - 错误处理
   - 响应解析
   - 类型检查

## 基础结构说明

本故事遵循标准的TDD练习框架结构：

### 命名规范

1. **特性名称 (feature_name)**：
   - 格式：`小写字母_用下划线分隔`
   - 示例：`basic_chat`, `json_response`, `multi_modal`
   - 要求：描述性、简洁、表明功能

2. **目录命名**：
   - 练习系列目录：`ExTDD_XX_FeatureName`
     - XX：两位数字编号（01、02等）
     - FeatureName：驼峰式命名
     - 示例：`ExTDD_01_BasicChat`

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

## LLM API调用特定实现

### 1. ExTDD_01_BasicChat: 基础文本对话

feature_name: basic_chat

```
ExTDD_01_BasicChat/
├── constraints/
│   └── task_constraints.md        # 基础对话的特定约束
├── inputs/
│   └── user_story.md             # 基础对话的用户故事
└── outputs/
    ├── _s1_think_options_basic_chat.md
    ├── _s2_think_design_basic_chat.md
    ├── _s3_think_validation_basic_chat.md
    ├── basic_chat.py
    ├── test_basic_chat.py
    └── doc_basic_chat.md
```

#### 特定需求
- 实现基础的文本对话功能
- 处理系统提示词和用户提示词
- 支持参数调优（temperature和top_p）
- 实现错误处理和重试机制

#### 技术要点
- 使用`chat_gpt_plain`函数
- 提示词工程和优化
- 参数配置管理
- 错误处理策略

#### 验收标准
- 成功调用LLM API并获取响应
- 正确处理各类错误情况
- 合理的参数配置效果
- 稳定的重试机制

### 2. ExTDD_02_JSONResponse: 结构化JSON响应

feature_name: json_response

```
ExTDD_02_JSONResponse/
├── constraints/
│   └── task_constraints.md        # JSON响应的特定约束
├── inputs/
│   └── user_story.md             # JSON响应的用户故事
└── outputs/
    ├── _s1_think_options_json_response.md
    ├── _s2_think_design_json_response.md
    ├── _s3_think_validation_json_response.md
    ├── json_response.py
    ├── test_json_response.py
    └── doc_json_response.md
```

#### 特定需求
- 获取结构化的JSON格式响应
- 处理JSON解析和验证
- 实现类型转换和验证
- 处理JSON修复机制

#### 技术要点
- 使用`chat_gpt_json`函数
- JSON Schema定义和验证
- 错误修复策略
- 类型系统集成

#### 验收标准
- 正确的JSON格式响应
- 可靠的类型转换
- 有效的错误修复
- 完整的验证覆盖

### 3. ExTDD_03_MultiModal: 多模态对话

feature_name: multi_modal

```
ExTDD_03_MultiModal/
├── constraints/
│   └── task_constraints.md        # 多模态对话的特定约束
├── inputs/
│   └── user_story.md             # 多模态对话的用户故事
└── outputs/
    ├── _s1_think_options_multi_modal.md
    ├── _s2_think_design_multi_modal.md
    ├── _s3_think_validation_multi_modal.md
    ├── multi_modal.py
    ├── test_multi_modal.py
    └── doc_multi_modal.md
```

#### 特定需求
- 处理图片和文本的多模态输入
- 管理图片上传和URL生成
- 构造多模态消息
- 处理多模态响应

#### 技术要点
- 使用`get_gpt_messages_multimodal`
- 云存储集成（OSS/TOS）
- 多模态消息格式
- 响应解析策略

#### 验收标准
- 成功的图片处理
- 正确的多模态消息构造
- 可靠的云存储交互
- 准确的响应解析

### 4. ExTDD_04_ModelSelector: 模型选择器

feature_name: model_selector

```
ExTDD_04_ModelSelector/
├── constraints/
│   └── task_constraints.md        # 模型选择的特定约束
├── inputs/
│   └── user_story.md             # 模型选择的用户故事
└── outputs/
    ├── _s1_think_options_model_selector.md
    ├── _s2_think_design_model_selector.md
    ├── _s3_think_validation_model_selector.md
    ├── model_selector.py
    ├── test_model_selector.py
    └── doc_model_selector.md
```

#### 特定需求
- 实现智能模型选择
- 管理多个模型客户端
- 实现降级策略
- 监控模型性能

#### 技术要点
- 使用`get_client_by_model`
- 模型特性比较
- 性能指标收集
- 降级策略实现

#### 验收标准
- 准确的模型选择
- 有效的性能监控
- 可靠的降级机制
- 合理的资源利用

### 5. ExTDD_05_Conversation: 对话管理器

feature_name: conversation

```
ExTDD_05_Conversation/
├── constraints/
│   └── task_constraints.md        # 对话管理的特定约束
├── inputs/
│   └── user_story.md             # 对话管理的用户故事
└── outputs/
    ├── _s1_think_options_conversation.md
    ├── _s2_think_design_conversation.md
    ├── _s3_think_validation_conversation.md
    ├── conversation.py
    ├── test_conversation.py
    └── doc_conversation.md
```

#### 特定需求
- 管理对话历史
- 实现上下文窗口控制
- 提供记忆机制
- 支持会话持久化

#### 技术要点
- 对话历史数据结构
- 上下文长度控制
- 记忆策略实现
- 持久化机制

#### 验收标准
- 可靠的历史管理
- 有效的上下文控制
- 准确的记忆提取
- 稳定的持久化存储

## 通用约束

1. 环境配置
   - 所有练习都需要正确配置环境变量
   - 使用.env文件管理API密钥
   - 遵循最佳安全实践

2. 错误处理
   - 所有API调用都需要适当的错误处理
   - 实现重试机制
   - 提供清晰的错误信息

3. 测试要求
   - 单元测试覆盖核心功能
   - 模拟外部API调用
   - 测试不同的错误场景

4. 文档要求
   - 清晰的API文档
   - 使用示例
   - 性能和限制说明

## 建议学习顺序

1. 从`ExTDD_01_BasicChat`开始，掌握基本的API调用
2. 通过`ExTDD_02_JSONResponse`学习结构化数据处理
3. 在`ExTDD_03_MultiModal`中扩展到多模态能力
4. 使用`ExTDD_04_ModelSelector`学习模型选择和管理
5. 最后通过`ExTDD_05_Conversation`掌握完整的对话管理

每个练习都会逐步增加复杂度，帮助学习者全面理解LLM API的使用。

## 技术依赖

1. **Python环境**
   - Python 3.8+
   - pip 包管理器

2. **核心依赖包**
   ```
   openai>=1.0.0
   python-dotenv
   tenacity
   httpx
   rich
   json-repair
   ```

3. **环境变量**
   ```
   # OpenAI/Azure配置
   OPENAI_API_KEY=your_key
   OPENAI_BASE_URL=your_url
   AZURE_OPENAI_VERSION=your_version

   # 阿里云配置（用于图片上传）
   OSS_ACCESS_KEY=your_key
   OSS_ACCESS_SECRET=your_secret
   OSS_BUCKET=your_bucket
   OSS_ENDPOINT=your_endpoint

   # 其他模型配置
   DASHSCOPE_API_KEY=your_key
   ARK_API_KEY=your_key
   DEEPSEEK_API_KEY=your_key
   SF_API_KEY=your_key
   ```

## 练习难度递进

每个练习都建立在前一个练习的基础上，逐步增加复杂度：

1. **ExTDD_01_BasicChat**
   - 基础难度：★★☆☆☆
   - 重点：基本API调用和错误处理
   - 依赖：基础环境配置

2. **ExTDD_02_JSONResponse**
   - 基础难度：★★★☆☆
   - 重点：结构化数据处理
   - 依赖：ExTDD_01的基础功能

3. **ExTDD_03_MultiModal**
   - 基础难度：★★★★☆
   - 重点：多模态处理和云存储
   - 依赖：ExTDD_01的对话功能

4. **ExTDD_04_ModelSelector**
   - 基础难度：★★★★☆
   - 重点：模型管理和性能优化
   - 依赖：前三个练习的经验

5. **ExTDD_05_Conversation**
   - 基础难度：★★★★★
   - 重点：复杂状态管理
   - 依赖：所有前序练习的功能 