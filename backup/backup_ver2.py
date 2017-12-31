# coding=utf-8
# 加上第一行才能中文注释

# ver_2相比于ver_1的优化：使用时间作为文件名，而当前日期作为目录名，存放在主备份目录中。

import os
import time

# 将要被备份的文件列表
source = ['/Users/tang/Downloads/test_backup1.txt', '/Users/tang/Downloads/test_backup2.txt']

# 备份到的文件目录
target_dir = '/Users/tang/Desktop/'


# 以日期作为子目录名
today = target_dir + time.strftime('%Y%m%d')

# 以时间作为文件名
now = time.strftime('%H%M%S')

# 如果子目录（日期）不存在，则创建
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successful created directory', today

# 备份文件目标
target = today + os.sep + now + '.zip'  # os.sep会根据操作系统给出目录分隔符，Linux&Unix就是'/',win就是'\\'

# zip -qr是生成压缩文件，' '.join(source)将source中的各项转换为字符串并用空格连接
zip_command = "zip -qr %s %s" % (target, ' '.join(source))

# os.system()运行shell命令,返回0为正确运行,1为出现异常
if os.system(zip_command) == 0:
    print 'Successful to backup to', target
else:
    print 'Backup FAILED!'
