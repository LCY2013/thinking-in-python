# http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
# http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/1/README.html

#  问： 将列表生成式中[]改成() 之后数据结构是否改变？ 答案：是，从列表变为生成器
L = [x*x for x in range(10)]
print(L)

g = (x*x for x in range(10))
print(g)

# 通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。
# 因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator
