# 官方文档装饰器的其他用途举例

# 向一个函数添加属性
def attr(**kwargs):
    def decorate(f):
        for k in kwargs:
            setattr(f, k, kwargs[k])
        return f

    return decorate


@attr(versionadded='v1.0.0',
      author='fufeng')
def method(f):
    pass


print(dir(method))
print(method.author)

##############################
# 函数参数观察器
import functools


def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
        return result

    return decorated_function


@trace
def greet(greeting, name):
    return f'{greeting}, {name}!'


greet('better', 'me')


############################################

# Python3.7 引入 Data Class  PEP557

class MyClass(object):
    def __init__(self, var_a, var_b):
        self.var_a = var_a
        self.var_b = var_b

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return False
        return (self.var_a, self.var_b) == (other.var_a, other.var_b)


mc1 = MyClass(1, 2)
mc2 = MyClass(1, 2)

print(mc1 == mc2)  # True

from dataclasses import dataclass


@dataclass
class MyClass(object):
    var_a: str
    var_b: str


mc1 = MyClass('a', 'b')
mc2 = MyClass('a', 'b')

# 不用在类中重新封装 __eq__

print(mc1 == mc2)  # True
print(mc1.var_a)
# print(MyClass.var_a)  # AttributeError: type object 'MyClass' has no attribute 'var_a'

# 存在的问题: var_a var_b不能作为类属性访问

##########################


# 如下的类装饰器实现了一个用于类实例属性的Private声明
# 属性存储在一个实例上，或者从其一个类继承而来
# 不接受从装饰的类的外部对这样的属性的获取和修改访问
# 但是，仍然允许类自身在其方法中自由地访问那些名称
# 类似于Java中的private属性

traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def Private(*privates):
    def oneDecorate(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, item):
                trace('get: ', item)
                if item in privates:
                    raise TypeError('private attribute fetch:' + item)
                else:
                    return getattr(self.wrapped, item)

            def __setattr__(self, key, value):
                trace('set: ', key, value)
                if key == 'wrapped':  # 这里捕捉对wrapped的赋值
                    self.__dict__[key] = value
                elif key in privates:
                    raise TypeError('private attribute change:' + key)
                else:  # 这里捕捉对wrapped.attr的赋值
                    setattr(self.wrapped, key, value)

        return onInstance

    return oneDecorate


if __name__ == '__main__':
    traceMe = True


    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print(f'{self.label} => {self.data}')


    x = Doubler('X is', [1, 2, 3])
    y = Doubler('Y is', [4, 5, 6])
    print(x.label)
    x.display()
    x.double()
    x.display()
    print(y.label)
    y.display()
    y.double()
    y.label = 'Spam'
    y.display()

    # 运行结果
    # [set:  wrapped <__main__.Doubler object at 0x111029b50>]
    # [set:  wrapped <__main__.Doubler object at 0x1113ac5d0>]
    # [get:  label]
    # X is
    # [get:  display]
    # X is => [1, 2, 3]
    # [get:  double]
    # [get:  display]
    # X is => [2, 4, 6]
    # [get:  label]
    # Y is
    # [get:  display]
    # Y is => [4, 5, 6]
    # [get:  double]
    # [set:  label Spam]
    # [get:  display]
    # Spam => [8, 10, 12]
    # [get:  size]

    # 这些访问都会引发异常
    print(x.size())
    print(x.data)
    x.data = [1, 1, 1]
    x.size = lambda S: 0
    print(x.data)
    print(x.size())
