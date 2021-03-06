# Beautiful Soup是一个强大的用于解析HTML第三方库，安装指令：pip install beautifulsoup4
# Beautiful Soup也是有中文的官方文档：http://beautifulsoup.readthedocs.io/zh_CN/latest/
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://www.cnblogs.com'  # 博客园首页
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html)
    aList = bf.find_all('a', class_='titlelnk')  # 抓取文章标题
    with open('F:/test.txt', 'a', encoding='utf-8') as f:
        for a in aList:
            print(a.text+'\n'+ a.get('href')+'\n')
            f.writelines(a.text)
            f.write('\n')
            f.writelines(a.get('href'))
            f.write('\n\n')
