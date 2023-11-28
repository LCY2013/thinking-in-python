class Klass(object):
    def A(self):
        pass

    # 定义覆盖上面的定义
    def A(self, a, b):
        print(f'{a},{b}')


inst = Klass()
# 没有实现重载 TypeError: Klass.A() missing 2 required positional arguments: 'a' and 'b'
inst.A()
