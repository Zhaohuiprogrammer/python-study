#!/usr/bin/env python3
# _*_coding: utf-8_*_
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    if not isinstance(name, str):
        raise TypeError("wrong type")
    if len(name) == 0:
        return None
    return str.upper(name[0]) + str.lower(name[1:])


################################################################


# 编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(n):
    if not isinstance(n, list):
        raise TypeError("wrong type")
    return reduce(lambda a, b: a * b, n)


# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


################################################################


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def char2num(c):
    return DIGITS[c]


def str2float(s):
    if not isinstance(s, str):
        raise TypeError("wrong type")
    l1 = []
    l2 = []
    for i, v in enumerate(s):
        if v == '.':
            l1 = list(map(char2num, s[0:i]))
            l2 = list(map(char2num, s[i + 1:]))
            break
    return reduce(lambda a, b: a * 10 + b, l1) + reduce(lambda c, d: c * 0.1 + d, reversed(l2)) * 0.1


# 测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
