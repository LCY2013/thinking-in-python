########################
# 内置的装饰方法函数

# functools.wraps
# @wraps接受一个函数来进行装饰
# 并加入了复制函数名称、注释文档、参数列表等等的功能
# 在装饰器里面可以访问在装饰之前的函数的属性
# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 用于在定义包装器函数时发起调用 update_wrapper() 作为函数装饰器。
# 它等价于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)。

from time import ctime, sleep
from functools import wraps


def outer_args(bar):
    def outer(func):
        # 结构不变增加wraps
        @wraps(func)
        def inner(*args, **kwargs):
            print("%s called at %s" % (func.__name__, ctime()))
            ret = func(*args, **kwargs)
            print(bar)

        return inner

    return outer


@outer_args('foo_args')
def foo_args(x, y, z):
    """  __doc__  """
    return x + y + z


print(foo_args.__name__)

########################
# flask 使用@wraps()的案例
from functools import wraps


def requires_auth(func):
    @wraps(func)
    def auth_method(*args, **kwargs):
        if not auth:
            authenticate()
        return func(*args, **kwargs)

    return auth_method


@requires_auth
def func_demo():
    pass


########################

from functools import wraps


def logit(logfile='out.log'):
    def logging_decorate(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorate


@logit()
def myfunc():
    pass


myfunc()


# myfunc was called

@logit(logfile='custom.log')
def myfunc():
    pass


myfunc()
# myfunc was called

##########################
# 可以使用wrapt包替代@wraps
# # wrapt包 https://wrapt.readthedocs.io/en/latest/quick-start.html
#  @wrapt.decorator
#  def wrapper(func, instance, args, kwargs):
import wrapt


def with_arguments(arg1, arg2):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print(arg1, arg2, instance)
        return wrapped(*args, **kwargs)

    return wrapper


@with_arguments(1, 2)
def myfunc():
    pass


myfunc()
