# pip install zhipuai 请先在终端进行安装

import zhipuai

zhipuai.api_key = "6971a4f263b0cb9cf7de4388912b3683.hJaHZRg2nrMx10ax"


def call():
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_pro",
        prompt=[{"role": "user", "content": "用python帮忙写个冒泡排序算法的代码，再给一个数组作为例子，写个测试程序"}],
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
    call()
