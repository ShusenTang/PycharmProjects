#encoding=utf-8
# 加上才能中文注释

import requests
try:
    url = "https://miaosha.jd.com/#1179011"
    r = requests.get(url,timeout = 30)
    r.raise_for_status() #如果状态不是200引发异常
    r.encoding = r.apparent_encoding #使解码正确
    print r.text[:1000]
except:
    print "爬取失败！！！"
