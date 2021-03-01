#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2021/1/7 16:33
# @Author : navy
# @File : Python 练习实例23.py
# @Software: PyCharm

# 题目：打印出如下图案（菱形）:

from sys import stdout
for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print(' ')
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print(' ')