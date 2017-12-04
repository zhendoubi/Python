#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 非递归求阶乘
def d(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print(d(5))


# 递归求阶乘
def d_2(n):
    if n == 1:
        return 1
    else:
        return n * d_2(n-1)


print(d_2(10))


# 非递归的斐波那契数列
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print('输入有误！')
        return -1
    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3


print(fab(3))


# 递归的斐波那契数列
def fab(n):
    if n < 1:
        print('输入有误！')
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-2) + fab(n-1)


print(fab(40))


# 汉诺塔
