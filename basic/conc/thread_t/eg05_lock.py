import threading
import time

num = 0
mutex = threading.Lock()


class MyThread(threading.Thread):

    def __init__(self, name, num):
        super().__init__()
        self.name = name
        self.num = num

    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire():  # 加锁
            num += 1
            print(f'{self.name} : name value is {num}')
        mutex.release()  # 解锁


if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = MyThread(name=f'thread-{i}', num=i)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
