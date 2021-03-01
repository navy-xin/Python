#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/21 15:49
# @Author : navy
# @File : 三级caidan.py
# @Software: PyCharm

date = {
    '河南':{
        "郑州":{"金水区","二七区","新郑"},
        "开封":{"龙亭区","金明区","鼓楼区"},
        "洛阳":{"洛龙区","吉利区","孟津县"}
    },
    '安徽':{
            "亳州":{"涡阳县","蒙城县","利辛"},
            "阜阳":{"龙亭区","金明区","鼓楼区"},
            "蚌埠":{"洛龙区","吉利区","孟津县"}
        },
    '山东':{
            "济南":{"市中区","天桥区","历城区"},
            "青岛":{"历下区","金明区","鼓楼区"},
            "泰安":{"槐荫区","吉利区","孟津县"}
        }

}


while True:
    for i in date:
        print(i)

    choice = input("选择进入1》》：")
    if choice in date:
        while True:
            for i2 in date[choice]:
                print("\t",i2)
            choice2 = input("选择进入2>>:")
            if choice2 in date[choice]:
                while True:
                    for i3 in date[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("已经是最底层，按b退出>>:")

                    if choice3 == "b":
                            break
            if choice2 == "b":
                            exit();
