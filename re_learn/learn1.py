#encoding=utf-8
# 加上才能中文注释

#正则表达式https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

import re
match = re.search(r'[1-9]\d{5}','bit100081')
# r'string'表示这个string是raw string，即其中的\不是转义字符
#[1-9]\d{5}为邮编的正则表达式
if match:
    print match.group(0)  #match为match型对象
    print type(match),match.string,match.re,match.start(),match.end(),match.span()

print '-----------分割线----------'

match = re.match(r'[1-9]\d{5}','bit100081')
if match:
    print match.group(0)  #未匹配，返回的同样是为match型对象

print '-----------分割线----------'


ls = re.findall(r'[1-9]\d{5}','bit100081 tsu100084')
if ls:
    print ls  #ls为列表型

print '-----------分割线----------'

ls = re.split(r'[1-9]\d{5}','bit 100081 tsu100084')#split将匹配的去掉并以此为界分割
if ls:
    print ls

print '-----------分割线----------'

ls = re.split(r'[1-9]\d{5}','bit100081 tsu100084',maxsplit = 1)#最多匹配一次
if ls:
    print ls

print '-----------分割线----------'

for m in re.finditer(r'[1-9]\d{5}','bit100081 tsu100084'):#对每次的匹配结果单独处理
    if m:
        print (m.group(0))  #返回为match型对象

print '-----------分割线----------'

str = re.sub(r'[1-9]\d{5}','123456','bit100081 tsu100084')#用123456替换匹配的字符串
print  str

