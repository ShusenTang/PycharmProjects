#encoding=utf-8
# 加上才能中文注释

#BeautifulSoup用来对HTML/XML解析，一个BeautifulSoup类对应一个HTML/XML文档的全部内容

"""
BeautifulSoup基本元素：

      Tag	     标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
     Name	     标签的名字，<p>...</p>的名字是’p‘，格式<tag>.name
  Attributes     标签的属性，字典组织形式，格式<tag>.attrs
NavigableString	 标签内非属性字符串，格式<tag>.string
    Comment	     标签内字符串的注释部分，一种特殊的Comment类型
"""

import requests
import os
from bs4 import BeautifulSoup  #从bs4中引入BeautifulSoup类，B和S要大写

url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,'html.parser')#html.parser是解析器
# 另外三种解析器是lxml，xml，htlm5lib，使用这三种解析器需要安装，如：pip install lxml

print soup.title #title即浏览器最上面标签上显示的内容
tag = soup.a  #定义一个标签并用soup中的a标签赋值,若有多个名叫a的标签则只返回第一个

print "标签名:",tag.name,"父标签:",tag.parent.name,"父标签的父标签:",tag.parent.parent.name
print type(tag.attrs) #标签的类型上字典
print tag.attrs,tag.attrs['class'],tag.attrs['href']

print "标签中的字符串信息:",tag.string

print soup.prettify()