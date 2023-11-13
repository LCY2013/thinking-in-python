# http://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block
# 类变量：
# 是可在类的所有实例之间共享的值（也就是说，它们不是单独分配给每个实例的）。例如下例中，num_of_instance 就是类变量，用于跟踪存在着多少个Test 的实例。

# 实例变量：
# 实例化之后，每个实例单独拥有的变量。

class Person:
    name = "aaa"


p1 = Person()
p2 = Person()
p1.name = "bbb"
print(p1.name)  # bbb
print(p2.name)  # aaa
print(Person.name)  # aaa


class Person1:
    name = []


p1 = Person1()
p2 = Person1()
p1.name.append(1)
# p1.name = [2]
print(p1.name)  # [1]
print(p2.name)  # [1]
print(Person1.name)  # [1]


class Test(object):
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


if __name__ == '__main__':
    print(Test.num_of_instance)  # 0
    t1 = Test('jack')
    print(Test.num_of_instance)  # 1
    t2 = Test('lucy')
    print(t1.name, t1.num_of_instance)  # jack 2
    print(t2.name, t2.num_of_instance)  # lucy 2
