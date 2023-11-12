# Python3.2 中引入了 concurrent.futures 库，利用这个库可以很方便的实现多线程，多进程。
from concurrent.futures import ThreadPoolExecutor
import time


def func(args):
    print(f'call func {args}')


if __name__ == '__main__':
    seed = ['a', 'b', 'c', 'd', 'e', 'f']

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(func, seed)

    time.sleep(1)

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(func, seed)

    time.sleep(1)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 2, 3)
        print(future.result())
