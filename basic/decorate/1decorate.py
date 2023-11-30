# PEP 318 装饰器  PEP-3129 类装饰器
# https://peps.python.org/pep-0318/
# https://peps.python.org/pep-3129/

# 前置问题
def fun():
    pass


a = fun
b = fun()


# a表示函数
# b表示执行函数

# 装饰器在模块导入的时候自动运行
# module.py

def decorate(func):
    print('running in module.')

    def inner():
        return func()

    return inner


############################
# 装饰器, @ 语法糖
@decorate
def fun():
    print('do sth')


# 等价于下面内容
def func():
    print('do sth')


func = decorate(func)


############################


# 装饰器在模块导入的时候自动运行
# testmodule.py
def decorate(func):
    print('running in modlue')

    def inner():
        return func()

    return inner


@decorate
def func2():
    pass


# test.py
import testmodule
# from testmodule import func2
