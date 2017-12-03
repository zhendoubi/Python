#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def ds(x):
    return 2 * x + 1


print(ds(5))


# 匿名函数
fun = lambda x : 2 * x +1
print(fun(5))


def add(x, y):
    return x + y


print(add(3, 4))

fun = lambda x, y: x + y
print(fun(3, 4))


