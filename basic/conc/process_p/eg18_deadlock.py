# join dead lock
from multiprocessing import Process, Queue


def f(q):
    q.put('X' * 100000)


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    p.join()  # this deadlocks
    obj = q.get()
    print(obj)
    print('main process exit')

# 注释掉上面的join()，程序就会正常退出，说明join()是死锁的原因。
# 或者交互join()和get()，程序也会正常退出。
