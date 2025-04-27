from dotenv import load_dotenv
import rich 
import os

load_dotenv()

from utils_llm.llm_base import get_sf_client, chat_gpt_plain, chat_gpt_json 


def exam_sf_plain():
    client = get_sf_client()
    # 打印调试信息
    print(f"Using API Key: {os.getenv('SF_API_KEY')[:5]}...")
    print(f"Base URL from client: {client.base_url}")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, world!"}
    ]
    
    response = chat_gpt_plain(
        model="Pro/deepseek-ai/DeepSeek-V3",
        messages=messages,
        client=client,
        temperature=0.7
    )

    rich.print(response)
    return response

def exam_sf_json():
    client = get_sf_client()
    messages = [
        {"role": "system", "content": "You are a helpful assistant that always responds in JSON format."},
        {"role": "user", "content": "Hello, world! return a json object"}
    ]
    
    response = chat_gpt_json(
        model="Pro/deepseek-ai/DeepSeek-V3",
        messages=messages,
        client=client,
        temperature=0.7
    )   

    rich.print(response)
    return response

def exam_sf_raw():
    from openai import OpenAI

    api_key=os.environ.get("SF_API_KEY") 

    client = OpenAI(api_key=api_key, 
                    base_url="https://api.siliconflow.cn/v1")
    response = client.chat.completions.create(
        # model='Pro/deepseek-ai/DeepSeek-R1',
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[
            {'role': 'user', 
            'content': "What New Opportunities Will Inference Models Bring to the Market?"}
        ],
        stream=True
    )

    for chunk in response:
        if not chunk.choices:
            continue
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
        if chunk.choices[0].delta.reasoning_content:
            print(chunk.choices[0].delta.reasoning_content, end="", flush=True)


if __name__ == "__main__":
    #exam_sf_raw()

    exam_sf_plain()
    exam_sf_json()