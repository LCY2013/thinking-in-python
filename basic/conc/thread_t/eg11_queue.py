import queue

q = queue.Queue(5)
q.put(111)  # 入队
q.put(222)
q.put(333)
q.put(444)

print(q.get())  # 出队
print(q.get())
q.task_done()  # 每次从queue中get一个数据之后，当处理好相关问题，最后调用该方法
# 以提示q.join()是否停止阻塞，让线程继续执行或者退出
print(q.qsize())  # 队列中元素的个数，队列的大小
print(q.empty())  # 队列是否为空
print(q.full())  # 队列是否已满

#####################

import queue
import threading
import random
import time

writelock = threading.Lock()


class Producer(threading.Thread):
    def __init__(self, q, con, name):
        threading.Thread.__init__(self)
        self.q = q
        self.con = con
        self.name = name
        print(f'Producer {self.name} is running')

    def run(self):
        while 1:
            global writelock  # 获取锁对象
            self.con.acquire()  # 获取锁对象

            if self.q.full():  # 队列满
                with writelock:
                    print(f'Producer {self.name} is full, producer wait')
                self.con.wait()  # 等待资源
            else:
                value = random.randint(0, 10)
                with writelock:
                    print(f'{self.name} put value {self.name} {str(value)} in queue')

                self.q.put((f'{self.name} : {str(value)}'))  # 入队
                self.con.notify()  # 通知消费者
                time.sleep(1)
        self.con.release()


class Consumer(threading.Thread):
    def __init__(self, q, con, name):
        threading.Thread.__init__(self)
        self.q = q
        self.con = con
        self.name = name
        print(f'Consumer {self.name} is running')

    def run(self):
        while 1:
            global writelock
            self.con.acquire()
            if self.q.empty():  # 队列空
                with writelock:
                    print(f'Consumer {self.name} is empty, consumer wait')
                self.con.wait()  # 等待资源
            else:
                value = self.q.get()  # 出队
                with writelock:
                    print(f'{self.name} get value {value} from queue')
                self.con.notify()  # 通知生产者
                time.sleep(1)
        self.con.release()


if __name__ == '__main__':
    q = queue.Queue(10)
    con = threading.Condition()  # 条件变量锁

    p1 = Producer(q, con, 'p1')
    p1.start()
    p2 = Producer(q, con, 'p2')
    p2.start()
    c1 = Consumer(q, con, 'c1')
    c1.start()
