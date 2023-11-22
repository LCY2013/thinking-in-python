# 类 和 对象

class FirstClass:
    pass


a = FirstClass()
b = FirstClass()
# 不同内存地址，两个不同对象
type(a)
type(b)

a.__class__()
b.__class__()

id(a)
id(b)

# 类也是对象
c = FirstClass
d = c()
d.__class__()
