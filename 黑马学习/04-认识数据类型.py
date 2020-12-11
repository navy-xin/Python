"""
1.按经验将不同的变量存储不同的类型的数据
2.验证这些数据到底是什么类型--检测数据类型--type(数据）
"""

# int & float
num1 = 1
num2 = 2.222
print(type(num1))
# float型
print(type(num2))

# str 型
a = 'nihaoa'
print(type(a))

# bool
b = False
print(type(b))

# tuple 元组
d = (10,20,30)
print(type(d))

# set 集合
e = {10,20,30}
print(type(e))

# dict 字典
f = {'name':'Tom','age':18}
print(type(f))