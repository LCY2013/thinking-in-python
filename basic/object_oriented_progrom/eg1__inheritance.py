# 继承
# 父类
class People(object):
    def __init__(self):
        self.gene = 'XY'

    def walk(self):
        print('I can walk')


# 子类
class Man(People):
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('work hard')


class Woman(People):
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('buy buy buy')


man = Man('fufeng')
woman = Woman('magic')

# 问题1 gene有没有被继承？ AttributeError: 'Man' object has no attribute 'gene'
# man.gene

# 问题2 People的父类是谁？ (<class 'object'>,)
print(People.__bases__)


# 问题3 能否实现多重层级继承 (<class '__main__.Woman'>, <class '__main__.Man'>)
class FF(Woman, Man):
    pass


print(FF.__bases__)

# 问题4 能否实现多个父类同时继承
