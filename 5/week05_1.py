#week05_1.py
class Test:
    def __init__(self):
        self.a=1
        self.b=2

test1=[1,2] #list
test2=(1,2) #tuple
test3=Test() #user-defined type(Test)

print(test1[0])
print(test2[0])
print(test3.a)

print(test1[1])
print(test2[1])
print(test3.b)

test1[0]=3
test2[0]=3 #오류 -> 튜플. 값 변경 불가
test3.a=3
print(test1[0])
print(test2[0])
print(test3.a)
