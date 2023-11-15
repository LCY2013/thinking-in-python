# __new__ 和 __init__ 区别 ？
# __new__是一个静态方法,而__init__是一个实例方法.
# __new__方法会返回一个创建的实例,而__init__什么都不返回.
# 只有在__new__返回一个cls的实例时后面的__init__才能被调用.
# 当创建一个新实例时调用__new__,初始化一个实例时用__init__.
# http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init
# __metaclass__是创建类时起作用.所以我们可以分别使用__metaclass__,__new__和__init__来分别在类创建,实例创建和实例初始化的时候做一些小手脚.

