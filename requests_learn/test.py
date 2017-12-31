#encoding=utf-8
# 加上才能中文注释


# 爬取网页的通用代码框架
import requests

kv = {'key1':'value1','key2':'value2'}
r = requests.request('GET','http://python123.io/ws',params=kv)
print r.url