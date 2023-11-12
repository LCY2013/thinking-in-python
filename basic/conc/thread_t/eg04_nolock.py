import threading
import time

num = 0


def addOne():
    global num
    num += 1
    time.sleep(1)  # 必须休眠，否则观察不到脏数据
    print(f'num value is {num}')


for i in range(10):
    t = threading.Thread(target=addOne)
    t.start()

print('main thread end')

# main thread end
# num value is 10
# num value is 10
# num value is 10
# num value is 10
# num value is 10
# num value is 10
# num value is 10
# num value is 10
# num value is 10
# num value is 10
