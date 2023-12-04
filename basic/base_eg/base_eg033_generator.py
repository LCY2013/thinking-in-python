# -*- coding: UTF-8 -*-

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # Forward iterator
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        # Reverse iterator
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)

# 同时迭代多个序列

# -*- coding: UTF-8 -*-

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
for name, age in zip(names, ages):
    print(name, age)

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]

dict1 = dict(zip(names, ages))

print(dict1)
