#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/18 18:11
# @Author : navy
# @File : 买东西.py
# @Software: PyCharm


product_list = [
    ('Iphone',7800),
    ('Mac pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('movie',30),

]

shopping_list = []
salary = input("请输入您的工资：")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("你要买什么？（退出q)购买请输入上面的商品序号：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and  user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("添加 %s 到购物车，你的余额是： %s" %(p_item,salary))
                else:
                    print("商品序号 [%s] 不能购买" % user_choice)
        elif user_choice == 'q':
                print("-------------------购物车列表--------------------")
                for p in shopping_list:
                    print(p)
                print("你的余额:",salary)
                exit()
        else:
                print("invalid option")
