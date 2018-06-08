#!/usr/bin/env python3
# _*_coding: utf-8_*_


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ele for ele in L1 if isinstance(ele, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
