# 钻石继承
class BaseClass(object):
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        print("Calling method on Left Subclass")
        self.num_left_calls += 1


# class RightSubclass(BaseClass):
class RightSubclass(object):
    num_right_calls = 0

    def call_me(self):
        print("Calling method on Right Subclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    pass


a = Subclass()
a.call_me()

print(Subclass.__bases__)
print(Subclass.mro())

# MRO 的顺序按照以下规则确定：
# 子类永远在父类前面。
# 如果有多个父类，它们在 MRO 中的相对顺序取决于它们在类定义中的出现顺序。
# 如果有多个继承路径，C3 算法确保维持相对顺序。

# 广度优先， 另外Python3 中不加(object)也是新式类，但是为了代码不会误运行在python2下产生意外结果，仍然建议增加
# >>> Subclass.mro()
# [<class '__main__.Subclass'>, <class '__main__.LeftSubclass'>, <class '__main__.RightSubclass'>, <class '__main__.BaseClass'>, <class 'object'>]
# 临接表表示继承关系图
# Subclass: [LeftSubclass, RightSubclass]
# LeftSubclass: [BaseClass]
# RightSubclass: [BaseClass]
# BaseClass: [object]
#                   object
#                  BaseClass
#   LeftSubclass               RightSubclass
#                  Subclass

#  修改RightSubclass 的 父类为 Object
# >>> Subclass.mro()
# [<class '__main__.Subclass'>, <class '__main__.LeftSubclass'>, <class '__main__.BaseClass'>, <class '__main__.RightSubclass'>, <class 'object'>]
# 临接表表示继承关系图
# Subclass: [LeftSubclass, RightSubclass]
# LeftSubclass: [BaseClass]
# RightSubclass: [object]
# BaseClass: [object]
# BaseClass: [object]
#                   object
#      BaseClass             RightSubclass
#   LeftSubclass
#                  Subclass



