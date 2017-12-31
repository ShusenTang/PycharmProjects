#encoding=utf-8
# 加上才能中文注释




import requests
#import os
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,'html.parser')

#find_all( name , attrs , recursive , text , **kwargs )
#name 参数可以查找所有名字为 name 的tag
#attrs：对标签属性值的检索字符串，可标注属性检索
#recursive：bool型，是否对子孙全部检索，默认为True
#string :<>...</>中字符串区域的检索字符串


#由于find_all很常用，所以有如下简写形式：
#<tag>(...)等价于<tag>.find_all(...)
#soup(...)等价于soup.find_all(...)

print soup.find_all('a')  #找出所有a标签
print soup.find_all(['a','b'])  #以列表的形式给出a、b标签
print soup.find_all('p','course')#找出带有course属性值的p标签
print soup.find_all(id = 'link1')#id为link1的元素
print soup.find_all(string = "Basic Python")

for tag in soup.find_all(True): #所有标签
    print tag.name

