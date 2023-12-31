# version 3
def line_conf():
    b = 10

    def line(x):
        '''如果line()的定义中引用了外部的变量'''
        return 2 * x + b

    return line


b = -1
my_line = line_conf()
print(my_line(5))

# 编译后函数体保存的局部变量
print(my_line.__code__.co_varnames)
# 编译后函数体保存的自由变量
print(my_line.__code__.co_freevars)
# 自由变量真正的值
print(my_line.__closure__[0].cell_contents)


# 20
# ('x',)
# ('b',)
# 10

#####################
# 函数和对象比较有哪些不同的属性
# 函数还有哪些属性
def func():
    pass


func_magic = dir(func)


# 常规对象有哪些属性
class ClassA():
    pass


obj = ClassA()
obj_magic = dir(obj)

# 比较函数和对象的默认属性
print(set(func_magic) - set(obj_magic))
