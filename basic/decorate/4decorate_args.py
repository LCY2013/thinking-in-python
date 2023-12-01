# 装饰器带参数
from multiprocessing.sharedctypes import synchronized


def outer_args(bar):
    def outer(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            print(bar)
            return ret

        return inner

    return outer


# 相当于outer_arg('foo_arg')(foo)()
@outer_args('foo_arg')
def foo_arg(x, y, z):
    return x ** 3 + y ** 3 + z ** 3


print(foo_arg(1, 2, 3))


############################################

# 装饰器堆叠
@classmethod
@synchronized(lock)
def foo(cls):
    pass


def foo(cls):
    pass


foo2 = synchronized(lock)(foo)
foo3 = classmethod(foo2)
foo = foo3
