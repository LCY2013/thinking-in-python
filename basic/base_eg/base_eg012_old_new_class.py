# 新式 旧式 类
# http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
# http://www.cnblogs.com/btchenguang/archive/2012/09/17/2689146.html
# 新式类很早在2.2就出现了,所以旧式类完全是兼容的问题,Python3里的类全部都是新式类.
# 这里有一个MRO问题可以了解下(新式类继承是根据C3算法,旧式类是深度优先),<Python核心编程>里讲的也很多.

class A():
    def foo1(self):
        print("A")


class B(A):
    def foo2(self):
        pass


class C(A):
    def foo1(self):
        print("C")


class D(B, C):
    pass


d = D()
d.foo1()


# 新式类
# C

# 旧式类
# 按照经典类的查找顺序从左到右深度优先的规则，在访问d.foo1()的时候,D这个类是没有的..那么往上查找,先找到B,
# 里面没有,深度优先,访问A,找到了foo1(),所以这时候调用的是A的foo1()，从而导致C重写的foo1()被绕过
# A
