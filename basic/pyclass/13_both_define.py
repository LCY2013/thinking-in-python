class Human(object):
    """
        同时存在的调用顺序
    """

    def __init__(self):
        self.age = 18

    def __getattribute__(self, item):
        print('Human:__getattribute__')
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print('Human:__getattr__')
        return 'Err 404 ,你请求的参数不存在'


h1 = Human()

# 如果同时存在，执行顺序是 __getattribute__ > __getattr__ > __dict__
print(h1.age)
print(h1.noattr)
# 注意输出，noattr的调用顺序
