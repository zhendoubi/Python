#!/usr/bin/env python
# _*_ coding:utf-8 _*_

str1 = 'I love my parents'
print(str1)
str1 = str1[:6] + ' 插入的汉字' + str1[6:]
print(str1)

# 字符串第一个字符改为大写
str2 = 'zhangzhen'
print(str2.capitalize())

# 将整个字符串的所有字符改为小写
str3 = 'ZHANGZHEN'
print(str3.casefold())
print(str3)

# center(width):将字符串居中，并使用空格填充至长度width的新字符串
print(str2.center(10))

# count(sub[,start[,end]]):返回sub在字符串里边出现的次数，start和end参数表示范围,可选
print(str3.count('A'))

