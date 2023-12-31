# 条件锁：该机制会使线程等待，只有满足某个条件，才能释放n个线程
import threading


def condition():
    ret = False
    r = input(">>>")
    if r == "yes":
        ret = True
    return ret


def func(conn, i):
    # print(i)
    conn.acquire()
    conn.wait_for(condition)  # 该方法接受一个函数的返回值
    print(i + 100)
    conn.release()


c = threading.Condition()
for i in range(10):
    t = threading.Thread(target=func, args=(c, i,))
    t.start()

# 条件锁的原理跟设计模式中的生产者/消费者 (Producer/Consumer)模式类似
