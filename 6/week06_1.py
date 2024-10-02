#week06_01.py
values = [1,2,3,4,5,6,7]

values_1 = [] ## 비어있는 리스트 준비
values_2 = []
for v in values :
    v_3 = v * 3 ## 중복된 연산을 줄여서 씀
    values_1.append(v_3)
    if v_3%2==0:
        values_2.append(v_3)

print(values_1)
print(values_2)

values_3 = [v*3 for v in values] ## vlaues에서 v를 뽑아 3배
values_4 = [v * 3 for v in values if v * 3 % 2 == 0]
print(values_3)
print(values_4)

values=['1','2','3']
#위 values의 데이터를 모두 정수로 변환한 새로운 리스트를 만들어보세요.(리스트 내포 이용.)
values_5=[v for v in values] ## values에 있는 v를 새로운 v로
values_5=[int(v) for v in values] ## 최종. 정수 v

print(values)
print(values_5)

mx = int(input("최대수 :"))
#최대수를 받아서 1~mx 까지의 숫자를 리스트로 만들어보세요.(리스트 내포 이용.)
#[B` for B in A(seq)]
values_6=[v for v in range(1,mx+1)] ## mx까지의 숫자를 뽑고싶을떄는 mx+1
print(values_6)
