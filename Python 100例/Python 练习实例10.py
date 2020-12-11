#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/11 16:52
# @Author : navy
# @File : Python 练习实例10.py
# @Software: PyCharm

print('题目：暂停一秒输出，并格式化当前时间')

import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# 暂停一秒

time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))