# 系统可以用户输入年龄，用这个年龄做条件判断
"""
1.用户输入
2.保存用户输入的年龄
3.if
***** 注意一个点：input 接收到的数据是str, 不能和18做判断 -- int转换类型
"""



age = int(input('请输入您的年龄:'))

if age >= 18:
    print(f'您输入的年龄是{age},已经成年，可以上网')
else:
    print(f'您输入的年龄是{age},小朋友可以回家写作业去')