# week11_01.py

class Test:  # Test 클래스(자료형) 선언
    pass  # 빈 블록

t1 = Test()  # 생성자 Test를 호출
             # 메모리에 Test 타입의 데이터가 생성
             #          (Test의 instance)
             # 그 데이터를 t1이 참조하고 있음.

i1 = int(1)  # 생성자 int를 호출하면서
             # 메모리에 int 타이의 데이터(1)가 생성
             # 그 데이터를 i1이 참조하고 있음
             # 단, int는 기본 자료형(class)

print(type(t1))
print(type(i1))
