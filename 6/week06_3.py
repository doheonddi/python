# week06_03.py
myInfo = {}

myInfo["n"]="김인하"
myInfo["a"]=23
myInfo["h"]=163.2
print(myInfo)

myInfo["h"]=173.2
print(myInfo)

del myInfo["h"]
print(myInfo)

# print(f"나의 키는 {myInfo['h']}cm 입니다.")# KeyError (인덱스가 아니므로 인덱스에러 x)

if 'h' in myInfo:
    print(f"나의 키는 {myInfo['h']}cm 입니다.")
else:
    print("키 자료 없음")

print(f"키{myInfo.get('h')}cm 입니다.")

if myInfo.get('h'):
    print(f"키:{myInfo['h']}cm")
else:
    print("키 자료 없음")
    
h=myInfo.get('h')
if h:
    print(f"키:{h}cm")
else:
    print("키 자료 없음")    

print(f"키{myInfo.get('h','--')}cm 입니다.")

myInfo.clear()
print(myInfo)
