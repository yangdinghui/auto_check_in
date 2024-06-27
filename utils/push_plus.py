# encoding:utf-8
import requests
import json

try:
    from utils import PUSH_PLUS_TOKEN
except Exception as e:
    print(f'push_plus.py文件,加载PUSH_PLUS_TOKEN异常{e}')


def push_msg(title, content):
    token = PUSH_PLUS_TOKEN
    url = 'https://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": content
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, data=body, headers=headers)
    print(f'PUSH_PLUS推送结果:{res}')
    if res.status_code == 200:
        print(f'PUSH_PLUS推送成功:{res.text}')
    else:
        print(f'PUSH_PLUS推送失败:{res.text}')


if __name__ == '__main__':
    push_msg('标题测试', '内容内容')
