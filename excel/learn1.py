# -*- coding: utf-8 -*-


#对excel文档操作要安装两个库：pip install Xlwt和pip install Xlrd

import xlrd  # 读

wordbook = xlrd.open_workbook('test.xls') #打开文档

sheet_name = wordbook.sheet_names() #获取所有sheet，返回列表型

sheet1 = wordbook.sheet_by_index(0)         # 按索引取得sheet
sheet2 = wordbook.sheet_by_name(u"工作表1")  # 按名字取得sheet

#   sheet可以看作一个二维数组
print sheet1.row(0)[1].value  #第0行第1列
print sheet2.col(0)[1].value  #第0列第1行
print sheet1.cell(0,1).value  #第0行第1列

for row in range(sheet1.nrows):
    for col in range(sheet1.ncols):
        print sheet1.cell(row,col).value,"              ",
    print '\n'