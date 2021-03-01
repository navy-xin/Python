#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/11 18:05
# @Author : navy
# @File : Python 练习实例15.py
# @Software: PyCharm



print('题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。')


score = int(input('输入分数：\n'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'D'
print('%d 属于 %s' %(score,grade))