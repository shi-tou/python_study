# 斐波那契数列。
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)


def fn(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fn(n-1)+fn(n-2)


print(str.format("输出第10个斐波那契数列:{0}", fn(10)))
