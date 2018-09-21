# requests为第三方库，安装指令：pip install requests
# requests中文文档：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
# -*- coding: utf-8 -*-
import requests
if __name__ == '__main__':
    target = 'https://www.cnblogs.com'
    req = requests.get(target)
    print(req.text)
