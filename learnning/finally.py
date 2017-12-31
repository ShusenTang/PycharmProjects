# coding=utf-8
# 加上第一行才能中文注释

import time
import os

try:
    f = file('poem.txt')
    while True:
        line = f.readline()  # 一行一行地读
        if len(line) == 0:
            break
        time.sleep(3) # 没读一行暂停3秒，故意将程序拖慢
        print line,  # 加逗号消除换行

    print '\ntest\n'

finally: # 若异常触发，程序也会在退出之前执行finally，将文件关闭
    f.close()
    print 'Cleanning up...closed the file!'