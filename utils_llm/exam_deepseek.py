from dotenv import load_dotenv
import rich 

load_dotenv()


from utils_llm.llm_base import get_deepseek_client, chat_gpt_plain, chat_gpt_json 


def exam_deepseek_plain():
    client = get_deepseek_client()
    response = chat_gpt_plain(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "Hello, world!"}],
        client=client
    )

    rich.print(response)
    return response

def exam_deepseek_json():
    client = get_deepseek_client()
    response = chat_gpt_json(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "Hello, world! return a json object"}],
        client=client
    )   

    rich.print(response)
    return response


def exam_deepseek_reasoner_plain():
    client = get_deepseek_client()
    response = chat_gpt_plain(
        model="deepseek-reasoner",
        messages=[{"role": "user", "content": "Hello, world!"}],
        client=client
    )

    rich.print(response)
    return response

if __name__ == "__main__":
    exam_deepseek_plain()
    exam_deepseek_json()

    exam_deepseek_reasoner_plain()
