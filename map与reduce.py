#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from functools import reduce

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4])
print(list(r))

# 将列表[1, 2, 3, 4]中的元素转换为字符串
print(list(map(str, [1, 2, 3, 4])))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4]))


# 将序列[1, 2, 3, 4]变换成整数1234
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 2, 3, 4]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, '17259')))
