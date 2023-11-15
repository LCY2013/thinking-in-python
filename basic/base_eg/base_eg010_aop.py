# http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python
# http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/3/README.html
# 装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。
# 装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
# 概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Do I have args?:")
        print(args)
        print(kwargs)
        # Then you unpack the arguments, here *args, **kwargs
        # If you are not familiar with unpacking, check:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")


function_with_no_argument()


# outputs
# Do I have args?:
# ()
# {}
# Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)


# outputs
# Do I have args?:
# (1, 2, 3)
# {}
# 1 2 3

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print("Do {0}, {1} and {2} like platypus? {3}".format(a, b, c, platypus))


function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")


# outputs
# Do I have args ? :
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# Do Bill, Linus and Steve like platypus? Indeed!

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):  # You can now add a default value
        print("I am {0}, what did you think?".format(self.age + lie))


m = Mary()
m.sayYourAge()


# outputs
# Do I have args?:
# (<__main__.Mary object at 0xb7d303ac>,)
# {}
# I am 28, what did you think?

# Decorators are ORDINARY functions
def my_decorator(func):
    print("I am an ordinary function")

    def wrapper():
        print("I am function returned by the decorator")
        func()

    return wrapper


# Therefore, you can call it without any "@"

def lazy_function():
    print("zzzzzzzz")


decorated_function = my_decorator(lazy_function)

decorated_function()


# outputs: I am an ordinary function

# It outputs "I am an ordinary function", because that’s just what you do:
# calling a function. Nothing magic.

@my_decorator
def lazy_function():
    print("zzzzzzzz")


# outputs: I am an ordinary function

lazy_function()


def decorator_maker():
    print("I make decorators! I am executed only once: "
          "when you make me create a decorator.")

    def my_decorator(func):
        print("I am a decorator! I am executed only when you decorate a function.")

        def wrapped():
            print("I am the wrapper around the decorated function. "
                  "I am called when you call the decorated function. "
                  "As the wrapper, I return the RESULT of the decorated function.")
            return func()

        print("As the decorator, I return the wrapped function.")

        return wrapped

    print("As a decorator maker, I return a decorator")
    return my_decorator


# Let’s create a decorator. It’s just a new function after all.
new_decorator = decorator_maker()


# outputs:
# I make decorators! I am executed only once: when you make me create a decorator.
# As a decorator maker, I return a decorator

# Then we decorate the function

def decorated_function():
    print("I am the decorated function.")


decorated_function = new_decorator(decorated_function)
# outputs:
# I am a decorator! I am executed only when you decorate a function.
# As the decorator, I return the wrapped function

# Let’s call the function:
decorated_function()


# outputs:
# I am the wrapper around the decorated function. I am called when you call the decorated function.
# As the wrapper, I return the RESULT of the decorated function.
# I am the decorated function.

@decorator_maker()
def decorated_function():
    print("I am the decorated function.")


# outputs:
# I make decorators! I am executed only once: when you make me create a decorator.
# As a decorator maker, I return a decorator
# I am a decorator! I am executed only when you decorate a function.
# As the decorator, I return the wrapped function.

# Eventually:
decorated_function()


# outputs:
# I am the wrapper around the decorated function. I am called when you call the decorated function.
# As the wrapper, I return the RESULT of the decorated function.
# I am the decorated function.

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print("I make decorators! And I accept arguments: {0}, {1}".format(decorator_arg1, decorator_arg2))

    def my_decorator(func):
        # The ability to pass arguments here is a gift from closures.
        # If you are not comfortable with closures, you can assume it’s ok,
        # or read: https://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print("I am the decorator. Somehow you passed me arguments: {0}, {1}".format(decorator_arg1, decorator_arg2))

        # Don't confuse decorator arguments and function arguments!
        def wrapped(function_arg1, function_arg2):
            print("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("I am the decorated function and only knows about my arguments: {0}"
          " {1}".format(function_arg1, function_arg2))


decorated_function_with_arguments("Rajesh", "Howard")
# outputs:
# I make decorators! And I accept arguments: Leonard Sheldon
# I am the decorator. Somehow you passed me arguments: Leonard Sheldon
# I am the wrapper around the decorated function.
# I can access all the variables
#   - from the decorator: Leonard Sheldon
#   - from the function call: Rajesh Howard
# Then I can pass them to the decorated function
# I am the decorated function and only knows about my arguments: Rajesh Howard

c1 = "Penny"
c2 = "Leslie"


