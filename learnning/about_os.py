# coding=utf-8
# 加上第一行才能中文注释

import os

print os.name # 输出正在使用的平台，Windows为nt，Linux、unix为posix

print os.getcwd() #得到当前工作目录路径

print os.listdir(os.getcwd()) #返回指定目录下所有的文件和目录名

print os.linesep
