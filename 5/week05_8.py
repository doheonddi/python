#week05_08.py
'''
for(int i=0; i<10;i++)
{
    print("%d",i);
}

for i in [0,1,2,3,4,5,6,7,8,9,]:
    print(i,end=" ")
'''

for i in range(10): #rnage(0,10,1)위에 주석 처리 한 코드랑 같음
    print(i,end=" ")

for i in range(1,10): #rnage(1,10,1)1부터 시작
    print(i,end=" ")

for i in range(1,10,2): #2씩 증가
    print(i,end=" ")

for i in range(10,1,-2): #10부터 1까지 2씩 감소
    print(i,end=" ")

a=range(10) #range 타입을 만듦. 리스트를 만드는게 아님. for문 돌릴 때만 씀
print(a) 
b=list(a) # range 타입을 리스트로 만들고 싶으면 list 쓰면 됨.
print(b) 
