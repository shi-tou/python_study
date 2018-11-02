# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
# -*- coding: UTF-8 -*-
import calendar

cal = calendar.month(2018, 10)
print ("以下输出2018年10月份的日历:\n------------------------")
print (cal)

cal=calendar.calendar(2018,w=2,l=1,c=6,m=4)
print ("以下输出2018年的日历:\n------------------------")
print (cal)

cal=calendar.weekday(2018,10,25)
print(cal)