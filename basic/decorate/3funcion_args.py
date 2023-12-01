# 被修饰函数带参数
def outer(func):
    def inner(a, b):
        print(f'inner {func.__name__}')
        print(a, b)
        func(a, b)

    return inner


@outer
def foo(a, b):
    print(a + b)
    print(f'foo: {foo.__name__}')


foo(1, 2)
print(foo.__name__)


############################################

# 被修饰函数带不定长参数
def outer(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)

    return inner


@outer
def foo(a, b, c):
    print(a + b + c)


foo(1, 2, 3)


############################################

# 被修饰函数带返回值
def outer(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret

    return inner


@outer
def foo(x, y, z):
    return x ** 2 + y ** 2 + z ** 2


print(foo(1, 2, 3))
