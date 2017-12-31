# coding=utf-8
# 加上第一行才能中文注释

# 用try...except模块来处理异常

import sys

# 把所有可能引发错误的部分放在try块中：
try:
    s = input('Enter something:') # 输入integer才是合法的


# 如果异常由EOF引起（即输入了command+D）
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit() # 退出

except:
    print '\nSome error exception occurred!'
    sys.exit()

print 'Done!'