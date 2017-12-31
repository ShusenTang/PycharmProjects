#encoding=utf-8
# 加上才能中文注释



#定向爬取最好大学网上的大学排名并屏幕输出
#步骤一：获取网页内容:getHTMLtext()
#步骤二：提取网页信息并存放至合适的数据结构(如列表list)中:fillUnivList()
#步骤三：利用数据结构展示并输出:printUnivList()


import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
from bs4 import BeautifulSoup
import bs4  #由于要使用bs4中的类

def getHTMLtext(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist,html): #
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:  #所有大学信息包含在tbody标签中
        if isinstance(tr,bs4.element.Tag):  #如果是bs4中的Tag型
            tds = tr("td")#<tag>(...)等价于<tag>.find_all(...)，返回列表型
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num): #num为打印数目
    for i in range(num):
        u = ulist[i]
        print u[0].center(20),u[1].center(20),u[2].center(20) #输出居中

if __name__ == '__main__':
    uinfolist = []  #大学排名信息存放在列表中
    url = 'http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2017.html'
    html = getHTMLtext(url)
    fillUnivList(uinfolist,html)
    num = input("请输入你所查询的学校数:\n")
    printUnivList(uinfolist,num)  #列出num所学校






