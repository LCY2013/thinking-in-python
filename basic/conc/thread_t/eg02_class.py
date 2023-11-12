import threading


class MyThread(threading.Thread):
    def __init__(self, name, num):
        threading.Thread.__init__(self)  # 调用父类的构造函数,必须要写
        self.name = name
        self.num = num

    def run(self):
        print('Hello, %s, %s' % (self.name, self.num))


if __name__ == '__main__':
    t1 = MyThread('Thread-1', 1)
    t2 = MyThread('Thread-2', 2)

    t1.start()
    t2.start()

    # 加入主线程等待子线程结束
    t1.join()
    t2.join()
