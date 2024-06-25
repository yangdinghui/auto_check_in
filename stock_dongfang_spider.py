import requests
from bs4 import BeautifulSoup



def start():
    url = 'http://data.eastmoney.com/zlsj/stocklist.html'
    baseurl = "http://data.eastmoney.com/zjlx/000001.html"
    headers = {'Content-Type': 'text/html; charset=utf-8'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tab1'})
    if table is not None:
        res = table.tbody.find_all('tr')
        for tr in res:
            tds = tr.find_all('td')
            if len(tds) > 1:
                stock_code = tds[1].text.strip()
                stock_name = tds[2].text.strip()
                stock_url = 'http://quote.eastmoney.com/' + stock_code + '.html'
                stock_response = requests.get(stock_url)
                stock_soup = BeautifulSoup(stock_response.text, 'html.parser')
                price = stock_soup.find('span', {'class': 'last'}).text.strip()
                print(stock_code, stock_name, price)
    else:
        print('无法找到指定的表格元素')


if __name__ == '__main__':
    start()
