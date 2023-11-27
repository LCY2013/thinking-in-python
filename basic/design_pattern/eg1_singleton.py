# 装饰器实现单实例模式
def singleton(cls):
    instances = {}

    def getInstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getInstance


@singleton
class SingletonCls(object):
    pass


sc1 = SingletonCls()
sc2 = SingletonCls()
print(id(sc1))
print(id(sc2))


##################
# __new__ 与 __init__ 的关系
class Foo(object):
    def __new__(cls, *args, **kwargs):
        print('trace __new__')
        return super().__new__(cls)

    def __init__(self, name):
        print('trace __init__')
        super().__init__()
        self.name = name


bar = Foo('test')
bar.name

# 相当于在执行下面的操作
bar = Foo.__new__(Foo, 'test')
if isinstance(bar, Foo):
    Foo.__init__(bar, 'test')


############################
# __new__ 方式实现单例模式
class Singleton(object):
    __isinstance = False  # 默认没有被初始化

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:
            return cls.__isinstance  # 返回实例化对象
        cls.__isinstance = object.__new__(cls)  # 实例化对象
        return cls.__isinstance


# object定义了一个名为Singleton的单例，它满足单例的3个需求：
# 一是只能有一个实例；
# 二是它必须自行创建这个实例；
# 三是它必须自行向整个系统提供这个实例。

class _Singleton(object):
    pass


singleton = _Singleton()
del _Singleton
another = Singleton.__class__()  # 没用绕过


# __new__

# 方法1,实现__new__方法
# 并在将一个类的实例绑定到类变量_instance上,
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._instance不为None,直接返回cls._instance

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance == super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)

# 解决并发，引入带锁版
import threading


class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            # double check locking
            if cls in cls.objs:
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
            return cls.objs[cls]
        finally:
            cls.objs_locker.release()


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)

# 利用经典的双检查锁机制，确保了在并发环境下Singleton的正确实现。
# 但这个方案并不完美，至少还有以下两个问题：
# ·如果Singleton的子类重载了__new__()方法，会覆盖或者干扰Singleton类中__new__()的执行，
# 虽然这种情况出现的概率极小，但不可忽视。
# ·如果子类有__init__()方法，那么每次实例化该Singleton的时候，
# __init__()都会被调用到，这显然是不应该的，__init__()只应该在创建实例的时候被调用一次。
# 这两个问题当然可以解决，比如通过文档告知其他程序员，子类化Singleton的时候，请务必记得调用父类的__new__()方法；
# 而第二个问题也可以通过偷偷地替换掉__init__()方法来确保它只调用一次。
# 但是，为了实现一个单例，做大量的、水面之下的工作让人感觉相当不Pythonic。
# 这也引起了Python社区的反思，有人开始重新审视Python的语法元素，发现模块采用的其实是天然的单例的实现方式。
# ·所有的变量都会绑定到模块。
# ·模块只初始化一次。
# ·import机制是线程安全的（保证了在并发状态下模块也只有一个实例）。
# 当我们想要实现一个游戏世界时，只需简单地创建World.py就可以了。

# World.py
import Sun


def run():
    while True:
        Sun.rise()
        Sun.set()


# main.py
import World

World.run()
