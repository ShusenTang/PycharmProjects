# coding=utf-8
# 加上第一行才能中文注释

# ver_3相比于ver_2的优化：zip归档名上可以附带一个用户提供的注释以便清楚地区分每个备份

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

# zip归档名上附带一个用户提供的注释
comment = raw_input('Enter a comment:')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'  # os.sep会根据操作系统给出目录分隔符，Linux&Unix就是'/',win就是'\\'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'  # 把注释中的空格替换成下划线

# 如果子目录（日期）不存在，则创建
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successful created directory', today

# zip -qr是生成压缩文件，' '.join(source)将source中的各项转换为字符串并用空格连接
zip_command = "zip -qr %s %s" % (target, ' '.join(source))

# os.system()运行shell命令,返回0为正确运行,1为出现异常
if os.system(zip_command) == 0:
    print 'Successful to backup to', target
else:
    print 'Backup FAILED!'
