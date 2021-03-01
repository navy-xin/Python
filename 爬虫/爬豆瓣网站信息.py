#!/usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2020/12/28 16:07
# @Author : navy
# @File : 爬豆瓣网站信息.py
# @Software: PyCharm

import requests
from lxml import etree

def get_html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}

    try:
        html = requests.get(url,headers = headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取源代码')
            print(html.text)
    except Exception as e :
        print('获取源代码失败：%s' % e)
    return html.text

def parse_html(html):

    html = etree.HTML(html)
    lis = html.xpath("//article[@class='doulist-item']/li")

    for li in lis:
        name = li.xpath("./mod[@class='title']/text()")
    print(len(name))
if __name__ == '__main__':

    url = 'https://www.douban.com/doulist/30299/'
    html = get_html(url)
    movies = parse_html(html)
