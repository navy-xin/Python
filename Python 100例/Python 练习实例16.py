#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/23 16:55
# @Author : navy
# @File : Python 练习实例16.py
# @Software: PyCharm

import datetime
if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))
    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)

    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
    # 日期算术运算
    miyazakiBirthDate =miyazakiBirthDate + datetime.timedelta(days=10)

    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
    # 日期替换
    miyazakiBirthDate = miyazakiBirthDate.replace(month=miyazakiBirthDate.month + 1)
    miyazakiBirthDate = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
