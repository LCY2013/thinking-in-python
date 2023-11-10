def chain(num):
    for i in range(num):
        yield i


number = 10
y = chain(number)
print(next(y))
print(list(y))
# next(y) StopIteration
