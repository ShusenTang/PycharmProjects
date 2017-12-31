#coding=utf-8
# 加上第一行才能中文注释

help(file)
print


poem = 'I love python~' \
       'hjjkkk' \
       'hjjkkk' \
       'dfa' \
       'afaf'

f = file('poem.txt', 'w')
f.write(poem)
f.close()

f = file('poem.txt')
while True:
    line = f.readline() # 一行一行地读
    if len(line) == 0:
        break
    print line, # 加逗号消除换行
f.close()
