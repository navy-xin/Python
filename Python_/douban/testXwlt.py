#-*- codeing = utf-8 -*-
#@Time : 2020/4/26 14:38
#@Author : navy
#@File : testXwlt.py
#@Software: PyCharm

import xlwt

"""
1、打印一个乘法表达式：x * x = x*X
2、一行打印多个表达式 --
3、打印多行表达式--循环： 一行表达式--换行
"""
workbook = xlwt.Workbook(encoding="utf-8") # 创建workbook对象
worksheet = workbook.add_sheet('99乘法表') # 创建工作表
j = 0
while j < 10:
    i = 0
    while i <= j:
        # print(f'{j} * {i} = {i*j}',end='\t')
        # s = i * j
        worksheet.write(j, i, '%d * %d = %d' %(i+1, j+1, (i+1)*(j+1)))
        i += 1
    # print()
    j +=1


# worksheet.write(0,0,'hello') # 写入数据，第一行参数'行',第二个参数'列'
workbook.save('student.xls') # 保存数据表