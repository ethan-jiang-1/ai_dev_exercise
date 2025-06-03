import pytest
import os
from dotenv import load_dotenv

# Load .env file for API keys
env_path = os.path.join(os.path.dirname(__file__), "../../../.env")
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv() # Fallback

from ai_wellness_advisor.src.llm_integration.deepseek_api_setup import get_simple_bmi_advice_from_deepseek, SimpleBMIAdvice
from openai import AuthenticationError

# Test with a few different BMI values to see varying advice (optional, one is enough for API check)
@pytest.mark.parametrize("bmi_value, description", [
    (17.0, "underweight"),
    (22.0, "normal weight"),
    (27.0, "overweight"),
    (32.0, "obese")
])
def test_live_get_simple_bmi_advice(bmi_value, description):
    """
    Live integration test for get_simple_bmi_advice_from_deepseek.
    Requires DEEPSEEK_API_KEY to be set.
    """
    print(f"\nTesting BMI advice for: {bmi_value} ({description})")
    print(f"DEEPSEEK_API_KEY available: {'DEEPSEEK_API_KEY' in os.environ}")
    
    try:
        result = get_simple_bmi_advice_from_deepseek(bmi_value=bmi_value)
        
        assert isinstance(result, SimpleBMIAdvice), \
            f"Response should be an instance of SimpleBMIAdvice, but got {type(result)}. Response: {result}"
        assert result.advice is not None, "Advice text should not be None"
        assert len(result.advice.strip()) > 0, "Advice text should not be empty"
        
        print(f"Successfully received advice for BMI {bmi_value} ({description}):")
        print(f"Advice: {result.advice[:200]}..." if len(result.advice) > 200 else result.advice)

    except AuthenticationError as e:
        pytest.fail(f"AuthenticationError for BMI {bmi_value} ({description}): {e}. Check DEEPSEEK_API_KEY.")
    except Exception as e:
        # If it was a dict error from our function, print details
        if isinstance(result, dict) and result.get("error"):
             pytest.fail(f"API call failed for BMI {bmi_value} ({description}). Error type: {result.get('type')}, Details: {result.get('details')}")
        else:
            pytest.fail(f"Unexpected error for BMI {bmi_value} ({description}): {e}. Result was: {result}")

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    dotenv_path = os.path.join(project_root, ".env")
    print(f"Attempting to load .env from: {dotenv_path}")
    if load_dotenv(dotenv_path=dotenv_path, override=True):
        print(".env loaded successfully for __main__ execution.")
    else:
        print("Failed to load .env or it does not exist.")

    # Run pytest for this file, with -s to show prints, -v for verbose test names
    # and -k to run a specific BMI test if needed, e.g., -k "22.0"
    pytest.main(["-s", "-v", __file__]) 