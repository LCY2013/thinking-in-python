# 事件：定义一个flag，当flag为True时，执行事件，否则不执行事件。set设置flag为True，wait等待flag为True，clear将flag设置为False。
import threading


def func(e, i):
    print(i)
    e.wait()  # 检测当前event是什么状态，如果是红灯，则阻塞等待，否则是绿灯则执行下面的语句，默认是红灯。
    print(i + 100)


event = threading.Event()
for i in range(10):
    t = threading.Thread(target=func, args=(event, i))
    t.start()

event.clear()  # 主动将event设置为红灯
inp = input(">>>")
if inp == "1":
    event.set()  # 主动将状态设置为绿灯
