# Beautiful Soup是一个强大的用于解析HTML第三方库，安装指令：pip install beautifulsoup4
# Beautiful Soup也是有中文的官方文档：http://beautifulsoup.readthedocs.io/zh_CN/latest/
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://www.cnblogs.com' #博客园首页
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html)
    aList = bf.find_all('a', class_='titlelnk') #抓取文章标题
    index = 0
    for a in aList:
        print( str(index)+'-' +a.text)
        index += 1
