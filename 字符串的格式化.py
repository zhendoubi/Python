#!/usr/bin/env python
# _*_ coding:utf-8 _*_

format1 = "{0} love {1} {2}".format('I', 'AHUT', 'CS')
print(format1)

format2 = '{a} love {b} {c}'.format(a='I', b='AHUT', c='CS')
print(format2)

'\t'
print('\ta')
print('\\')


print('{{0}}'.format('不打印'))

# 打印出定点数
print('{0:.1f}{1}'.format(5.56, 'M'))

# %c：格式化字符及其ASCII码
print('%c' % 63)
print('%c %c %c' % (97, 98, 99))

# %s: 格式化字符串
print('%s' % 'I love AHUT')

# %d: 格式化整数
print('%d + %d = %d' % (4, 5, 4+5))
