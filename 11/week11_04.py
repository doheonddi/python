#  week11_04.py

class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0

students=[]
for i in range(3):
    print("[" + str(i + 1) + "] 입력")
    s = Student()
    s.name=input("이름 :")
    s.number=input("학번 :")
    s.dept=input("학과 :")
    s.birthyear=int(input("생년 :"))

    students.append(s)

for i in students:  # type(i) == Student
    print(i.name)

# (1)
# 동일한 학번이 들어왔을 때는 어떻게 할지?

# (2)
# students를 dict로 만들어서 실행해볼 것
#d dict의 key는 학번이 합당 할 거승로 보임

# (3)
# while문으로 바꿔서 본인이 원하는 만큼만
'''        
s1 = Student()
s1.name=input("이름 :")
s1.number=input("학번 :")
s1.dept=input("학과 :")
s1.birthyear=int(input("생년 :"))

s2 = Student()
s2.name=input("이름 :")
s2.number=input("학번 :")
s2.dept=input("학과 :")
s2.birthyear=int(input("생년 :"))

s3 = Student()
s3.name=input("이름 :")
s3.number=input("학번 :")
s3.dept=input("학과 :")
s3.birthyear=int(input("생년 :"))
print(s1.name)
print(s2.name)
print(s3.name)
'''
