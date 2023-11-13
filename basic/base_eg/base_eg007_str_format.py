# .format在许多方面看起来更便利.对于%最烦人的是它无法同时传递一个变量和元组.你可能会想下面的代码不会有什么问题:
# http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format
name = 'fufeng'
print("hi there %s" % name)

name = (1, 'fufeng')
# print("hi there %s" % name) # TypeError: not all arguments converted during string formatting
print("hi there %s" % (name,))  # 提供一个单元素的数组而不是一个参数
print(f'hi there {name}')
print(r'hi there {name}')
