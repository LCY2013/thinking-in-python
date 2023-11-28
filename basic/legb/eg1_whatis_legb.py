# 问题代码一
# def func():
#     var = 100
# func()
# print(var)

# 问题代码二
# def func():
#     print(var)
# func()
# var = 100

var = 100


def func():
    print(var)


func()

# L G
x = 'Global'


def func1():
    x = 'Enclosing'

    def func2():
        x = 'Local'
        print(x)

    func2()


print(x)
func1()

# E
x = 'Global'


def func3():
    x = 'Enclosing'

    def func4():
        print(x)

    return func4


f3 = func3()
f3()

# B Built-in
print(dir(__builtins__))
