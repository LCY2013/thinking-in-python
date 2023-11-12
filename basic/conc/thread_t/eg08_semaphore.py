# 信号量：内部实现一个计数器，占用信号量的线程数超过指定值时，线程被阻塞，当计数器减为0时，线程被唤醒
import threading
import time


def run(n):
    semaphore.acquire()  # 占用信号量
    print("run the thread %s" % n)
    time.sleep(1)
    semaphore.release()  # 释放信号量


semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()
