# 推导式
d = {i: f'{i}-{i}' for i in range(10)}
print(d)

d = {value: key for (key, value) in d.items()}
print(d)
