#!/usr/bin/env python3
# _*_coding: utf-8_*_


# 筛选出列表中的字符串
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ele for ele in L1 if isinstance(ele, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


################################################################


# 去除字符串前后的空格
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


################################################################


# 杨辉三角
def triangles(num):
    s = [1]
    while True:
        yield s
        s = [v + s[i + 1] for i, v in enumerate(s[:len(s) - 1])]
        s.insert(0, 1)
        s.append(1)
        if len(s) == num + 1:
            break


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles(10):
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
