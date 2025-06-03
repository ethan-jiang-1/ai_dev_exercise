# S3: 验证方法与结果 - DEEPSEEK API基础配置与调用验证 (deepseek_api_setup)

## 1. 目标
定义如何验证 `call_deepseek_simple_json()` 函数是否按预期工作，覆盖成功和失败场景。这包括纯粹的mock测试和一次真实的API调用测试。

## 2. 测试策略
将使用 `pytest` 框架编写单元测试。核心依赖 `unittest.mock` 来模拟对 `utils_llm` 组件的调用和环境变量。

*   **Category 1: Mocked Tests**
    *   文件: `ai_wellness_advisor/tests/llm_integration/test_deepseek_api_setup.py`
    *   目的: 严格单元测试 `call_deepseek_simple_json` 的逻辑，不执行实际API调用。
*   **Category 2: Live API Call Test**
    *   文件: `ai_wellness_advisor/tests/llm_integration/test_deepseek_api_setup_live.py`
    *   目的: 验证与实际DeepSeek API的端到端通信，获取简单JSON响应。会被标记以便选择性执行。

## 3. Category 1: Mocked Test Cases (for `test_deepseek_api_setup.py`)

### 3.1. 成功场景
*   **`test_call_deepseek_successful_response(mock_chat_gpt_json, mock_get_deepseek_client)`**:
    *   **Arrange**:
        *   Mock `utils_llm.llm_base.get_deepseek_client` to return a dummy client object (or a MagicMock).
        *   Mock `utils_llm.llm_base.chat_gpt_json` to return a dictionary matching `SimpleDeepSeekResponse` (e.g., `{"status": "ok", "message": "Hello from DeepSeek!"}`).
    *   **Act**: Call `call_deepseek_simple_json()`.
    *   **Assert**:
        *   `get_deepseek_client`被调用一次。
        *   `chat_gpt_json` 被以正确的参数（包括模型名、prompt messages、DeepSeek client）调用一次。
        *   返回的是 `SimpleDeepSeekResponse` 的实例。
        *   实例的 `status` 和 `message` 字段与预期一致。

### 3.2. `utils_llm` 错误场景 (模拟 `chat_gpt_json` 或 `get_deepseek_client` 抛出异常)
*   **`test_call_deepseek_auth_error(mock_chat_gpt_json, mock_get_deepseek_client)`**:
    *   **Arrange**: Mock `utils_llm.llm_base.get_deepseek_client` (或 `utils_llm.llm_base.chat_gpt_json`，取决于哪里更适合模拟认证失败) to raise `openai.AuthenticationError("Invalid API Key")`.
    *   **Act**: Call `call_deepseek_simple_json()`.
    *   **Assert**: 返回一个错误字典，`type` 为 `"authentication_error"`，并包含错误详情。
*   **`test_call_deepseek_rate_limit_error(mock_chat_gpt_json, mock_get_deepseek_client)`**:
    *   **Arrange**: Mock `utils_llm.llm_base.chat_gpt_json` to raise `openai.RateLimitError("Rate limit exceeded")`.
    *   **Act**: Call `call_deepseek_simple_json()`.
    *   **Assert**: 返回一个错误字典，`type` 为 `"rate_limit_error"`。
*   **`test_call_deepseek_api_error(mock_chat_gpt_json, mock_get_deepseek_client)`**: (Covers general API errors like 500s)
    *   **Arrange**: Mock `utils_llm.llm_base.chat_gpt_json` to raise `openai.APIError("Server error", status_code=500)`.
    *   **Act**: Call `call_deepseek_simple_json()`.
    *   **Assert**: 返回一个错误字典，`type` 为 `"api_error"`.
*   **`test_call_deepseek_network_error(mock_chat_gpt_json, mock_get_deepseek_client)`**:
    *   **Arrange**: Mock `utils_llm.llm_base.chat_gpt_json` to raise `openai.APIConnectionError("Network issue")`.
    *   **Act**: Call `call_deepseek_simple_json()`.
    *   **Assert**: 返回一个错误字典，`type` 为 `"network_error"`.
