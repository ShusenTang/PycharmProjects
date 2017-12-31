# coding=utf-8
# 加上第一行才能中文注释

#pickle和cPickle（C语言编写，更快）可以使你在文件中存储任何Python对象

import cPickle
#imort pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'peach', 'banana']

f = file(shoplistfile,'w')

cPickle.dump(shoplist,f) # 存储

f.close()

del shoplist

f = file(shoplistfile) # 默认为'r'，即读文件

storedlist = cPickle.load(f) # 取存储

print storedlist

