#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/11 17:36
# @Author : navy
# @File : Python 练习实例13.py
# @Software: PyCharm

print('题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。')

for n in range(100,1000):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    if n == i*i*i + j*j*j + k*k*k:
        print(i,j,k)
        print(n)