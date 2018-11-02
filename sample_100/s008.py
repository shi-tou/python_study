# 输出9*9乘法口诀表。


for i in range(1, 10):
    j = i+1
    s = ""
    for k in range(1, j):
        s += ("" if(s == "") else "  ")+str.format("{0}*{1}={2}", k, i, i*k)
    print(s)
