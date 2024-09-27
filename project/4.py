a=int(input("인원 :"))
b=int(input("피자 수량(판) :"))
c=int(input("피자 조각 (판당) :"))

d=b*c #총 조각

e=d//a #인당 조각
f=d%a #남은 조각

print(f"결과 : 인당{e}조각, 남은 조각{f}조각")
