#-*- codeing = utf-8 -*-
#@Time : 2020/4/26 18:56
#@Author : navy
#@File : TEST.py
#@Software: PyCharm
url = "https://movie.douban.com/top250?start"
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    # except urllib.error.URLError as e:
    #     if hasattr(e, "code"):
    #         print(e.code)
    #     if hasattr(e, "reason"):
    #         print(e.reason)
    # return html


askURL(url)