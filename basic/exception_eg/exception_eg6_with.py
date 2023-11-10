file1 = open("1.txt", encoding='utf-8')
try:
    data = file1.read()
finally:
    file1.close()

# 语法糖等价于上面
with open('1.txt', encoding='utf-8') as f:
    data = f.read()
