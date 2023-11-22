class Human(object):
    # 人为约定不可修改
    _age = 0

    # 私有属性
    __fly = False

    # 魔术方法，不会自动改名
    # 如 __init__


# 自动改名机制
Human.__dict__
# mappingproxy({'__module__': '__main__', '_age': 0, '_Human__fly': False, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None, '__annotations__': {}})
