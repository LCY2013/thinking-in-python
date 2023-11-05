# Python code
from datetime import date
import datetime
import math

# swap two variables
var1, var2 = 1, 2
tmp = var1
var1 = var2
var2 = tmp

var1, var2 = var2, var1

# print a string
print('Hello World')

# python 可交互可编译
# python -m py_compile basic.py
# python -i basic.py
# >>> x  = 1
# >>> help(x)
# >>> type(x)
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'x']
# >>> exit()

# 内置数据类型
# 数值、字符串、列表、元组、字典、集合、布尔值、None

# # # 常见数值有 整数、浮点数、复数、布尔值
# 整数 1 2 3 4 5 6 7 8 9 0 整数可以表示为十进制、二进制、八进制、十六进制没有大小限制，受限制于内存
# 浮点数 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0
# 复数 1+2j 2+3j 3+4j 4+5j 5+6j 6+7j 7+8j 8+9j
# 布尔值 True False
# # # 字符串
# 'Hello World'

# # # 列表
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # 元组
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
# # # 字典
# {'name': 'Python', 'age': 30}
# # # 集合
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# # # 布尔值
# True False
# # # None
# None

# 数值支持算数运算 + - * / //整数除法 %求模 **求幂
# 字符串支持 + * in
# 示例 'Hello' + 'World' = 'HelloWorld' 'Hello' * 3 = 'HelloHelloHello' 'H' in 'Hello' = True
# 列表支持 + * in
# 示例 [1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6] [1, 2, 3] * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3] 1 in [1, 2, 3] = True
# 元组支持 + * in
# 示例 (1, 2, 3) + (4, 5, 6) = (1, 2, 3, 4, 5, 6) (1, 2, 3) * 3 = (1, 2, 3, 1, 2, 3, 1, 2, 3) 1 in (1, 2, 3) = True
# 字典支持 in
# 示例 {'name': 'Python', 'age': 30} in {'name': 'Python', 'age': 30} = True
# 集合支持 in
# 示例 {1, 2, 3} in {1, 2, 3} = True
# 布尔值支持 and or not
# 示例 True and False = False True or False = True not True = False

# 支持数学函数
# import math
# abs(x) 返回x的绝对值
# divmod(x, y) 返回''x除以y的商和余数
# pow(x, y) 返回x的y次方
print("pow(2,3) = ", pow(2, 3))
# round(x, n) 返回x的四舍五入值，n是小数点后的位数
# max(x1, x2, x3, ...) 返回最大值
# min(x1, x2, x3, ...) 返回最小值
# sum(iterable) 返回可迭代对象的和
# sum(iterable, start) 返回可迭代对象的和，加上start

# 列表
# list() 创建一个空列表
# list(iterable) 用可迭代对象创建一个列表
# 支持列表本身的方法 append() count() extend() index() insert() pop() remove()
# reverse() sort()
x = list()
x = [1, 'a', 'A', "hello world"]
print(x)
print(x[0])
# 反向访问
print(x[-1])
# print(x[9])
print(len(x))
# print(max(x))
x.reverse()
print(x)

# 元组
# tuple() 创建一个空元组
# tuple(iterable) 用可迭代对象创建一个元组
# 支持元组本身的方法 count() index()
x = tuple()
x = (1, 'a', 'A', "hello world")
print(x)
print(x[0])
# 反向访问
print(x[-1])
# print(x[9])
print(len(x))
# print(max(x))
# x.reverse()
print(x)

# 字典
# dict() 创建一个空字典
# dict(**kwargs) 用关键字参数创建一个字典
# dict(mapping, **kwargs) 用映射创建一个字典
# dict(iterable, **kwargs) 用可迭代对象创建一个字典
# 支持字典本身的方法 clear() copy() fromkeys() get() items() keys() pop() popitem()
# setdefault() update() values()
x = dict()
x = {'name': 'Python', 'age': 30}
print(x)
print(x['name'])
print(x.get('name'))
print(x.get('name1'))
print(x.get('name1', 'default'))
print(x.get('name1', 1))
print(x.get('name1', True))
print(x.get('name1', False))
print(x.get('name1', None))
print(x.get('name1', []))
print(x.get('name1', {}))
print(x.get('name1', ()))
print(x.get('name1', set()))
print(x.get('name1', 0))
print(x.get('name1', 0.0))
print(x.get('name1', 0 + 0j))
print(x.get('name1', ''))
print(x.get('name1', b''))
print(x.get('name1', bytearray()))
print(x.get('name1', range(0)))
print(x.get('name1', tuple()))
print(x.get('name1', dict()))
print(x.get('name1', object()))
print(x.get('name1', type))
print(x.get('name1', print))
print(x.get('name1', Exception))
print(x.get('name1', BaseException))
print(x.get('name1', SystemExit))
print(x.get('name1', KeyboardInterrupt))
print(x.get('name1', GeneratorExit))
print(x.get('name1', StopIteration))
print(x.get('name1', StopAsyncIteration))
print(x.get('name1', ArithmeticError))
print(x.get('name1', FloatingPointError))
print(x.get('name1', OverflowError))

