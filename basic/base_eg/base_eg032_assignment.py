# 有时候我就是不想要默认值啊，只是想单单判断默认参数有没有值传递进来，那该怎么办？
_no_value = object()


def print_value(a, b=_no_value):
    if b is _no_value:
        print('not input b')
        return
    print('input b')
    return


print_value(1)
print_value(1, 2)
print_value(1, b=2)

print('\n'.join([' '.join('%dx%d=%2d' % (x, y, x * y) for x in range(1, y + 1)) for y in range(1, 10)]))
