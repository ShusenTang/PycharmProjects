#encoding=utf-8
# 加上才能中文注释


# 爬取网页的通用代码框架
import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30) #设置30s超时
        r.raise_for_status() #如果状态不是200引发异常
        r.encoding = r.apparent_encoding #使解码正确
        return r.text
    except:
        return "产生异常！！！"

if __name__ == "__main__":
    url = "http://bing.com"
    print (getHTMLText(url))
