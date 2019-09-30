# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义构造方法

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def speak(self):
        print(self.name, " 说: 我", self.age, "岁。")


# 实例化类
p = people('runoob', 10)
p.speak()
