#week05_05.py
scores=[]

while True:
    score = input("점수:")
    if not score.strip(): # 문자가 하나도 없을 때 break
        break
    scores.append(float(score)) 

if 0 < len(scores):
    number = 0
    summary = 0
    for score in scores:
        number += 1
        summary +=score
        print(f"{number} 점수 : {score}")
    print(f"총 평균:{summary/len(scores)}")
else:
    print("점수가 없어요!")
