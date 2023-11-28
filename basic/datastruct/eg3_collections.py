# 命名元组
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, y=20)
print(p.x + p.y)
print(p[0] + p[1])
x, y = p
print(p)

# 统计计数器
from collections import Counter

mystring = ['a', 'b', 'c', 'd', 'd', 'd', 'd', 'c', 'c', 'e']
# 获取出现频率最高的三个词
cnt = Counter(mystring)
print(cnt.most_common(3))
print(cnt['b'])

# 双向队列
from collections import deque

d = deque('uvw')
d.append('xyz')
d.appendleft('rst')
print(d)
# deque(['rst', 'u', 'v', 'w', 'xyz'])
