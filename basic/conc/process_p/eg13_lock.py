# 加进程锁
# 为了解决不同进程抢共享资源的问题，我们可以用加进程锁来解决
import multiprocessing as mp
import time


# 在job()中设置进程锁的使用，保证运行时只有一个进程可以执行job()函数
def job(v, num, l):
    if l.acquire():  # 加锁
        print(f'进程{mp.current_process().name}抢到锁，正在执行job()函数')
        for _ in range(5):
            time.sleep(0.1)
            v.value += num  # 获取共享内容
            print(v.value, end="|")
        print(f'进程{mp.current_process().name}执行完job()函数，释放锁')
        l.release()  # 释放锁
    else:
        print(f'进程{mp.current_process().name}没有抢到锁，正在等待')


def multicore():
    l = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享内容
    # 进程锁的信息传入各个进程中
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()

# 运行一下，让我们看看是否还会出现抢占资源的情况
# 显然，进程锁保证了进程p1的完整运行，然后才进行了进程p2的运行

# 在某些特定的场景下要共享string类型，方式如下：
from ctypes import c_char_p

str_val = mp.Value(c_char_p, b"Hello World")
