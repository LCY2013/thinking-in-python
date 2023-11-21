# http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
# http://blog.csdn.net/mrlevo520/article/details/51712440

# super() 可以让您避免显式引用基类，这很好。但主要优点是多重继承，可以发生各种有趣的事情。如果您还没有看过 super 的标准文档，请参阅。
#
# 请注意，Python 3.0 中的语法发生了变化：您可以直接说 super()。__init__() 而不是 super(ChildB, self)。__init__() 在我看来，这更好一些。

class Base(object):
    def __init__(self):
        print("Base created")


class ChildA(Base):
    def __init__(self):
        Base.__init__(self)


class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()


ChildA()
ChildB()
