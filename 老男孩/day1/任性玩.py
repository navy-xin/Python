#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/17 10:32
# @Author : navy
# @File : 任性玩.py
# @Software: PyCharm


age_of_yeye = 88
count = 0
while count < 3:
    guess_age = int(input("老爷爷多大年纪？请输入："))
    if guess_age == age_of_yeye:
        print("是的，你猜对了，真棒！")
    elif guess_age > age_of_yeye:
        print("猜大了，再往下。。。")
    else:
        print("猜小了，再多点试试...")
    count += 1

    if count == 3:
        countime = input("还要猜么？Y/N")
        if countime != 'n':
            count = 0

