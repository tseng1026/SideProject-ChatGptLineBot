from .chatgpt import openai


def get_response(messages: str) -> str:
    # 將第六個字元之後的訊息發送給 OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=messages,
        max_tokens=256,
        temperature=0.5,
    )
    # 接收到回覆訊息後，移除換行符號
    return response["choices"][0]["text"].replace("\n", "")
