a=float(input("1학기 학점 :"))
b=float(input("2학기 학점 :"))
c=int(input("봉사시간 :"))

avg=(a*b)/2

if(avg>=3.5 and c>=8): 
    print("장학금 대상 여부 : 확정")
else:
    print("장학금 대상 여부 : 탈락")
