# __getattribute__ 的底层原理是描述器
class Desc(object):
    """
    通过打印来展示描述器的访问流程
    """

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f'__get__{instance} {owner}')
        return self.name

    def __set__(self, instance, value):
        print(f'__set__{instance} {value}')
        self.name = value

    def __delete__(self, instance):
        print(f'__delete__{instance}')
        del self.name


class Obj(object):
    d1 = Desc('d1')
    d2 = Desc('d2')


o = Obj()
print(o.d1)

del o.d1
o.d1 = 777
print(o.d1)

# __get__<__main__.Obj object at 0x119aa3cd0> <class '__main__.Obj'>
# d1
# __delete__<__main__.Obj object at 0x119aa3cd0>
# __set__<__main__.Obj object at 0x119aa3cd0> 777
# __get__<__main__.Obj object at 0x119aa3cd0> <class '__main__.Obj'>
# 777
