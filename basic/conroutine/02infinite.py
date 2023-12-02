# itertools的三个常见无限迭代器
import itertools

count = itertools.count()  # 计数器
print(next(count))
print(next(count))
print(next(count))

###############
cycle = itertools.cycle(('yes', 'no'))  # 循环计数器
print(next(cycle))
print(next(cycle))
print(next(cycle))

###############
repeat = itertools.repeat(10, times=2)  # 重复计数器
print(next(repeat))
print(next(repeat))
# print(next(repeat))

################
# 有限迭代器
for i in itertools.chain('ABC', [5, 6, 7], (9, 8, 7), {'key': 'value'}):
    print(i)

print('====================')


# Python3.3 引入了 yield from
# PEP-380
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
l = [5, 6, 7]
t = (9, 8, 7)
for i in chain(s, l, t):
    print(i)

print(list(chain(s, l, t)))

print('====================')


def chain(*iterables):
    for i in iterables:
        yield from i  # 替代内层循环


print(list(chain(s, l, t)))
