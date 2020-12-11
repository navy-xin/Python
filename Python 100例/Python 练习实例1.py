#-*- codeing = utf-8 -*-
#@Time : 2020/5/13 14:21
#@Author : navy
#@File : Python 练习实例1.py
#@Software: PyCharm

"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

程序源代码：
"""
s = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)
                s += 1

print('合计%d个不同的组合' %s)