#### 高级特性
- 切片(Slice)
```
L = list(range(100))
L[:10]

>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

(0, 1, 2, 3, 4, 5)[:3]

>>> (0, 1, 2)

'ABCDEFG'[:3]

>>> 'ABC'
```
> 在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。

- 迭代
1. 通过collections模块的Iterable类型判断对象是否为可迭代对象
```
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代

>>> True
```
2. Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
```
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

>>>
    0 A
    1 B
    2 C
```
- 列表生成
1. `list(range(1, 11))`
2. 生成\[1x1, 2x2, 3x3, ..., 10x10]
```
L = []
for x in range(1, 11):
    L.append(x * x)
```
3. 列表生成式（list comprehensions）可以用一行语句代替循环生成上面的list
```
[x * x for x in range(1, 11)]
```
- 生成器（generator）
> generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误;
> 同样也可以使用for循环遍历
1. 把一个列表生成式的\[\]改成()
```
g = (x * x for x in range(10))
for n in g:
   print(n)

>>>
    0
    1
    4
    9
    16
    25
    36
    49
    64
    81
```
2. 函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
> generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
> 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
```
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
```
- 迭代器
1. 可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function
> 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。可以使用isinstance()判断一个对象是否是Iterable对象。
> 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。可以使用isinstance()判断一个对象是否是Iterator对象。
2. 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
3. Python的for循环本质上就是通过不断调用next()函数实现的。
```
for x in [1, 2, 3, 4, 5]:
    pass
```
完全等同于:
```
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```
小结:Python的Iterator对象表示的是一个数据流，这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。