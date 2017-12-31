#encoding=utf-8
# 加上才能中文注释


#图片的爬取及存储
#图片网址为https://www.example.com/picture.jpg

import requests
import os

path = '/Users/tang/Desktop/demo3_get_picture.jpg'
url = 'http://edu-image.nosdn.127.net/A51E45E5E97DA5F5BC5B3B06BB48C2F6.png?imageView&thumbnail=520x520&quality=100'
try:
    r = requests.get(url)
    r.raise_for_status() #如果状态不是200引发异常
    r.encoding = r.apparent_encoding #使解码正确
    with open(path,'wb') as f:
        if os.path.exists(path):
            print "文件已存在！！"
        else:
            f.write(r.content)
            f.close()
except:
    print "爬取失败！！！"