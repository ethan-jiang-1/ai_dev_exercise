import pytest
import os
from dotenv import load_dotenv

# Attempt to load .env file to ensure API keys are available for live tests
# This is particularly important if running the test directly or if pytest isn't loading it.
# utils_llm should also do this, but it's good practice for live tests to ensure environment.
env_path = os.path.join(os.path.dirname(__file__), "../../../.env") # Assuming .env is in the project root
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)
else:
    # Fallback for different structures or if pytest is run from a different root
    load_dotenv() 

# It's good practice to skip live tests if the API key isn't available.
# However, utils_llm.get_deepseek_client() will raise an error if the key is missing,
# which the test can catch or let fail naturally.
# For this exercise, we'll let it fail if the key is not set, as per implied behavior.

from ai_wellness_advisor.src.llm_integration.deepseek_api_setup import call_deepseek_simple_json, SimpleDeepSeekResponse
from openai import AuthenticationError # To potentially catch and provide a better message if API key is an issue

# Marker for pytest to identify live tests, can be used to include/exclude them
# pytest.mark.live = pytest.mark.skipif(
# "DEEPSEEK_API_KEY" not in os.environ, reason="DEEPSEEK_API_KEY not set in environment"
# ) # We will not use this marker for now, to keep it simple as requested

def test_live_call_deepseek_simple_json():
    """
    Live integration test for call_deepseek_simple_json.
    This test makes a real API call to DeepSeek.
    It requires the DEEPSEEK_API_KEY to be set in the environment.
    """
    print(f"DEEPSEEK_API_KEY available: {'DEEPSEEK_API_KEY' in os.environ}")
    
    try:
        result = call_deepseek_simple_json(model_name="deepseek-chat")
        
        assert isinstance(result, SimpleDeepSeekResponse), "Response should be an instance of SimpleDeepSeekResponse"
        assert result.status == "ok", f"Expected status 'ok', but got '{result.status}'"
        assert result.message == "Hello from DeepSeek!", f"Expected message 'Hello from DeepSeek!', but got '{result.message}'"
        print("Live test successful: Received and validated response from DeepSeek.")
        print(f"Response status: {result.status}, message: {result.message}")

    except AuthenticationError as e:
        pytest.fail(f"AuthenticationError during live API call: {e}. Please ensure DEEPSEEK_API_KEY is correctly set in your .env file.")
    except Exception as e:
        pytest.fail(f"An unexpected error occurred during the live API call: {e}")

if __name__ == "__main__":
    # Ensure .env is loaded if running script directly
    # This might be redundant if pytest itself handles it or if the global load_dotenv worked.
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    dotenv_path = os.path.join(project_root, ".env")
    print(f"Attempting to load .env from: {dotenv_path}")
    if load_dotenv(dotenv_path=dotenv_path, override=True): # override ensures it reloads if already loaded
        print(".env loaded successfully for __main__ execution.")
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if api_key:
            print(f"DEEPSEEK_API_KEY found in environment after load: {bool(api_key)}")
        else:
            print("DEEPSEEK_API_KEY not found after .env load.")
    else:
        print("Failed to load .env or it does not exist.")

    # Run pytest for this file
    # Adding -s to show print statements from the test
    pytest.main(["-s", "-v", __file__]) 