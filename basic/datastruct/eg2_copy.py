# 容器序列的拷贝问题
old_list = [i for i in range(1, 11)]

new_list1 = old_list
new_list2 = list(old_list)

# 切片操作
new_list3 = old_list[:]

# 嵌套对象
old_list.append([11, 12])

print(old_list, new_list1, new_list2, new_list3)

import copy

new_list4 = copy.copy(old_list)
new_list5 = copy.deepcopy(old_list)

assert new_list4 == new_list5  # True
# assert new_list4 is new_list5  # False AssertionError

old_list[10][0] = 13

print(old_list, new_list1, new_list2, new_list3)

print(new_list4, new_list5)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
