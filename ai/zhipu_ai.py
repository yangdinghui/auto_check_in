import zhipuai
from openai import OpenAI

from ai import zhipuai_ai_key

zhipuai.api_key = zhipuai_ai_key

client = OpenAI(
    api_key=zhipuai_ai_key,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)


def call_model(model_name, cont):
    response = zhipuai.model_api.sse_invoke(
        model=model_name,
        prompt=[{"role": "user", "content": cont}],
        temperature=0.9,
        top_p=0.7,
        incremental=True
    )

    for event in response.events():
        if event.event == "add":
            print(event.data, end="")
        elif event.event == "error" or event.event == "interrupted":
            print(event.data, end="")
        elif event.event == "finish":
            print(event.data)
            print(event.meta, end="")
        else:
            print(event.data, end="")


def zhipu_use_openai_sdk(model_name):
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "你是一个聪明且富有创造力的小说作家"},
            {"role": "user",
             "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"}
        ],
        top_p=0.7,
        temperature=0.9
    )
    print(completion.choices[0].message)


if __name__ == '__main__':
    content = '用python帮忙写个冒泡排序算法的代码，再给一个数组作为例子，写个测试程序'
    # call_model('chatglm_pro', content)
    # call_model('glm-4', content)
    zhipu_use_openai_sdk('glm-4')

