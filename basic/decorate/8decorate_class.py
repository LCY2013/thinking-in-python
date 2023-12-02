# 装饰类
def decorate(aclass):
    class newclass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aclass(args)

        def display(self):
            # 将runtimes()替换为display()
            self.times += 1
            print('run times', self.times)
            self.wrapped.display()

    return newclass


@decorate
class MyClass(object):
    def __init__(self, number):
        self.number = number

    # 重新display
    def display(self):
        print('number is ', self.number)


six = MyClass(7)
for i in range(5):
    six.display()
