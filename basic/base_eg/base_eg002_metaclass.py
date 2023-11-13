# http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
# https://realpython.com/blog/python/instance-class-and-static-methods-demystified/

# \	        实例方法	            类方法	                静态方法
# a = A()	a.foo(x)	    a.class_foo(x)	        a.static_foo(x)
# A	        不可用	        A.class_foo(x)	        A.static_foo(x)

def foo(x):
    print("executing foo(%s)" % (x))


# A 静态方法(staticmethod),类方法(classmethod)和实例方法
class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
a.foo(1)
a.class_foo(1)
a.static_foo(1)

# A.foo(1) error
A.class_foo(1)
A.static_foo(1)
