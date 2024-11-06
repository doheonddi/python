# week11_02.py

import datetime

class Test:  # Test 클래스(자료형) 선언
    def __init__(self):  # init은 매개변수를 설정하는데 보통 self를 사용
        name = ""  # 지역변수, __init__ 종료 후 사라짐
        self.name = ""  # 멤버변수(인스턴스 변수)
        self.age = 20
        print(datetime.datetime.now())
        
t = Test()
# 1단계 : Test() 생성자 호출
# 2단계 : __new__() 메소드 호출 (인스턴스 생성)
# 3단계 : __init__() 메소드 호출 ( 인스턴스 초기화)
# 4단계 : 생성한 인스턴스 참조를 반환
print(t.name)  # 멤버변수를 출력

t2 = Test()
print(t2.name)

#t3 = t2 -> 생성자를 통해서만 instance가 만들어짐

t.name = "김인하"
t2.name = "박인하"

print(t.age, t2.age)


# 메모리의 위치
print(id(t))
print(id(t2))

print(type(t) == type(t2))  # True
print(t == t2)  # False
print(t.name == t2.name)  # False
print(t.age == t2.age)  # True
