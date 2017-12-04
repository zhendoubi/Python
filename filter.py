#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 在一个list中，删除偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 7])))


# 把一个序列中的空字符串删掉，可以这么写
def not_empty(s):
    return s and s.strip()


print(filter(not_empty, ['A', '', 'A', '   ']))
print(list(filter(not_empty, ['A', '', 'A', '   '])))


# 用filter求素数
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n