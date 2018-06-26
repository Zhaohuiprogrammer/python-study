
# 错误，调试和测试
> 在程序运行过程中，总会遇到各种各样的错误，Python内置了一套异常处理机制，来帮助我们进行错误处理。

![debug](http://pa8r6emo8.bkt.clouddn.com/blog/5.jpg)

<!--more-->

## 错误处理

> 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数`open()`，成功时返回文件描述符（就是一个整数），出错时返回`-1`。

用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错，所以高级语言通常都内置了一套`try...except...finally...`的错误处理机制，Python也不例外。

### try

```python
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
```

当我们认为某些代码可能会出错时，就可以用`try`来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即`except`语句块，执行完`except`后，如果有`finally`语句块，则执行`finally`语句块，至此，执行完毕。

Python的错误其实也是class，所有的错误类型都继承自`BaseException`，所以在使用`except`时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。

### 调用栈

如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看`err.py`：

```python
# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
```

执行，结果如下：

```python
$ python3 err.py
Traceback (most recent call last):
  File "err.py", line 11, in <module>
    main()
  File "err.py", line 9, in main
    bar('0')
  File "err.py", line 6, in bar
    return foo(s) * 2
  File "err.py", line 3, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
```

我们从上往下可以看到整个错误的调用函数链。

### 记录错误

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

Python内置的`logging`模块可以非常容易地记录错误信息：

```python
# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
```

执行上述模块：

```python
$ python3 err_logging.py
ERROR:root:division by zero
Traceback (most recent call last):
  File "err_logging.py", line 13, in main
    bar('0')
  File "err_logging.py", line 9, in bar
    return foo(s) * 2
  File "err_logging.py", line 6, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END
```

### 抛出错误

因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用`raise`语句抛出一个错误的实例：

```python
# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
```

执行，可以最后跟踪到我们自己定义的错误：

```python
$ python3 err_raise.py
Traceback (most recent call last):
  File "err_throw.py", line 11, in <module>
    foo('0')
  File "err_throw.py", line 8, in foo
    raise FooError('invalid value: %s' % s)
__main__.FooError: invalid value: 0
```

最后，我们来看另一种错误处理的方式：

```python
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
```

在`bar()`函数中，我们明明已经捕获了错误，但是，打印一个`ValueError!`后，又把错误通过`raise`语句抛出去了，这不有病么？

其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

`raise`语句如果不带参数，就会把当前错误原样抛出。此外，在`except`中`raise`一个Error，还可以把一种类型的错误转化成另一种类型：

```python
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
```

## 调试

程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。

### print()

用`print()`把可能有问题的变量打印出来看看。

### 断言

```python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```

`assert`的意思是，表达式`n != 0`应该是`True`，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，`assert`语句本身就会抛出`AssertionError`。

### logging

logging允许你指定记录信息的级别，有`debug`，`info`，`warning`，`error`等几个级别，当我们指定`level=INFO`时，`logging.debug`就不起作用了。同理，指定`level=WARNING`后，`debug`和`info`就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

`logging`的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

```python
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
```

### pdb

Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

```python
# err.py
s = '0'
n = int(s)
print(10 / n)
```

然后启动：

```python
$ python -m pdb err.py
> /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
-> s = '0'
```

以参数`-m pdb`启动后，pdb定位到下一步要执行的代码`-> s = '0'`。输入命令`l`来查看代码：

```python
(Pdb) l
  1     # err.py
  2  -> s = '0'
  3     n = int(s)
  4     print(10 / n)
```

输入命令`n`可以单步执行代码。

### pdb.set_trace()

这个方法也是用pdb，但是不需要单步执行，我们只需要`import pdb`，然后，在可能出错的地方放一个`pdb.set_trace()`，就可以设置一个断点：

```python
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
```

运行代码，程序会自动在`pdb.set_trace()`暂停并进入pdb调试环境，可以用命令`p`查看变量，或者用命令`c`继续运行。

### IDE

目前比较好的Python IDE有：

isual Studio Code：<https://code.visualstudio.com/>，需要安装Python插件。

PyCharm：<http://www.jetbrains.com/pycharm/>

另外，[Eclipse](http://www.eclipse.org/)加上[pydev](http://pydev.org/)插件也可以调试Python程序。

## 单元测试

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

## 文档测试

如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。

可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。

这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。

**[>> 下一篇：IO编程](https://github.com/Zzz468005600/python-study/blob/master/document/io.md)**