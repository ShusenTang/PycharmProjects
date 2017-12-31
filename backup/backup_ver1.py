# coding=utf-8
# 加上第一行才能中文注释
import os
import time

# 将要被备份的文件列表
source = ['/Users/tang/Downloads/test_backup1.txt', '/Users/tang/Downloads/test_backup2.txt']

# 备份到的文件目录
target_dir = '/Users/tang/Desktop/'

# 以zip压缩文件的形式备份文件，以当前日期与时间命名
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# zip -qr是生成压缩文件，' '.join(source)将source中的各项转换为字符串并用空格连接
zip_command = "zip -qr %s %s" % (target, ' '.join(source))

# os.system()运行shell命令,返回0为正确运行,1为出现异常
if os.system(zip_command) == 0:
    print 'Successful to backup to', target
else:
    print 'Backup FAILED!'
