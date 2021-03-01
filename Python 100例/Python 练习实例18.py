#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/23 17:34
# @Author : navy
# @File : Python 练习实例18.py
# @Software: PyCharm

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#
# 程序分析：关键是计算出每一项的值。
#
# 程序源代码：

from functools import  reduce

Tn = 0
Sn = []
S=0
n = int(input('n ='))
a = int(input('a ='))

for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)
    S= S + Tn
#Sn = reduce(lambda  x,y : x + y,Sn)
print("计算和为：",S)
