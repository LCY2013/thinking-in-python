def chain(num):
    for i in range(num):
        yield i


number = 10
y = chain(number)
print(next(y))
print(list(y))
# next(y) StopIteration

# 迭代器
mylist = [1, 2, 3]
for i in mylist:
    print(mylist)

mylist = [x * x for x in range(3)]
for i in mylist:
    print(i)
# 可以使用 for .. in .. 语法的叫做一个迭代器：列表，字符串，文件……你经常使用它们是因为你可以如你所愿的读取其中的元素，
# 但是你把所有的值都存储到了内存中，如果你有大量数据的话这个方式并不是你想要的。

# 生成器
# 生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据:
mygenerator = (x * x for x in range(10))
for i in mygenerator:
    print(i)


# 看起来除了把 [] 换成 () 外没什么不同。但是，你不可以再次使用 for i in mygenerator , 因为生成器只能被迭代一次：先计算出0，然后继续计算1，然后计算4，一个跟一个的…

# yield 关键字
# yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器
def create_generator():
    mylist = range(5)
    for i in mylist:
        yield i * i


# create generator
cg = create_generator()
print(cg)
for i in cg:
    print(i)
# 为了精通 yield ,你必须要理解：当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象，这有点蹊跷不是吗。
# 第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值.
# 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。
# 如果生成器内部没有定义 yield 关键字，那么这个生成器被认为成空的。这种情况可能因为是循环进行没了，或者是没有满足 if/else 条件。

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)


# 控制生成器的穷尽
class Bank(object):
    crisis = False

    def create_atm(self):
        while not self.crisis:
            yield '$1000000000'


hsbc = Bank()
corner_street_atm = hsbc.create_atm()
print(next(corner_street_atm))
print(corner_street_atm.__next__())
print([next(corner_street_atm) for i in range(5)])
# ['$1000000000', '$1000000000', '$1000000000', '$1000000000', '$1000000000']
hsbc.crisis = True
print(next(corner_street_atm))
# StopIteration
wall_street_atm = hsbc.create_atm()
print(next(wall_street_atm))
# StopIteration
hsbc.crisis = False
wall_street_atm = hsbc.create_atm()
print(next(wall_street_atm))
for cash in wall_street_atm:
    print(cash)

# Itertools,你最好的朋友
# itertools 包含了很多特殊的迭代方法。是不是曾想过复制一个迭代器?串联两个迭代器？把嵌套的列表分组？不用创造一个新的列表的 zip/map?
# 只要 import itertools
# 需要个例子？让我们看看比赛中4匹马可能到达终点的先后顺序的可能情况:
import itertools

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
# <itertools.permutations object at 0x1170a3740>
print(list(itertools.permutations(horses)))
# [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

# 迭代器的内部机理
# 迭代是一个实现可迭代对象(实现的是 __iter__() 方法)和迭代器(实现的是 __next__() 方法)的过程。可迭代对象是你可以从其获取到一个迭代器的任一对象。迭代器是那些允许你迭代可迭代对象的对象。
