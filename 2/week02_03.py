# week02_03.py
# print()함수는 모든 타입의 데이터를 출력
# 출력 타입은 '문자열'

#sep 옵션은 교재/pdf에 없음.
print("I", "AM", "A", "BOY.")
print("I", "AM", "A", "BOY.", sep="")
print("I", "AM", "A", "BOY.", sep=";")
print("I", "AM", "A", "BOY.", sep="\n")
print("=" * 10)

print("I")
print("AM")
print("A")
print("BOY.")
print("=" * 10)

print("I", end=" ")
print("AM", end="\n")
print("A", end="--")
print("BOY.")
print("=" * 10)

print()
print(int(1))
print(str("1"))
print(float(1.1))
print(bool(True))
print([1,2,3])
print("123")
print("1" "2" "3")
print("1", "2", "3")
print("1" + "2" + "3")
