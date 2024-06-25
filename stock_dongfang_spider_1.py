from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作


def main():
    baseurl = "http://data.eastmoney.com/zjlx/000001.html"
    # 1.爬取网页
    datalist = getDate(baseurl)

    # 2.逐一解析数据

    # 3.打印数据或保存到当前代码文件夹下    
    savepath = "东方财富名称.xlsx"
    saveData(datalist, savepath)


# 创建正则表达式的对象
findTitle = re.compile(r'<a href="(.*?)">(.*?)</a>')


# 爬取网页
def getDate(baseurl):
    datalist = []
    html = askURL(baseurl)  # 保存获取到的网页源码
    # 2.逐一解析数据       在网页的解析中，寻找到需要的信息代码块
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('tr'):
        for it in item.find_all('td'):
            it = str(it)
            tirle = re.findall(findTitle, it)
            if len(tirle) != 0:
                datalist.append(tirle[0][1])
    # print(datalist)
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    # 用户代理，表示告诉网页服务器，是何种类型的机器、浏览器
    # 模拟浏览器头部信息，向网页服务器发送信息
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 94.0.4606.61Safari / 537.36Edg / 94.0.992.31"
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(datalist, savepath):
    print('Title：\n', datalist)
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    # cell_overwrite_ok=True每一个单元往里面输入的时候直接覆盖掉里面的内容
    sheet = book.add_sheet('东方财富名称', cell_overwrite_ok=True)

    # 向xlsx表中横向添加标题
    for i in range(0, 20):
        print("执行完第%d条" % (i + 1))
        data = datalist[i]
        # print(data)
        sheet.write(0, i, data)
    book.save(savepath)  # 保存
    print('Title：\n', datalist)


if __name__ == "__main__":
    # 调用函数
    main()
    print("爬取完毕！")