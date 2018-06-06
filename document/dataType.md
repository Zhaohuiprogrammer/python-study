#### **数据类型:**
- **整数**
- **浮点数**
- **字符串**
> 1. 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容。
```
print('''line1
... line2
... line3''')

>>>
line1
line2
line3
```
> 2. Python 3版本中，字符串是以Unicode编码的。
> 3. 源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
- **布尔类型**
> 布尔值可以用and、or和not运算
- **空值**
> 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
- **list**
> list是一种有序的集合，可以随时添加和删除其中的元素。`classmates = ['Michael', 'Bob', 'Tracy']`
- **tuple**
> 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改。`classmates = ('Michael', 'Bob', 'Tracy')`
- **dict**
> dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
```
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

>>>95
```
- **set**
> set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
```
s = set([1, 1, 2, 2, 3, 3])
s

>>>{1, 2, 3}
```