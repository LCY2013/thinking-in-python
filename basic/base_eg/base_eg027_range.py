# http://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x
from jieba.posseg.viterbi import xrange

# 都在循环时使用，xrange内存性能更好。 for i in range(0, 20): for i in xrange(0, 20):
# What is the difference between range and xrange functions in Python 2.X?
# range creates a list,
# so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.
# xrange is a sequence object that evaluates lazily.

# 在 Python 3.0 中只有一个range，它的行为与 2.x 类似xrange，但没有最小和最大端点的限制。

for i in range(0, 20):
    print(i)

# for i in xrange(0, 20):
#     print(i)

for i in list(range(0, 20)):
    print(i)

# python -m timeit 'for i in range(1000000):' ' pass'
# python -m timeit 'for i in list(range(1000000)):' ' pass'
