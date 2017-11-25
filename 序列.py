#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 将一个对象转换成元组
a = 'I love You'
a = list(a)
print(a)

b = (1, 2, 3, 4, 5, 6)
b = list(b)
print(b)

# tuple:将一个可迭代对象转换成元组
b = tuple(b)
print(b)

print(max(1, 5, 2, 4, 9))
print(max(a))

print(sum(b))

print(sorted(a))

numbers = [0, 54, 36, 3, 45, 32, 123, 98]

# reversed : 翻转
print(reversed(numbers))
print(list(reversed(numbers)))

print(enumerate(numbers))

# enumerate
print(list(enumerate(numbers)))

# zip
a = [1, 6, 45, 23, 46, 8, 55]
b = [3, 45, 6, 89, 6]
print(zip(a, b))
print(list(zip(a, b)))