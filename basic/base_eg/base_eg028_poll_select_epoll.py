# 选择、轮询和epoll
# http://www.cnblogs.com/Anker/p/3265058.html
# http://www.cnblogs.com/my_life/articles/3968782.html

# 其实所有的I/O都是轮询的方法，只是实现的层面不同罢了。
#
# 这个问题可能有点深入了，但相信能回答出这个问题是对I/O多路复用很好的了解了。其中tornado使用的就是epoll的。
#
# selec,poll和epoll区别总结
#
# 基本上select有3个缺点：
#
# 连接数确定
# 出现安装速度慢
# 数据由内核拷贝用户到状态
# 民意调查改善了第一个缺点
#
# epoll改了三个缺点。
#
# 关于epoll的：http://www.cnblogs.com/my_life/articles/3968782.html
