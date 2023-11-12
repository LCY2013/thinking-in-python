import threading
import time

# Lock普通锁不可重入，RLock普通锁可重入
mutex = threading.RLock()


class MyThread(threading.Thread):
    def __init__(self, name, num):
        threading.Thread.__init__(self)
        self.name = name
        self.num = num

    def run(self):
        if mutex.acquire(blocking=True):
            print('thread ' + self.name, 'get mutex')
            time.sleep(1)
            mutex.acquire()
            mutex.release()
        mutex.release()


if __name__ == '__main__':
    threads = []

    for i in range(10):
        t = MyThread('thread-' + str(i), i)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
