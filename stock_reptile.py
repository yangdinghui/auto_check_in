import re
import time
import random
import requests
import pandas

# 请求头信息
headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
           'Connection': 'keep-alive',
           'Cookie': 'qgqp_b_id=19f66ef1368d6e2506b33a57d7d42102; websitepoptg_api_time=1693827592377; '
                     'st_si=15311446147433; websitepoptg_show_time=1693827592660; st_asi=delete; '
                     'st_pvi=64611557087756; st_sp=2023-09-04%2019%3A39%3A52; '
                     'st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=3; '
                     'st_psi=20230904194014849-113200301321-2315029714',
           'Host': '48.push2.eastmoney.com', 'Referer': 'https://quote.eastmoney.com/center/gridlist.html',
           'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'Sec-Ch-Ua-Mobile': '?0',
           'Sec-Ch-Ua-Platform': '"Windows"', 'Sec-Fetch-Dest': 'script', 'Sec-Fetch-Mode': 'no-cors',
           'Sec-Fetch-Site': 'same-site',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/116.0.0.0 Safari/537.36'}


# 定义一个函数，用来获取股票数据
def get_stock_data(_url):
    # 发送GET请求获取网页内容
    res = requests.get(_url, headers=headers)
    # 返回网页内容
    return res.text


# 定义一个函数，用来解析股票数据
def parse_stock_data(data):
    # 使用正则表达式提取股票数据
    stock_code = re.findall('"f12":"(.*?)","f13"', data)
    company_name = re.findall('"f14":"(.*?)","f15"', data)
    latest_price = re.findall('f2":(.*?),"f3', data)
    change_percent = re.findall('f3":(.*?),"f4', data)
    change_amount = re.findall('"f4":(.*?),"f5"', data)
    volume = re.findall('f5":(.*?),"f6', data)
    turnover = re.findall('f6":(.*?),"f7', data)
    amplitude = re.findall('f7":(.*?),"f8', data)
    highest = re.findall('f15":(.*?),"f16', data)
    lowest = re.findall('f16":(.*?),"f17', data)
    open_price = re.findall('f17":(.*?),"f18', data)
    previous_close = re.findall('f18":(.*?),"f20', data)
    volume_ratio = re.findall('f10":(.*?),"f11', data)
    turnover_rate = re.findall('f8":(.*?),"f9', data)
    pe_ratio = re.findall('f9":(.*?),"f10', data)
    pb_ratio = re.findall('f23":(.*?),"f24', data)
    return stock_code, company_name, latest_price, change_percent, change_amount, volume, turnover, amplitude, \
           highest, lowest, open_price, previous_close, volume_ratio, turnover_rate, pe_ratio, pb_ratio


# 定义一个函数，用来获取股票数据
def scrape_stock_info():
    # 定义一个列表，用来存放所有股票数据
    _all_list = []
    # 定义一个初始化页码的变量
    page = 1
    # 定义一个循环，用来爬取所有股票数据
    while page <= 2:
        url = f'https://48.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112408633284394296752_1693827639686&pn={page}&pz' \
              f'=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,' \
              f'm:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,' \
              f'f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1693827639687 '
        # 调用函数获取股票数据
        data = get_stock_data(url)
        # 调用函数解析股票数据
        stock_code, company_name, latest_price, change_percent, change_amount, volume, turnover, amplitude, \
        highest, lowest, open_price, previous_close, volume_ratio, turnover_rate, pe_ratio, pb_ratio = parse_stock_data(
            data)
        # 将股票数据添加到列表中
        for i in range(len(stock_code)):
            # 定义一个列表，用来存放每一条股票数据
            mylist = [stock_code[i], company_name[i], latest_price[i], change_percent[i], change_amount[i], volume[i],
                      turnover[i], amplitude[i], highest[i], lowest[i], open_price[i], previous_close[i],
                      volume_ratio[i],
                      turnover_rate[i], pe_ratio[i], pb_ratio[i]]
            # 将每一条股票数据添加到列表中
            _all_list.append(mylist)
            print('正在获取数据。。。')
        page += 1
        # 设置一个随机的休眠时间，防止被服务器拒绝访问
        time.sleep(random.randint(1, 5))

    # 返回所有股票数据
    return _all_list


# 定义一个函数，用来将数据保存到excel表格中
def excel_data(_all_list):
    # 创建一个表格对象
    table_data = pandas.DataFrame(_all_list)
    # 将表格数据保存到excel表格中
    table_data.to_excel('股票信息.xlsx',
                        header=['股票代码', '企业名称', '最新价', '涨跌幅', '涨跌额', '成交量', '成交额', '振幅',
                                '最高',
                                '最低', '今开', '昨收', '量比', '换手率', '市盈率', '市净率'])


# 定义一个主函数
if __name__ == '__main__':
    # 调用函数获取股票数据
    all_list = scrape_stock_info()
    # 调用函数将数据保存到excel表格中
    excel_data(all_list)
    print('数据获取完成！')
