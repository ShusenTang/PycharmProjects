# encoding=utf-8
# 加上才能中文注释

# 淘宝搜索商品并比价
# 步骤一：提交商品搜索请求，循环获取下一页
# 步骤二：对每个页面提取商品名称和价格
# 步骤三：输出

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parsePage(ilt, html):
    try:
        price_lt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        name_lt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(price_lt)):
            price = eval(price_lt[i].split(':')[1])  # eval可将string最外层引号去掉
            name = eval(name_lt[i].split(':')[1])
            ilt.append([price, name])

    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format(" 序号 ", " 价格 ", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print (tplt.format(count, g[0], g[1]))


if __name__ == '__main__':
    goods = '书包'
    depth = 1  # 爬取的页面数
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)  # 观察知淘宝一页显示43个商品
            html = getHTMLText(url)
            parsePage(infolist, html)
        except:
            continue  # 一页解析失败不会影响下一页

    printGoodsList(infolist)
