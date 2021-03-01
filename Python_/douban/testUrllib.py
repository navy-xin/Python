#-*- codeing = utf-8 -*-
#@Time : 2020/4/24 18:16
#@Author : navy
#@File : testUrllib.py
#@Software: PyCharm

import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# import urllib.parse
# date = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data= date)
# print(response.read().decode("utf-8"))

url = "https://movie.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))