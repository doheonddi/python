import math # 파이 쓰기 위함

a=int(input("도형 선택(1: 사각, 2: 삼각, 3:원): "))

if(a==1): #사각
    b=int(input("가로 입력 :"))
    c=int(input("세로 입력 :"))
    print(f"도형의 넓이 :{b*c}")
    
elif(a==2): #삼각
    d=int(input("밑변 입력 :"))
    e=int(input("높이 입력 :"))
    print(f"도형의 넓이 :{(d*e)/2:.2f}")
    
elif(a==3): #원
    g=int(input("반지름  입력 :"))
    h=(math.pi)*(g**2)
    print(f"도형의 넓이 :{h:.2f}")    
else: #잘못한입력
    print("잘못한 입력")
