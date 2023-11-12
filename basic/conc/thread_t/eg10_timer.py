# 定时器： 指定一个时间，在指定时间后执行某段代码
from threading import Timer


def hello():
    print("hello world")


t = Timer(1, hello)  # 表示1秒后执行hello()
t.start()
