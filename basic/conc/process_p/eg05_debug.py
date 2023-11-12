# 显示所涉及的各个进程ID，这是一个扩展示例

from multiprocessing import Process
import os
import multiprocessing


def debug_info(title):
    print('-' * 20)
    print(title)
    print('模块名称:', __name__)
    print('父进程:', os.getppid())
    print('当前进程:', os.getpid())
    print('-' * 20)


def f(name):
    debug_info('function f')
    # print('hello {}'.format(name))
    print(f'hello {name}')


if __name__ == '__main__':
    debug_info('main')
    p = Process(target=f, args=('world',))
    p.start()

    for p in multiprocessing.active_children():
        print('子进程名称:', p.name)
        print('子进程ID:', p.pid)
        print('子进程退出代码:', p.exitcode)
        print('子进程是否退出:', p.exitcode is None)
        print('子进程是否运行中:', p.is_alive())
        print('子进程是否停止:', p.is_alive() is False)
        print(f'CPU核心数量: {str(multiprocessing.cpu_count())}')

    p.join()
