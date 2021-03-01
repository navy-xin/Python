#-*- codeing = utf-8 -*-
#@Time : 2020/4/27 10:26
#@Author : navy
#@File : testSqlite.py
#@Software: PyCharm

import sqlite3

# 创建数据表
# conn = sqlite3.connect("test2.db")
# print("成功打开数据库")
# c = conn.cursor()
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
#
# c.execute(sql)  # 执行sql语句
# conn.commit()   # 提交数据库操作
# conn.close()    # 关闭数据库

# print("成功建表")

# 插入数据
# conn = sqlite3.connect("test2.db")
# print("成功打开数据库")
#
# c = conn.cursor()
# sql1 = '''
#     insert into company (id,name,age,address,salary)
#     values (1,'张三',32,"成都",8000);
# '''
#
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values (2,'李四',30,"重庆",15000);
# '''
# c.execute(sql1)
# c.execute(sql2)
# conn.commit()
# conn.close()
#
# print("插入数据完毕")


# 查询数据
conn = sqlite3.connect("test2.db")
print("成功打开数据库")

c = conn.cursor()
sql = "select id,name,address,salary from company"

cursor = c.execute(sql)

for row in cursor:
    print("id =", row[0])
    print("name =", row[1])
    print("address =", row[2])
    print("salary =", row[3], "\n")

conn.close()

print("查询完毕")