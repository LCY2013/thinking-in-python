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
#outputs:
#I make decorators! And I accept arguments: Leonard Penny
#I am the decorator. Somehow you passed me arguments: Leonard Penny
#I am the wrapper around the decorated function.
#I can access all the variables
#   - from the decorator: Leonard Penny
#   - from the function call: Leslie Howard
#Then I can pass them to the decorated function
#I am the decorated function and only know about my arguments: Leslie Howard
