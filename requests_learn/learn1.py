#encoding=utf-8
# 加上第一行才能中文注释

import requests
r = requests.get("http://www.baidu.com")
print "http请求的返回状态:",(r.status_code) #200表示访问成功
print  type(r)
print "头部为",r.headers
print "内容(字符串形式)为：",r.text  #其中中文是乱码
print "从header中猜测响应编码方式为：",r.encoding
print "从内容中分析出响应内容编码方式:",r.apparent_encoding  #解析出来的编码方式更准确
print  "内容的二进制形式为：",r.content


r.encoding = r.apparent_encoding; #解决中文乱码的问题(中文是utf-8)
print r.text