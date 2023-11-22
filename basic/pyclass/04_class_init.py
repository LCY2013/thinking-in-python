# GOD
class Human(object):

    # 使用__init__接收参数，思考不定参数处理
    def __init__(self, name):
        # self表示对象本身，约定俗成
        self.name = name


man = Human('Adam')
human = Human('Eve')

# 对实例属性做修改
man.name = 'python'
man.name
human.name
