from multiprocessing import Process, Queue
import os, time


def write(q):
    print("启动Write子进程：%s" % os.getpid())
    for i in ['A', 'B', 'C', 'D', 'E']:
        q.put(i)  # 写入队列
        time.sleep(1)
    print("结束Write子进程：%s" % os.getpid())


def read(q):
    print("启动Read子进程：%s" % os.getpid())
    while True:
        data = q.get(True)  # 阻塞，等待获取write到队列的值并从队列中读取
        print("Read子进程：%s，读取到数据：%s" % (os.getpid(), data))
        time.sleep(1)
    print("结束Read子进程：%s" % os.getpid())


if __name__ == '__main__':
    # 父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    pw.join()
    # pr进程是一个死循环，无法等待其结束，只能强行结束
    # （写进程结束了，所以读进程也就可以结束了）
    pr.terminate()
    print('父进程结束')

# 启动Write子进程：90146
# 启动Read子进程：90147
# Read子进程：90147，读取到数据：A
# Read子进程：90147，读取到数据：B
# Read子进程：90147，读取到数据：C
# Read子进程：90147，读取到数据：D
# Read子进程：90147，读取到数据：E
# 结束Write子进程：90146
# 父进程结束
