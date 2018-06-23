#!/usr/bin/env python3
# _*_coding: utf-8_*_


# 寻找最大和最小的数字
def find_min_and_max(l):
    if not isinstance(l, (list, tuple)):
        raise TypeError("wrong type")
    if len(l) == 0:
        return None, None
    if len(l) == 1:
        return l[0], l[0]
    min_num = l[0]
    max_num = l[0]
    for n in l:
        if n < min_num:
            min_num = n
        if n > max_num:
            max_num = n
    return min_num, max_num


# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
