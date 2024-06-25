from openai import OpenAI

from ai import moonshot_ai_key

client = OpenAI(
    api_key=moonshot_ai_key,
    base_url="https://api.moonshot.cn/v1",
)

history = [
    {"role": "system",
     "content": "你是 Kimi，由 Moonshot AI "
                "提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI "
                "为专有名词，不可翻译成其他语言。"
     }
]


def chat(query, historyText):
    historyText.append([{
        "role": "user",
        "content": query
    }])
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=historyText,
        temperature=0.3,
    )
    result = completion.choices[0].message.content
    historyText.append([{
        "role": "assistant",
        "content": result
    }])
    return result


def singleChat():
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system",
             "content": "你是 Kimi，由 Moonshot AI "
                        "提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI "
                        "为专有名词，不可翻译成其他语言。"
             },
            {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"}
        ],
        temperature=0.3,
    )
    print(completion.choices[0].message.content)


if __name__ == '__main__':
    # text = chat("地球的自转周期是多少？", history)
    # print(text)
    # text2 = chat("月球呢？", history)
    # print(text2)

    singleChat()
