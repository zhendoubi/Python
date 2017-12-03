#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 内嵌函数
def fun1():
    print('fun1()正在被调用')
    def fun2():
        print('fun2()正在被调用')
    fun2()


print(fun1())


# 闭包
def FunX(x):
    def FunY(y):
        return x*y
    return FunY


print(FunX(5)(6))

i = FunX(2)
print(i(5))


def Fun1():
    x = [5, 6]
    def Fun2():
        x[0] *= x[1]
        return x[0]
    return Fun2()


print(Fun1())


def Fun1():
    x = 5
    def Fun2():
        nonlocal x  # 将x强制声明为不是一个局部变量
        x *= x
        return x
    return Fun2()


print(Fun1())






