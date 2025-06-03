from typing import Union, Dict, Any
from pydantic import BaseModel, ValidationError
import os

# Attempt to import from utils_llm. If this structure causes issues later with pytest discovery
# or pathing in a non-package context, we might need to adjust how utils_llm is referenced or packaged.
# For now, assume utils_llm is in PYTHONPATH or structured as a discoverable package.
from utils_llm.llm_base import get_deepseek_client, chat_gpt_json
from openai import APIError, APITimeoutError, APIConnectionError, RateLimitError, AuthenticationError, BadRequestError

class SimpleDeepSeekResponse(BaseModel):
    status: str
    message: str

class SimpleBMIAdvice(BaseModel):
    advice: str

DEEPSEEK_MODEL_NAME = os.getenv("DEEPSEEK_CHAT_MODEL", "deepseek-chat")

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
        client = get_deepseek_client()

        prompt_messages = [
            {"role": "system", "content": "You are an assistant that only responds in valid JSON format. Do not include any explanatory text outside the JSON structure."},
            {"role": "user", "content": "Please provide a JSON object with a 'status' field set to 'ok' and a 'message' field set to 'Hello from DeepSeek!'"}
        ]

        response_dict = chat_gpt_json(
            messages=prompt_messages,
            model=model_name, 
            client=client,
            temperature=0.1
        )
        
        validated_response = SimpleDeepSeekResponse(**response_dict)
        return validated_response

    except AuthenticationError as e:
        return {"error": True, "type": "authentication_error", "details": str(e)}
    except RateLimitError as e:
        return {"error": True, "type": "rate_limit_error", "details": str(e)}
    except (APIConnectionError, APITimeoutError) as e:
        return {"error": True, "type": "network_error", "details": str(e)}
    except BadRequestError as e:
        return {"error": True, "type": "bad_request_error", "details": str(e)}
    except APIError as e:
        return {"error": True, "type": "api_error", "details": str(e)}
    except ValidationError as e:
        # Capture the response_dict if it exists for raw_response, otherwise provide a placeholder
        raw_resp_for_error = response_dict if 'response_dict' in locals() else 'Response dictionary not available before validation.'
        return {"error": True, "type": "pydantic_validation_error", "details": e.errors(), "raw_response": raw_resp_for_error}
    except Exception as e:
        return {"error": True, "type": "unexpected_error", "details": str(e)}

def get_simple_bmi_advice_from_deepseek(bmi_value: float, model_name: str = DEEPSEEK_MODEL_NAME) -> Union[SimpleBMIAdvice, Dict[str, Any]]:
    """
    Calls the DeepSeek API to get general health advice for a given BMI value.
    Expects a JSON response with an 'advice' key.

    Args:
        bmi_value (float): The BMI value to get advice for.
        model_name (str): The name of the DeepSeek model to use.

    Returns:
        Union[SimpleBMIAdvice, Dict[str, Any]]:
            Pydantic model instance if successful, or a dictionary with error info.
    """
    try:
        client = get_deepseek_client()

        prompt_messages = [
            {"role": "system", "content": "You are a helpful AI health advisor. Respond ONLY in valid JSON format with a single key 'advice' containing your health advice. Do not include any explanatory text outside the JSON structure."},
            {"role": "user", "content": f"My BMI is {bmi_value:.1f}. Please provide general health advice based on this BMI."}
        ]

        response_dict = chat_gpt_json(
            messages=prompt_messages,
            model=model_name,
            client=client,
            temperature=0.7 # Allow for more diverse advice
        )
        
        validated_response = SimpleBMIAdvice(**response_dict)
        return validated_response

    except AuthenticationError as e:
        return {"error": True, "type": "authentication_error", "details": str(e)}
    except RateLimitError as e:
        return {"error": True, "type": "rate_limit_error", "details": str(e)}
    except (APIConnectionError, APITimeoutError) as e:
        return {"error": True, "type": "network_error", "details": str(e)}
    except BadRequestError as e:
        return {"error": True, "type": "bad_request_error", "details": str(e)}
    except APIError as e:
        return {"error": True, "type": "api_error", "details": str(e)}
    except ValidationError as e:
        raw_resp_for_error = response_dict if 'response_dict' in locals() else 'Response dictionary not available before validation.'
        return {"error": True, "type": "pydantic_validation_error", "details": e.errors(), "raw_response": raw_resp_for_error}
    except Exception as e:
        return {"error": True, "type": "unexpected_error", "details": str(e)}

if __name__ == '__main__':
    # Example usage, requires .env file with DEEPSEEK_API_KEY
    # Ensure load_dotenv() has been called (it's called when utils_llm.llm_base is imported)
    print("Attempting to call DeepSeek API...")
    
    # For this direct script execution to find utils_llm, ensure the project root is in PYTHONPATH
    # or run this script with `python -m ai_wellness_advisor.src.llm_integration.deepseek_api_setup` from the project root.
    # Alternatively, adjust sys.path here for standalone testing (not recommended for final code).
    
    # import sys
    # import os
    # # Add project root to sys.path for utils_llm discovery if run directly
    # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')) 
    # if project_root not in sys.path:
    #     sys.path.insert(0, project_root)
    
    # from utils_llm.llm_base import load_dotenv # Explicitly ensure dotenv is loaded if not by prior import
    # load_dotenv() # Call it if utils_llm might not have been fully initialized in this context

    result = call_deepseek_simple_json()
    
    if isinstance(result, SimpleDeepSeekResponse):
        print("Success!")
        print(f"Status: {result.status}")
        print(f"Message: {result.message}")
    elif isinstance(result, dict) and result.get("error"):
        print(f"Error Type: {result.get('type')}")
        print(f"Details: {result.get('details')}")
        if 'raw_response' in result:
            print(f"Raw Response: {result.get('raw_response')}")
    else:
        print(f"Unexpected result format: {result}") 