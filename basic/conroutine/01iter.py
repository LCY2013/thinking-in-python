alist = [1, 2, 3, 4, 5, 6, 7]

print(hasattr(alist, '__iter__'))  # True
print(hasattr(alist, '__next__'))  # False

for i in alist:
    print(i)

# 结论一  列表是可迭代对象，或称作可迭代（iterable）,
#         不是迭代器（iterator）

# __iter__方法是 iter() 函数所对应的魔法方法，
# __next__方法是 next() 函数所对应的魔法方法

###########################

g = (i for i in range(8))
print(g)
# <generator object <genexpr> at 0x1050f4110>

print(hasattr(g, '__iter__'))  # True
print(hasattr(g, '__next__'))  # True

print(g.__next__())
print(next(g))
for i in g:
    print(i)


# 结论二 生成器实现完整的迭代器协议

##############################
# 类实现完整的迭代器协议

class SampleIterator:
    def __iter__(self):
        return self

    def __next__(self):
        # Not The End
        if ...:
            return ...
        # Reach The End
        else:
            raise StopIteration


# 函数实现完整的迭代器协议
def SampleGenerator():
    yield ...
    yield ...
    yield ...  # yield语句


# 只要一个函数的定义中出现了 yield 关键词，则此函数将不再是一个函数，
# 而成为一个“生成器构造函数”，调用此构造函数即可产生一个生成器对象。

###################
# check iter
def check_iterator(obj):
    if hasattr(obj, '__iter__'):
        if hasattr(obj, '__next__'):
            print(f'{obj} is a iterator')  # 实现了完整的迭代器协议
        else:
            print(f'{obj} is a iterable')  # 可迭代对象
    else:
        print(f'{obj} can not iterable')  # 不可迭代对象


def func():
    yield range(5)


check_iterator(func)
check_iterator(func())
# <function func at 0x117c4b600> can not iterable
# <generator object func at 0x117a64e80> is a iterator

# 结论三： 有yield的函数是迭代器，执行yield语句之后才变成生成器构造函数