# 集合
# set() 创建一个空集合
# set(iterable) 用可迭代对象创建一个集合
# 支持集合本身的方法 add() clear() copy() difference() difference_update()
# discard() intersection() intersection_update() isdisjoint() issubset()
# issuperset() pop() remove() symmetric_difference()
# symmetric_difference_update() union() update()
x = set()
x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(x)
print(x.pop())
print(len(x))
print(max(x))
# x.reverse()
print(x)

# 布尔值
# bool() 创建一个布尔值
# bool(x) 用x创建一个布尔值
# 支持布尔值本身的方法
x = bool()
x = True
print(x)
print(x.__str__())
print(x.__bool__())
print(x.__repr__())
print(x.__format__(''))
print(x.__sizeof__())
print(x.__class__)
print(x.__class__.__name__)
print(x.__class__.__module__)
print(x.__class__.__bases__)
print(x.__class__.__dict__)
print(x.__dir__())
print(x.__hash__())
print(x.__doc__)
print(x.__getattribute__('__doc__'))
print(x.__getattribute__('__doc__').__class__)
print(x.__getattribute__('__doc__').__class__.__name__)

# None
# None 创建一个None
# 支持None本身的方法
x = None
print(x)

# 变量
# 变量名 = 值
# 变量名1 = 变量名2 = 变量名3 = 值
# 变量名1, 变量名2, 变量名3 = 值1, 值2, 值3
# 变量名1, 变量名2, 变量名3 = 可迭代对象
# 变量名1, *变量名2, 变量名3 = 可迭代对象
# *变量名1, 变量名2, 变量名3 = 可迭代对象
# 变量名1, 变量名2, *变量名3 = 可迭代对象

# if 语句
# if 条件:
#     语句1
#     ...
# else:
#     语句1
#     ...
# if 条件1:
#     语句1
#     ...
# elif 条件2:
#     语句1
#     ...
# elif 条件3:
#     语句1
#     ...
# else:
#     语句1
#     ...
# 示例
x = 1
if x == 1:
    print('x == 1')
elif x == 2:
    print('x == 2')
else:
    print('x != 1')

# while 语句 支持break continue
# while 条件:
#     语句1
#     ...
# else:
#     语句1
#     ...
# 示例
x = 1
while x <= 10:
    print(x)
    x += 1
else:
    print('x > 10')

# for 语句 支持break continue
# for 变量名 in 可迭代对象:
#     语句1
#     ...
# else:
#     语句1
#     ...
# 示例
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in x:
    print(i)
else:
    print('for end')

# 函数
# def 函数名(参数1, 参数2, ...):
#     语句1
#     ...
#     return 返回值
# 示例


def add(x, y):
    return x + y


print(add(1, 2))

# 类
# class 类名(父类1, 父类2, ...):
#     语句1
#     ...
# 示例


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'Hello, {self.name}, {self.age}')


p = Person('Python', 30)
p.say()

# 异常处理
# try:
#     语句1
#     ...
# except 异常类型1 as e:
#     语句1
#     ...
# except 异常类型2 as e:
#     语句1
#     ...
# 示例
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('try end')
finally:
    print('finally end')

# 标准库导入
# import 标准库
# import 标准库 as 别名
# from 标准库 import 模块
# from 标准库 import 模块 as 别名
# from 标准库 import 模块1, 模块2, ...
# from 标准库 import 模块1 as 别名1, 模块2 as 别名2, ...
# from 标准库 import *
# 示例


print(datetime.date.today())


print(date.today())
