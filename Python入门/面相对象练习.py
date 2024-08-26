# 设计类
class Student:
    name = None   #学生名字
    gender = None #学生性别
    age = None    #学生年龄

stu_1=Student()
stu_1.name = '许宗广'
stu_1.age = 18
stu_1.gender = '男'
stu_2=Student()
stu_2.name = '尚宁宁'
stu_2.age = 19
stu_2.gender = '女'
print(f'我叫：{stu_1.name}')
print(f'今年：{stu_1.age}')
print(f'性别是：{stu_1.gender}')
print(f'我叫：{stu_2.name}')
print(f'今年：{stu_2.age}')
print(f'性别是：{stu_2.gender}')
