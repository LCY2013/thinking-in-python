list1 = []
for i in range(1, 11):
    if i > 5:
        list1.append(i ** 2)
print(list1)

# list1 == list2

# 列表推导式
list2 = [i ** 2 for i in range(1, 11) if i > 5]
print(list2)

# 循环嵌套
list3 = [str(i) + j for i in range(1, 5) for j in 'abcde']
print(list3)

# 用推导式将字典转换为列表
dict1 = {'a': 1, 'b': 2, 'c': 3}
list4 = [key + ":" + str(value) for key, value in dict1.items()]
print(list4)

# 用推导式生成字典
dict2 = {i: i * i for i in range(1, 10)}
print(dict2)

# 用推导式实现字典的k-v互换
dict3 = {v: k for k, v in dict2.items()}
print(dict3)

# 推导式生成集合
set1 = {i for i in 'Hello World' if i not in 'lo'}
print(set1)

# 推导式生成 生成器
generator1 = (i for i in range(0, 10))
print(generator1)
print(list(generator1))
