# 迭代器有效性测试
a_dict = {'a': 1, 'b': 2}
a_dict_iter = iter(a_dict)

print(next(a_dict_iter))

a_dict['c'] = 3
# print(next(a_dict_iter))
# RuntimeError: dictionary changed size during iteration
# RuntimeError: 字典进行插入操作后，字典迭代器会立即失效

# 尾插入操作不会损坏指向当前元素的List迭代器,列表会自动变长

# 迭代器一旦耗尽，永久损坏
x = iter([y for y in range(5)])
for i in x:
    print(i)

# x.__next__()
# StopIteration
