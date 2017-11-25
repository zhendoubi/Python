#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 定义一个函数
def MyFirstFunction():
    print('这是我创建的第一个函数！很不错，继续加油！')

MyFirstFunction()


def MySecondFunction(name):
    print(name + '，我爱你')

MySecondFunction('AHUT')


def add(n1, n2):
    result = n1 + n2
    print(result)

add(1, 2)


def add(n1, n2):
    return n1 + n2

print(add(1, 2))

# 关键字参数
def SaySome(name, words):
    print(name + '->' + words)

SaySome('AHUT', 'CS')
SaySome(words='AHUT', name='CS')


def SaySome(name='AHUT', words='CS'):
    print(name + '->' + words)

SaySome()
SaySome('HeHe')

# 收集(可变)参数
def test(*params):
    print('参数的长度是:', len(params));
    print('第二个参数是:', params[1])

test('AHUT', 'CS')

def hello():
    print('Hello world!')

temp = hello()
print('temp =', temp)

# 函数变量的作用域问题
def discount(price, rate):
    final_price = price * rate
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discount(old_price, rate)
print('打折后的价格：', new_price)

print(r"This is a joke.\n""This is a new joke")