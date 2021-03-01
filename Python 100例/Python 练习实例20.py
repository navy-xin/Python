#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/23 18:13
# @Author : navy
# @File : Python 练习实例20.py
# @Software: PyCharm


# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
#
# 程序分析：无
#
# 程序源代码：

tour = []
height = []
hei = 100.0
tim = 10
for i in range(1, tim +1):

    if i == 1:
        tour.append(hei)
    else:
        tour.append(2*hei)
    hei /= 2
    height.append(hei)

print('总调试：tou = {0}'.format(sum(tour)))
print('第10次反弹调试：height = {0}'.format((height[-1])))

