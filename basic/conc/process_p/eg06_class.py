# multiprocessing.Process的run()方法
import os
import time
from multiprocessing import Process


class NewProcess(Process):  # 继承Process类创建一个新类
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self):  # 重写Process类中的run()方法
        while True:
            print(f'进程 {self.num} , pid是 {os.getpid()}')
            time.sleep(1)


if __name__ == '__main__':
    for i in range(2):
        p = NewProcess(i)
        p.start()

# 当不给Process指定target时，会默认调用Process类里的run()方法。
# 这和指定target效果是一样的，只是将函数封装进类之后便于理解和调用。
