# week11_08.py

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

print(1)
print(1.1)
p1 = Point()
p2 = Point(1.0, 10.0)


class Rectangle:
    def __init__(self,x=0.0,y=0.0,w=0.0,h=0.0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Subject:
    def __init__(self, num, name, t=None, grade=None):
        self.number = num
        self.name = name
        self.teacher = t
        self.grade = grade

class Student:
    def __init__(self,name,number,dept,birthyear):
        self.name = name
        self.number = number
        self.dept = dept
        self.birthyear = birthyear

class Rectangle2:
    def __init__(self,sp=Point(),w=0.0,h=0.0):
        self.startpoint = Point()  # x:0, y:0
        self.w = w
        self.h = h
        self.startpoint = sp  # x:0, y:0

r = Rectangle2(Point(1,1),10,20)

class Rectangle3:
    def __init__(self, sp = Point(), ep = Point()):
        self.startpoint = sp
        self.endpoint = ep


