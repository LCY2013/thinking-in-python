import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_a():
    time.sleep(5)
    print(a.result())
    return 5


def wait_on_b():
    time.sleep(5)
    print(b.result())
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

# 当回调已关联了一个 Future 然后再等待另一个 Future 的结果时就会发产死锁情况
# https://docs.python.org/zh-cn/3.12/library/concurrent.futures.html#threadpoolexecutor
