class Human(object):

    def __getattribute__(self, item):
        """
                   将不存在的属性设置为100并返回,模拟getattr行为
        """
        print('Human2:__getattribute__')
        try:
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item] = 100
            return 100


h1 = Human()
print(h1.noattr)
print(h1.__dict__)

# 思考：有更简洁的写法吗？
