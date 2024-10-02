#week06_01.py
students=[]
titles=["국어", "영어", "수학"]

#students = [[10,20,30],[1,2,3]]
#students = [[10,1],[20,2],[30,3]]

number=int(input("인원 :"))

for n in range(number):
    print(f"{n+1} 학생>>")
    students.append([]) # [[]]
    for t in titles:
        score = float(input(f"{t} 과목: "))
        students[n].append(score)

for value in enumerate(students):
    print(value)
    print(value[0], value[1])

for v1, v2 in enumerate(students):
    print(v1, v2)

for v1, v2 in enumerate(students):
    print(f"{v1+1}:")
    for j, score in enumerate(v2):
        print(f"{titles[j]} : {score}")
