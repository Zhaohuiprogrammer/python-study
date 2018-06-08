#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def trim(s):
    if not isinstance(s, str):
        raise TypeError("wrong type")
    if len(s) == 0:
        return s
    start = 0
    end = len(s) - 1
    while True:
        is_start_find = True
        is_end_find = True
        if s[start:start + 1] == " ":
            start = start + 1
            is_start_find = False
        if s[end:end + 1] == " ":
            end = end - 1
            is_end_find = False
        if (is_start_find and is_end_find) or start == end:
            break
    return s[start: end + 1]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
