#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/23 17:10
# @Author : navy
# @File : Python 练习实例17.py
# @Software: PyCharm


import string
s = input('请输入一个字符串：\n')
letters = 0
space = 0
digit = 0
others = 0
i = 0
while i < len(s):
#    print('长度：%d' %i)
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char = %d, space = %d,digit = %d,others= %d' %(letters,space,digit,others))