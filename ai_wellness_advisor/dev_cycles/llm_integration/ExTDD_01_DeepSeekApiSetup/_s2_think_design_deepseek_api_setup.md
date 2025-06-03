# S2: 设计方案 - DEEPSEEK API基础配置与调用验证 (deepseek_api_setup)

## 1. 目标
设计一个Python模块/函数，实现与DeepSeek API的基础通信，获取并验证一个简单的JSON响应。

## 2. 模块/函数设计

**模块名**: `deepseek_api_setup.py` (位于 `{app_name}/src/llm_integration/`)

**核心函数签名**: `call_deepseek_simple_json()`

```python
from typing import Union, Dict, Any
from pydantic import BaseModel, ValidationError
import os # For DEEPSEEK_MODEL_NAME, if we make it configurable via env

# utils_llm components that will be used
from utils_llm.llm_base import get_deepseek_client, chat_gpt_json, jsons_load_repair # jsons_load_repair might be used by chat_gpt_json internally
from openai import APIError, APITimeoutError, APIConnectionError, RateLimitError, AuthenticationError, BadRequestError # Common OpenAI exceptions

# --- Pydantic Model Definition ---
class SimpleDeepSeekResponse(BaseModel):
    status: str
    message: str

# --- Configuration (Optional, can be passed as arg or defaulted) ---
DEEPSEEK_MODEL_NAME = os.getenv("DEEPSEEK_CHAT_MODEL", "deepseek-chat") 

# --- Core Function --- 
def call_deepseek_simple_json(model_name: str = DEEPSEEK_MODEL_NAME) -> Union[SimpleDeepSeekResponse, Dict[str, Any]]:
    """
    Calls the DeepSeek API via utils_llm.chat_gpt_json with a simple prompt 
    expecting a JSON response, then validates it using Pydantic.

    Args:
        model_name (str): The name of the DeepSeek model to use.

    Returns:
        Union[SimpleDeepSeekResponse, Dict[str, Any]]: 
            Pydantic model instance if successful, or a dictionary with error info.
    """
    try:
        # 1. Get DeepSeek client (utils_llm handles API key loading via load_dotenv and os.getenv)
        client = get_deepseek_client()

        # 2. Define a simple prompt that asks for a JSON response.
        #    This prompt is crucial for instructing the model to return JSON.
        prompt_messages = [
            {"role": "system", "content": "You are an assistant that only responds in valid JSON format. Do not include any explanatory text outside the JSON structure."},
            {"role": "user", "content": "Please provide a JSON object with a 'status' field set to 'ok' and a 'message' field set to 'Hello from DeepSeek!'"}
        ]

        # 3. Make the API call using chat_gpt_json from utils_llm
        #    chat_gpt_json handles retries, response_format={'type': 'json_object'}, and json_repair internally.
        response_dict = chat_gpt_json(
            messages=prompt_messages,
            model=model_name, 
            client=client,
            temperature=0.1 # Low temperature for predictable JSON output
        )

        # 4. Validate the JSON response (which is already a dict) using Pydantic
        #    chat_gpt_json returns a dict after json_repair.
        validated_response = SimpleDeepSeekResponse(**response_dict)
        return validated_response

    except AuthenticationError as e:
        # Handles issues like missing or invalid API key if not caught by get_deepseek_client itself
        return {"error": True, "type": "authentication_error", "details": str(e)}
    except RateLimitError as e:
        return {"error": True, "type": "rate_limit_error", "details": str(e)}
    except (APIConnectionError, APITimeoutError) as e:
        return {"error": True, "type": "network_error", "details": str(e)}
    except BadRequestError as e: # e.g. model not found, invalid request structure by OpenAI standards
        return {"error": True, "type": "bad_request_error", "details": str(e)}
    except APIError as e: # General API error from OpenAI/DeepSeek
        return {"error": True, "type": "api_error", "details": str(e)}
    except ValidationError as e:
        # This catches Pydantic validation errors if the dict from chat_gpt_json doesn't match the model
        return {"error": True, "type": "pydantic_validation_error", "details": e.errors(), "raw_response": response_dict if 'response_dict' in locals() else 'Unknown'}
    except Exception as e: # Catch-all for other unexpected errors during the process
        # This could include errors from chat_gpt_json not fitting other specific exceptions,
        # or issues within this function's logic.
        return {"error": True, "type": "unexpected_error", "details": str(e)}

```

## 3. 关键组件与依赖

*   **`utils_llm.llm_base`**: 
    *   `get_deepseek_client()`: Used to obtain the configured DeepSeek client. Handles API key loading via `os.getenv` internally (after `load_dotenv()` is called at module level in `llm_base`).
    *   `chat_gpt_json()`: Core function for making the call. It handles client instantiation (if not provided), `response_format`, JSON repair, and retries.
*   **`pydantic`**: For defining `SimpleDeepSeekResponse` and validating the dictionary returned by `chat_gpt_json`.
*   **`openai` client exceptions**: `AuthenticationError`, `RateLimitError`, `APIConnectionError`, `APITimeoutError`, `BadRequestError`, `APIError` will be caught if raised by the client interactions within `chat_gpt_json` or by `get_deepseek_client`.

## 4. 错误处理策略
*   The function `call_deepseek_simple_json` will catch exceptions from `chat_gpt_json` (which itself handles retries and some parsing).
*   Specific OpenAI exceptions (`AuthenticationError`, `RateLimitError`, etc.) will be caught and translated into a structured error dictionary.
*   `pydantic.ValidationError` will be caught if the data returned by `chat_gpt_json` (after its internal `json_repair`) does not conform to `SimpleDeepSeekResponse`.
*   A general `Exception` catch-all is included for unforeseen issues.
*   Successful calls return a `SimpleDeepSeekResponse` instance.
*   Failed calls return a dictionary: `{"error": True, "type": "error_type", "details": ...}`.

## 5. `.env` File Example
```
DEEPSEEK_API_KEY="your_actual_api_key_here"
# Optional: DEEPSEEK_MODEL_NAME="deepseek-chat"
```

## 6. 预期交互流程
1.  Application/Test calls `call_deepseek_simple_json()`.
2.  Function attempts to load API key and initialize client.
3.  Function sends request to DeepSeek.
4.  Function receives response.
5.  Function parses and validates response against `SimpleDeepSeekResponse`.
6.  Returns Pydantic object on success, or error dictionary on failure. 