*   **`test_call_deepseek_bad_request_error(mock_chat_gpt_json, mock_get_deepseek_client)`**:
    *   **Arrange**: Mock `utils_llm.llm_base.chat_gpt_json` to raise `openai.BadRequestError("Invalid request")`.
    *   **Act**: Call `call_deepseek_simple_json()`.
    *   **Assert**: 返回一个错误字典，`type` 为 `"bad_request_error"`.

### 3.3. Pydantic 验证失败场景
*   **`test_call_deepseek_response_pydantic_validation_error(mock_chat_gpt_json, mock_get_deepseek_client)`**:
    *   **Arrange**:
        *   Mock `utils_llm.llm_base.get_deepseek_client`.
        *   Mock `utils_llm.llm_base.chat_gpt_json` to return a dictionary that will fail Pydantic validation (e.g., `{"statuz": "ok", "msg": "Hello!"}` - misspelled keys, or missing keys).
    *   **Act**: Call `call_deepseek_simple_json()`.
    *   **Assert**: 返回一个错误字典，`type` 为 `"pydantic_validation_error"`，并包含Pydantic的错误详情和原始响应。

### 3.4. 意外错误场景
*   **`test_call_deepseek_unexpected_error(mock_chat_gpt_json, mock_get_deepseek_client)`**:
    *   **Arrange**: Mock `utils_llm.llm_base.chat_gpt_json` to raise a generic `Exception("Something totally unexpected")`.
    *   **Act**: Call `call_deepseek_simple_json()`.
    *   **Assert**: 返回一个错误字典，`type` 为 `"unexpected_error"`.

## 4. Mocking 策略细节 (Category 1)
*   **主要 Mock 对象**: `utils_llm.llm_base.chat_gpt_json`.
    *   `return_value`: 应该是一个字典，`SimpleDeepSeekResponse` 可以成功解析，或者是一个会导致Pydantic验证错误的字典。
    *   `side_effect`: 用于模拟各种 `openai.*Error` 异常或其他通用异常。
*   **辅助 Mock 对象**: `utils_llm.llm_base.get_deepseek_client`.
    *   主要确保它被调用，或用于模拟 `AuthenticationError` (如果API密钥在此阶段未找到)。
*   **环境变量**: 如果我们在 `get_deepseek_client` 之外测试密钥加载逻辑 (尽管当前设计中 `get_deepseek_client` 自己加载密钥)，则可能需要使用 `monkeypatch.setenv` 来处理 `DEEPSEEK_API_KEY`。

## 5. Category 2: Live API Call Test (for `test_deepseek_api_setup_live.py`)

*   **警告**: 此测试执行对DeepSeek API的实际调用，并需要在 `.env` 文件中提供有效的 `DEEPSEEK_API_KEY`。
*   **标记**: 此文件中的测试应进行标记 (例如 `@pytest.mark.live`)，以便可以有选择地运行或跳过它们。

### 5.1. 测试用例
*   **`test_call_deepseek_live_successful_simple_json_response()`**:
    *   **Arrange**: 确保 `DEEPSEEK_API_KEY` 可用 (已从 `.env` 加载)。
    *   **Act**: 调用 `call_deepseek_simple_json(model_name="deepseek-chat")` (或其他合适的模型)。
    *   **Assert**:
        *   检查结果是否为 `SimpleDeepSeekResponse` 的实例。
        *   如果结果是错误字典，测试应失败，并输出错误信息以供诊断 (除非我们希望在实时测试中专门处理某些临时网络问题)。
        *   确保 `result.status == "ok"`。
        *   确保 `result.message == "Hello from DeepSeek!"` (或与 `call_deepseek_simple_json` 中prompt请求的内容一致)。

## 6. 预期测试执行流程 (TDD Cycle)
1.  **Red**: 编写一个或多个Category 1的测试用例。最初它们会失败。
2.  **Green**: 逐步实现 `deepseek_api_setup.py` (`call_deepseek_simple_json`) 的逻辑，直到所有测试用例通过。
3.  **Refactor**: 在测试的保护下重构代码。
4.  重复此过程，直到Category 1中的所有测试都通过。
5.  实现Category 2的测试 (`test_call_deepseek_live_successful_simple_json_response`)。运行它（了解这需要已配置的环境）。这可能需要调整 `call_deepseek_simple_json` 中的prompt，以便从真实模型稳定地获得所需的JSON响应。 