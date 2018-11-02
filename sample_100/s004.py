# 输入某年某月某日，判断这一天是这一年的第几天？
# -*- coding: UTF-8 -*-

import time
import datetime
import calendar

nowTime = datetime.datetime.now()
print("当前时间:", nowTime.strftime("%Y-%m-%d %H:%M:%S"))
year = nowTime.year
month = nowTime.month
day = nowTime.day
print(str.format("年：{0}，月：{1}，日：{2}", str(year), str(month), str(day)))

startTime = datetime.datetime(year, 1, 1)
timeSpan = nowTime-startTime
print(str.format("这一天是这一年的第{0}天",timeSpan.days))

print(str.format("今年是{0}年","闰" if(calendar.isleap(year)) else "平"))
