from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(processes=4) as pool:  # 进程池包含4个进程
        print(pool.map(f, range(10)))  # 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

        it = pool.imap(f, range(10))
        print(it)
        print(next(it))  # 输出 0
        print(next(it))  # 输出 1
        print(it.next(timeout=1))  # 输出 4
