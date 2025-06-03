# S1: 思考与选项分析 - DEEPSEEK API基础配置与调用验证 (deepseek_api_setup)

## 1. 核心目标
确保DEEPSEEK API调用通路完全畅通，所有相关配置正确，并能成功获取一个简单的、结构化的JSON格式输出，使用Pydantic进行验证。

## 2. 关键问题与考量点

### 2.1. API密钥管理与加载
*   **选项1**: 直接在代码中硬编码 (不推荐，仅为快速测试)。
*   **选项2**: 使用 `.env` 文件和 `python-dotenv` 加载 (推荐)。
*   **选项3**: 通过环境变量由部署环境注入。
*   **决策**: 遵循项目通用约束，使用 `.env` 和 `python-dotenv`，并通过 `utils_llm` (如果其封装了加载逻辑) 或直接加载。

### 2.2. `utils_llm` 工具包的利用
*   **确认**: `utils_llm.llm_base` 提供了 `get_deepseek_client()` 方法，以及更通用的 `get_client_by_model(model_name)`。
*   **确认**: `utils_llm.llm_base` 提供了 `chat_gpt_json()` 函数，该函数可以:
    *   接收一个 `client` 参数 (我们可以传入DeepSeek client)。
    *   在内部调用 `client.chat.completions.create` 时使用 `response_format={"type": "json_object"}`。
    *   使用 `json_repair.repair_json()` 处理响应。
    *   包含重试逻辑。
*   **决策**: 我们将优先使用 `utils_llm.chat_gpt_json()` 配合 `get_deepseek_client()` 或 `get_client_by_model()`. 这将极大简化 `deepseek_api_setup` 的实现。

### 2.3. 构造简单请求
*   **模型选择**: `deepseek-chat` (如 `exam_deepseek.py` 中所示) 是一个合适的初始测试模型。
*   **Prompt内容**: 一个极其简单的、期望返回JSON的prompt。例如："请返回一个JSON对象，包含键 'status' 值为 'ok'，和键 'message' 值为 'Hello DeepSeek!'"。
*   **请求参数**: `model`, `messages`, `temperature` (设低一些，如0.1，确保输出稳定), `max_tokens`。

### 2.4. 处理响应
*   **成功响应**: 解析JSON字符串。
*   **错误响应**: API返回的错误码和错误信息如何捕获和展示？（例如401 API Key错误，429速率限制，500服务器错误）
*   **网络问题**: 如何处理连接超时等网络异常？(`httpx` 的异常处理)

### 2.5. Pydantic模型验证
*   **模型定义**: 定义一个简单的Pydantic模型，例如：
    ```python
    from pydantic import BaseModel

    class DeepSeekResponse(BaseModel):
        status: str
        message: str
    ```
*   **验证逻辑**: 用获取的JSON数据实例化Pydantic模型，捕获 `ValidationError`。

### 2.6. 输出结构
*   **成功**: 返回Pydantic模型实例或其`dict()`形式。
*   **失败**: 返回明确的错误信息或抛出自定义异常。

## 3. 初步方案选择
1.  `DEEPSEEK_API_KEY` 将由 `utils_llm.get_deepseek_client()` (内部调用 `os.getenv`) 负责加载，前提是根目录存在 `.env` 文件且已执行 `load_dotenv()` (由 `utils_llm.llm_base` 在导入时完成)。
2.  使用 `utils_llm.get_deepseek_client()` 获取DeepSeek客户端实例。
3.  调用 `utils_llm.chat_gpt_json()` 函数，传入DeepSeek客户端、选定的模型 (`deepseek-chat`) 以及一个要求简单JSON输出的 `messages` 列表。
4.  `chat_gpt_json` 内部已包含对API调用异常的捕获和重试逻辑。我们需要关注的是 `chat_gpt_json` 可能抛出的最终异常 (如 `ValueError` for empty messages, `openai.BadRequestError`) 或返回的成功/失败结果。
5.  使用Pydantic模型解析和验证从 `chat_gpt_json` 返回的字典。
6.  我们的函数/模块将返回Pydantic模型实例或一个包含错误信息的字典。 