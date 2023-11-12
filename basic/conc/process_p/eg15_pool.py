# Pool 类表示一个工作进程池
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing.pool import Pool
from time import sleep, time
import random
import os


def func(name):
    print(f'{name}-子进程开始，进程ID: {os.getpid()}')
    start = time()
    sleep(random.choice([1, 2, 3, 4]))
    end = time()
    print(f'{name}-子进程结束，进程ID：{os.getpid()}, 耗时%0.2f：{end - start}')


if __name__ == '__main__':
    print('父进程开始')
    # 创建多个进程，表示可以同时执行的进程数量。默认大小是CPU的核心数
    p = Pool(4)
    for i in range(10):
        # 创建进程，放进进程池统一管理
        p.apply_async(func, args=(f'任务{i}',))
    # 如果我们使用的是进程池，在调用join()前必须先close()
    # 并且在close()之后不拿再继续往进程池添加新的进程
    p.close()
    # 进程池对象调用join，会等待进程池中所有的子进程结束完毕在去结束父进程
    p.join()
    print('父进程结束')
    p.terminate()

# close()：如果我们用的是进程池，在调用join()之前必须要先close()，
# 并且在close()之后不能再继续往进程池添加新的进程
# join()：进程池对象调用join，会等待进程池中所有的子进程结束完毕再去结束父进程
# terminate()：一旦运行到此步，不管任务是否完成，立即终止。
