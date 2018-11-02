# 输入三个整数x,y,z，请把这三个数由小到大输出。
# -*- coding: UTF-8 -*-

#arr=[3,9,6]
#arr.sort()
#print(arr)

l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print (l)