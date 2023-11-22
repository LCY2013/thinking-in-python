# https://github.com/taizilongxu/interview_python
# http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

a = 1


def fun(a):
    a = 2


fun(a)
print(a)  # 1

a = []


def fun(a):
    a.append(1)


fun(a)
print(a)  # [1]

a = 1


def fun(a):
    print("func_in", id(a))  # func_in 41322472
    a = 2
    print("re-point", id(a), id(2))  # re-point 41322448 41322448


print("func_out", id(a), id(1))  # func_out 41322472 41322472
fun(a)
print(a)  # 1

a = []


def fun(a):
    print("func_in", id(a))  # func_in 53629256
    a.append(1)


print("func_out", id(a))  # func_out 53629256
fun(a)
print(a)  # [1]

# 类型是属于对象的，而不是变量。而对象有两种,“可更改”（mutable）与“不可更改”（immutable）对象。在python中，strings, tuples, 和numbers是不可更改的对象，而 list, dict, set 等则是可以修改的对象。(这就是这个问题的重点)
#
# 当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用没有半毛关系了.所以第一个例子里函数把引用指向了一个不可变对象,当函数返回的时候,外面的引用没半毛感觉.而第二个例子就不一样了,函数内的引用指向的是可变对象,对它的操作就和定位了指针地址一样,在内存里进行修改.
