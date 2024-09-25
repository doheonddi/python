#week05_03.py
socnum = input("주민등록번호;")

if "-" in socnum:
    gender = int(socnum[7])%2 # 주민번호에 -가 있으면 7번째 요소

else:
    gender = int(socnum[6])%2 # 주민번호에 -가 없으면 6번째 요소 
"""else에 주석처리를 하면 int(socnum)이
실행되지 않아 gender 변수가 생성되지 않으므로nameerror가 뜬다"""
if gender == 0:
    msg = "여성"

else:
    msg = "남성"

print(f"성별 : {msg}")
  
a = "-" in socnum
b = "-" not in socnum

gender = int(socnum[7]) % 2

if gender == 0:
    msg = "여성"

if gender == 1:
    msg = "남성"

print(f"성별 : {msg}")
