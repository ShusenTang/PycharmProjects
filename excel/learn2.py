# -*- coding: utf-8 -*-

import xlwt  # 写


# 创建工作簿
file = xlwt.Workbook(encoding = 'ascii')
# 创建sheet
sheet = file.add_sheet(u"工作表1")

sheet.write(0,0, label= u"第0行第0列的内容")
file.save(u"用xlwt创建的.xls")