@decorator_maker_with_arguments("Leonard", c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("I am the decorated function and only knows about my arguments:"
          " {0} {1}".format(function_arg1, function_arg2))


decorated_function_with_arguments(c2, "Howard")


# outputs:
# I make decorators! And I accept arguments: Leonard Penny
# I am the decorator. Somehow you passed me arguments: Leonard Penny
# I am the wrapper around the decorated function.
# I can access all the variables
#   - from the decorator: Leonard Penny
#   - from the function call: Leslie Howard
# Then I can pass them to the decorated function
# I am the decorated function and only know about my arguments: Leslie Howard

def decorator_with_args(decorator_to_enhance):
    """
    This function is supposed to be used as a decorator.
    It must decorate an other function, that is intended to be used as a decorator.
    Take a cup of coffee.
    It will allow any decorator to accept an arbitrary number of arguments,
    saving you the headache to remember how to do that every time.
    """

    # We use the same trick we did to pass arguments
    def decorator_maker(*args, **kwargs):
        # We create on the fly a decorator that accepts only a function
        # but keeps the passed arguments from the maker.
        def decorator_wrapper(func):
            # We return the result of the original decorator, which, after all,
            # IS JUST AN ORDINARY FUNCTION (which returns a function).
            # Only pitfall: the decorator must have this specific signature or it won't work:
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


# You create the function you will use as a decorator. And stick a decorator on it :-)
# Don't forget, the signature is "decorator(func, *args, **kwargs)"
@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print("Decorated with {0} {1}".format(args, kwargs))
        return func(function_arg1, function_arg2)

    return wrapper


# Then you decorate the functions you wish with your brand new decorated decorator.

@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print("Hello {0} {1}".format(function_arg1, function_arg2))


decorated_function("Universe and", "everything")


# outputs:
# Decorated with (42, 404, 1024) {}
# Hello Universe and everything

# Whoooot!

# 最佳实践：装饰器
# 装饰器是在 Python 2.4 中引入的，因此请确保您的代码将在 >= 2.4 上运行。
# 装饰器减慢了函数调用的速度。记住这一点。
# 您无法取消装饰函数。（有一些技巧可以创建可以删除的装饰器，但没有人使用它们。）因此，一旦函数被装饰，它就会为所有代码进行装饰。
# 装饰器包装函数，这会使它们难以调试。（从 Python >= 2.5 开始，这会变得更好；见下文。）
# 该functools模块是在 Python 2.5 中引入的。它包括 function functools.wraps()，它将修饰函数的名称、模块和文档字符串复制到其包装器中。
#
# （有趣的事实：functools.wraps()是一个装饰器！）

# For debugging, the stacktrace prints you the function __name__
def foo():
    print("foo")


print(foo.__name__)


# outputs: foo

# With a decorator, it gets messy
def bar(func):
    def wrapper():
        print("bar")
        return func()

    return wrapper


@bar
def foo():
    print("foo")


print(foo.__name__)
# outputs: wrapper

# "functools" can help for that
import functools


def bar(func):
    # We say that "wrapper", is wrapping "func"
    # and the magic begins
    @functools.wraps(func)
    def wrapper():
        print("bar")
        return func()

    return wrapper


@bar
def foo():
    print("foo")


print(foo.__name__)


# outputs: foo

####################装饰器作用#######################
def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("{0} {1}".format(func.__name__, time.clock() - t))
        return res

    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("{0} {1} {2}".format(func.__name__, args, kwargs))
        return res

    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """

    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))


print(reverse_string("Able was I ere I saw Elba"))
print(reverse_string(
    "A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))


# outputs:
# reverse_string ('Able was I ere I saw Elba',) {}
# wrapper 0.0
# wrapper has been used: 1x
# AblE was I ere I saw elbA
# reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
# wrapper 0.0
# wrapper has been used: 2x
# !amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A

@counter
@benchmark
@logging
def get_random_futurama_quote():
    from urllib import request
    result = request.urlopen("http://subfusion.net/cgi-bin/quote.pl?quote=futurama").read()
    try:
        value = result.split("<br><b><hr><br>")[1].split("<br><br><hr>")[0]
        return value.strip()
    except:
        return "No, I'm ... doesn't!"


print(get_random_futurama_quote())
print(get_random_futurama_quote())

# outputs:
# get_random_futurama_quote () {}
# wrapper 0.02
# wrapper has been used: 1x
# The laws of science be a harsh mistress.
# get_random_futurama_quote () {}
# wrapper 0.01
# wrapper has been used: 2x
# Curse you, merciful Poseidon!

# Python本身提供了几种装饰器：property、staticmethod等。
#
# Django 使用装饰器来管理缓存和查看权限。
# 扭曲为假内联异步函数调用。

from functools import wraps


def makebold(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"

    return wrapper


def makeitalic(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"

    return wrapper


@makebold
@makeitalic
def hello():
    return "hello world"


@makebold
@makeitalic
def log(s):
    return s


print(hello())  # returns "<b><i>hello world</i></b>"
print(hello.__name__)  # with functools.wraps() this returns "hello"
print(log('hello'))  # returns "<b><i>hello</i></b>"

from functools import wraps


def wrap_in_tag(tag):
    def factory(func):
        @wraps(func)
        def decorator():
            return '<%(tag)s>%(rv)s</%(tag)s>' % (
                {'tag': tag, 'rv': func()})

        return decorator

    return factory


@wrap_in_tag('b')
@wrap_in_tag('i')
def say():
    return 'hello'


makebold = wrap_in_tag('b')
makeitalic = wrap_in_tag('i')


@makebold
@makeitalic
def say():
    return 'hello'


def say():
    return 'hello'


# say = wrap_in_tag('b')(wrap_in_tag('i')(say)))
from abc import ABCMeta, abstractmethod


class Decorator(metaclass=ABCMeta):
    """ Acts as a base class for all decorators """

    def __init__(self):
        self.method = None

    def __call__(self, method):
        self.method = method
        return self.call

    @abstractmethod
    def call(self, *args, **kwargs):
        return self.method(*args, **kwargs)


class MakeBold(Decorator):
    def call(self):
        return "<b>" + self.method() + "</b>"


class MakeItalic(Decorator):
    def call(self):
        return "<i>" + self.method() + "</i>"


@MakeBold()
@MakeItalic()
def say():
    return "Hello"


class ApplyRecursive(Decorator):

    def __init__(self, *types):
        super().__init__()
        if not len(types):
            types = (dict, list, tuple, set)
        self._types = types

    def call(self, arg):
        if dict in self._types and isinstance(arg, dict):
            return {key: self.call(value) for key, value in arg.items()}

        if set in self._types and isinstance(arg, set):
            return set(self.call(value) for value in arg)

        if tuple in self._types and isinstance(arg, tuple):
            return tuple(self.call(value) for value in arg)

        if list in self._types and isinstance(arg, list):
            return list(self.call(value) for value in arg)

        return self.method(arg)


@ApplyRecursive(tuple, set, dict)
def double(arg):
    return 2 * arg


print(double(1))
print(double({'a': 1, 'b': 2}))
print(double({1, 2, 3}))
print(double((1, 2, 3, 4)))
print(double([1, 2, 3, 4, 5]))


# 2
# {'a': 2, 'b': 4}
# {2, 4, 6}
# (2, 4, 6, 8)
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# decorator.py
def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
            if "css_class" in kwds else ""

        def wrapped(*args, **kwds):
            return "<" + tag + css_class + ">" + fn(*args, **kwds) + "</" + tag + ">"

        return wrapped

    # return decorator dont call it
    return real_decorator


@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"


print(hello())


# class.py
class makeHtmlTagClass(object):
    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
            if css_class != "" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class + ">" \
                + fn(*args, **kwargs) + "</" + self._tag + ">"

        return wrapped


@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)


print(hello("Your name"))


############################################################
#
#    decorators
#
############################################################

def bold(fn):
    def decorate():
        # surround with bold tags before calling original function
        return "<b>" + fn() + "</b>"

    return decorate


def uk(fn):
    def decorate():
        # swap month and day
        fields = fn().split('/')
        date = fields[1] + "/" + fields[0] + "/" + fields[2]
        return date

    return decorate


import datetime


def getDate():
    now = datetime.datetime.now()
    return "%d/%d/%d" % (now.day, now.month, now.year)


@bold
def getBoldDate():
    return getDate()


@uk
def getUkDate():
    return getDate()


@bold
@uk
def getBoldUkDate():
    return getDate()


print(getDate())
print(getBoldDate())
print(getUkDate())
print(getBoldUkDate())
# what is happening under the covers
print(bold(uk(getDate))())
# 15/11/2023
# <b>15/11/2023</b>
# 11/15/2023
# <b>11/15/2023</b>
# <b>11/15/2023</b>


from decopatch import function_decorator, DECORATED
from makefun import wraps


@function_decorator
def makestyle(st='b', fn=DECORATED):
    open_tag = "<%s>" % st
    close_tag = "</%s>" % st

    @wraps(fn)
    def wrapped(*args, **kwargs):
        return open_tag + fn(*args, **kwargs) + close_tag

    return wrapped


from decopatch import function_decorator, WRAPPED, F_ARGS, F_KWARGS


@function_decorator
def makestyle(st='b', fn=WRAPPED, f_args=F_ARGS, f_kwargs=F_KWARGS):
    open_tag = "<%s>" % st
    close_tag = "</%s>" % st
    return open_tag + fn(*f_args, **f_kwargs) + close_tag


@makestyle
@makestyle('i')
def hello(who):
    return "hello %s" % who


assert hello('world') == '<b><i>hello world</i></b>'
