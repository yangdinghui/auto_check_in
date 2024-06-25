import zhipuai

from ai import zhipuai_ai_key

zhipuai.api_key = zhipuai_ai_key


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


if __name__ == '__main__':
    content = '用python帮忙写个冒泡排序算法的代码，再给一个数组作为例子，写个测试程序'
    # call_model('chatglm_pro', content)
    call_model('glm-4', content)
