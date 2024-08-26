# 设计类
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def content(self):
        print(f'我的名字是：{self.name}，年龄是：{self.age}，考了{self.score}分')

# 创建对象

stu_1 = Student('许宗广',18,99)
stu_1.content()