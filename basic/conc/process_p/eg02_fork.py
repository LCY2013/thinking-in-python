# 区分父子进程
import os
import time

res = os.fork()
print(f'res == {res}')

if res == 0:
    print(f'子进程, pid是：{os.getpid()} 父进程id是：{os.getppid()}')
else:
    print(f'父进程，pid是：{os.getpid()}')
