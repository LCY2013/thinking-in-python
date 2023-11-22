class Foo(object):
    """类三种方法语法形式"""

    def instance_method(self):
        print('类的实例方法，只能被实例对象调用')

    @classmethod
    def class_method(cls):
        print('类方法')

    @staticmethod
    def static_method():
        print('静态方法')


foo = Foo()
foo.instance_method()
foo.class_method()
foo.static_method()
print('----------------')
# Foo.instance_method()
# TypeError: Foo.instance_method() missing 1 required positional argument: 'self'
Foo.class_method()
Foo.static_method()
