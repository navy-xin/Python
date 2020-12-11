#-*- codeing = utf-8 -*-
#@Time : 2020/5/13 15:41
#@Author : navy
#@File : Python 练习实例4.py
#@Software: PyCharm

l = []
for i in range(3):
    x = int(input('输入一个整数:\n'))
    l.append(x)
l.sort()
print(l)