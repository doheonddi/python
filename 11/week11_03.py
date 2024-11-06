# week11_03.py

class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Rectangle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.w = 0.0
        self.h = 0.0

class Subject:
    def __init__(self):
        self.number = ""
        self.name = ""
        self.teacher = ""
        self.grade = 0.0

class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0

class Rectangle2:
    def __init__(self):
        self.startpoint = Point()  # x:0, y:0
        self.w = 0.0
        self.h = 0.0

class Rectangle3:
    def __init__(self):
        self.startpoint = Point()
        self.endpoint = Point()


r2 = Rectangle2()
r3 = Rectangle3()

r2.w=10
r2.h=20
print(r2.startpoint.x + r2.w)

r3.endpoint.x = 10
r3.endpoint.y = 20

print(r3.endpoint.x)
