#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# from ... import 语句
# from sys import *
# from ... import **


# 模块的__name__
# 使用模块的__name__
if __name__ == '__main__':
    print('AHUT')
else:
    print('CS')

# 这个模块应该被放置在我们输入它的程序的同一个目录中
import mymodule

mymodule.sayhi()
print('Version',mymodule.version)

# 使用from...import
from mymodule import sayhi,version

sayhi()
print('Version', version)