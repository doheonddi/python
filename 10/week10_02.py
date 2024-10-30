# week10_03.py
f = open(r"c:\202444066\jeondoheon02.txt",'a')

scores={'math':90,'kor':100,'eng':10}

while True:
    scores['math']=int(input("math:"))
    scores['kor']=int(input("kor:"))
    scores['eng']=int(input("eng:"))

    data = ""
    for k, v in scores.items():
        if data:
            data += "|"
        data += f"{k},{v}"
    f.write(f"{data}\n")
    if "Y" == input("종료(Y):").upper():
        break
    

f.close()

'''
f = open(r"c:\202444066\jeonoheon01.txt",'w')

scores={'math':90,'kor':100,'eng':10}

for k, v in scores.items():
    f.write(f"{k},{v}\n")

f.close()
'''
'''
f = open(r"c:\202444066\jeonoheon01.txt",'a')

scores={'math':90,'kor':100,'eng':10}

while True:
    scores['math']=int(input("math:"))
    scores['kor']=int(input("kor:"))
    scores['eng']=int(input("eng:"))

    for k, v in scores.items():
        f.write(f"{k},{v}\n")
    if "Y" == input("종료(Y):").upper():
        break
    

f.close()
'''
