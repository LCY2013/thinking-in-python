# 问题1: a、b、c三个id是否相同
a = 123
b = 123
c = a
print(id(a))
print(id(b))
print(id(c))

a = 10000
b = 10000
print(id(a))
print(id(b))

# 4376706552
# 4376706552
# 4376706552
# 4363353936
# 4363353936

#############
# 问题2: a、b、c的值分别是多少
a = 456
print(id(a))
c = 789
c = b = a

print(a, b, c)
# 456 456 456

#############
# 问题3: x、y的值分别是什么
x = [1, 2, 3]
y = x
x.append(4)
print(x)
print(y)
# [1,2,3,4]
# [1,2,3,4]


#############
# 问题4: a、b的值分别是多少
a = [1, 2, 3]
b = a
a = [4, 5, 6]
print(a)
print(b)
# [4,5,6]
# [1,2,3]

#############
# 问题5: a、b的值分别是多少
a = [1, 2, 3]
b = a
a[0], a[1], a[2] = 4, 5, 6
print(a)
print(b)
# [4,5,6]
# [4,5,6]