#encoding=utf-8
# 加上才能中文注释


#百度关键词
import requests
keyword = 'python'
try:
    url = "https://www.baidu.com"
    kv = {'wd':keyword}
    r = requests.get(url,timeout = 30,params=kv)
    r.raise_for_status() #如果状态不是200引发异常
    r.encoding = r.apparent_encoding #使解码正确

    print(r.request.url) #此时URL已加上关键字
    print(len(r.text))
except:
    print "爬取失败！！！"