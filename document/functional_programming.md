#### 函数式编程
- 高阶函数
> 在python中函数名是指向函数的变量，当函数的参数也是函数的时候，这种函数我们称之为高阶函数。
```
def add(x, y, f):
    return f(x) + f(y)
add(1, -6, abs)
```
1. map/reduce
> map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
```
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

>>> [1, 4, 9, 16, 25, 36, 49, 64, 81]
```
> reduce把一个函数作用在一个序列\[x1, x2, x3, ...\]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，效果如下:
```
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```
结合map和reduce可以整理出一个str2int的函数:
```
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
```