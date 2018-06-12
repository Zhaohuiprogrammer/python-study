#### 函数
> [练习代码](https://github.com/Zzz468005600/python-study/blob/master/code/test_function.py)

**1. 定义函数**
- 使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
```
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```
- 可返回多个值（返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple）。
```
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
```
**2. 函数的参数**
- 位置参数
- 默认参数
```
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
```
> 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错；二是当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。三是默认参数必须指向不变对象（str、None等）！
- 可变参数
```
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2)
nums = [1, 2, 3]
calc(*nums)
```
- 关键字参数
> 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
```
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

>>> name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```
- 命名关键字参数
```
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

>>> Jack 24 Beijing Engineer

def person(name, age, *args, city='Beijing', job):
    print(name, age, args, city, job)
person('Jack', 24, job='Engineer')

>>> Jack 24 Beijing Engineer
```
> 和关键字参数\*\*kw不同，命名关键字参数需要一个特殊分隔符\*，\*后面的参数被视为命名关键字参数。如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符\*了






