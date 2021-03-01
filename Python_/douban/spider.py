#-*- codeing = utf-8 -*-
#@Time : 2020/4/24 16:54
#@Author : navy
#@File : spider.py
#@Software: PyCharm

from bs4 import BeautifulSoup # 网页解析，获取数据
import re # 正则表达式，进行文字匹配
import urllib.request,urllib.error # 制定URL，获取网页数据
import xlwt # 进行SQLite数据操作
import sqlite3 # 进行SQLite数据操作

def main():
    # 1.爬取网页
    baseurl = "https://movie.douban.com/top250?start"
    datalist = getData(baseurl)
    savepath = "豆瓣电影Top250.xls"
    # 3.保存数据
    saveData(datalist, savepath)

# 影片详情连接的规则
findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findIng = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p', re.S)



def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl + str(i*25)
        html = askURL(url)      # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup("html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)
            #影片详情的链接
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findIng, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())

            datalist.append(data)


    return datalist

#得到指定一个URL 的网页内容
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
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

# 保存数据
def saveData(datalist, savepath):
    print("save...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0) # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True) # 创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评分数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i]) # 列名
    for i in range(0, 250):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j]) # 数据

    book.save(savepath)  # 保存

if __name__ == "__main__":
    main()
    print("爬取完毕！")
    # 调用函数
