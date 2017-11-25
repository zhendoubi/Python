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

# %o: 格式化无符号八进制数
print('%o' % 10)

# %x: 格式化无符号十六进制数
print('%x' % 10)

# %X: 格式化无符号十六进制数(大写)
print('%X' % 10)

# %f: 格式化定点数，可指定小数点后的精度(默认为6位)
print('%f' % 10.658)

# %e/%E: 用科学计数法格式化定点数
print('%e' % 10.658)
print('%E' % 10.658)

# %g: 根据值的大小决定使用%f或%e
print('%g' % 10.658)
print('%g' % 10.658794)


#  格式化操作符辅助指令
#  m.n: m是显示的最小宽度(字符串总长度为m)，n是小数点后的位数
print('%5.2f' % 10.659)

# -: 用于左对齐
print('%10d' % 5)
print('%010d' % 5)
print('%-10d' % 5)

# +: 在正数前面显示加号(+)
print('%+d' % 10)

# #: 在八进制前面显示零('0'),在十六进制前面显示'0x'或'0X'
print('%#o' % 10)
print('%#x' % 10)
print('%#X' % 10)

# 0: 显示的数字前面填充'0'取代空格

