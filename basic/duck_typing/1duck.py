class Foo(object):
    # 用与方法
    def __str__(self):
        return '__str__ was called'

    # 用于字典操作
    def __getitem__(self, item):
        print(f'__getitem__ {item}')

    def __setitem__(self, key, value):
        print(f'__setitem__ {key}, {value}')

    def __delitem__(self, key):
        print(f'__delitem__ {key}')

    def __iter__(self):
        return iter([i for i in range(10)])


# __str__
bar = Foo()
print(bar)

# __XXitem__
bar['key']
bar['key'] = 'value'
del bar['key']

# iter
for i in bar:
    print(i)
