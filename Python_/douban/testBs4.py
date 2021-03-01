#-*- codeing = utf-8 -*-
#@Time : 2020/4/26 17:30
#@Author : navy
#@File : testBs4.py
#@Software: PyCharm

from bs4 import BeautifulSoup
import re
file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(bs.title)
# print(bs.title.string)
# print(type(bs.title.string))
# t_list = bs.find_all(re.compile("a"))

# print((t_list))

pat = re.compile("AA")
M = pat.search("CBAADFA")
print(M)