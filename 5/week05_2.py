#week05_2.py
toeic=int(input("TOEIC:"))
age=int(input("AGE:"))
grade=int(input("GRADE:"))
temp=int(input("TEMPERATURE:"))
height=int(input("HEIGHT:"))
socnum=int(input("SOC NUMBER:"))

a=toeic >= 800 and age < 30 # toeic이 800 이상, age가 30보다 작을 때 실행
b=toeic >= 800 or age < 30 # toeic이 800 이상이거나, age가 30보다 작으면 실행
d=temp < 10 or temp > 28 # 온도가 10도보다 낮거나, 28도보다 높으면 실행

c = not (age==30) and toeic < 600 #age가 30이 아니고 toeic이 600보다 낮으면 실행0
# c = age != 30 and toeic < 600

e = height >= 120 and height <= 160 #키가 120 이상이거나 키가 160 이하일 때 실행
# e = 120 <= height <= 160 (중요함)

print(a,b,c,d,e)

cars = ["audi","tesla","전도헌","kia","정진호","hyundai"]
car= "KIA"
print(car in cars) #false
print(car not in cars) #true
print(car.lower() in cars) #true
print(car.lower() not in cars) #false
print("*" * 30)

