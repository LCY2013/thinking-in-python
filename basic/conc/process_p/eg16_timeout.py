from multiprocessing import Pool
import time


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(processes=4) as pool:  # 进程池包含4个进程
        result = pool.apply_async(f, (10,))  # 执行一个子进程
        print(result.get(timeout=1))  # 显示执行结果，给定超时时间

        result = pool.apply_async(time.sleep, (10,))
        print(result.get(timeout=1))  # 显示执行结果，给定超时时间, raise multiprocessing.TimeoutError
