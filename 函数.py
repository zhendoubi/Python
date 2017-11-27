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

# 使用函数形参
def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    else:
        print(b, 'is maximum')

printMax(5, 6)

x = 7
y = 9
printMax(x, y)

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


# 使用局部变量
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

x = 5
func(x)
print('x is still', x)


# 使用global语句:用来声明函数中的变量是全局变量
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed local x to', x)

x = 50
func()
print('x is still', x)


# 使用默认参数值:!!!只有在形参表末尾的那些参数可以有默认参数值，即你不能在声明函数形参的时候，
# 先声明有默认值的参数而后声明没有默认值的形参。这是因为赋给形参的值是根据位置而赋值的。
def say(message, times = 1):
    print(message * times)

say('Hello')
say('World\t', 5)


# 关键参数：而你只想指定其中的一部分，那么你可以通过命名来为这些参数赋值——
# 这被称作 关键参数 ——我们使用名字（关键字）而不是位置（我们前面所一直使用的方法）来给函数指定实参。
# 这样做有两个 优势 ——一，由于我们不必担心参数的顺序，使用函数变得更加简单了。
# 二、假设其他参数都有默认值，我们可以只给我们想要的那些参数赋值。
def func(a, b=5, c=10):
    print('a =', a, 'b =', b, 'c =', c)

func(1)

# return语句
def maximun(x, y):
    if x > y:
        return x
    else:
        return y
print(maximun(2, 3))

# 没有返回值的return语句等价于return None
def someFunction():
    pass

print(someFunction())


# Docstring:文档字符串
def printMax(x, y):
    """prints the maximum of two numbers.

    The two values must be integers."""
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

printMax(3, 5)
print(printMax.__doc__)