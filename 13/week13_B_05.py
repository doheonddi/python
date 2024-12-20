# week13_B_05.py
# id : 202444066
# name : jeon doheon
from datetime import datetime as dt

dtformat = "%Y-%m-%d %H:%M:%S"
    
cars=[]
while True:
        number = input("차량번호: ").strip()
        if not number:
            break
    while True:
        try:
            intime = input("입차시간: ").strip()
            if intime:
                intime = dt.strptime(intime, dtformat)
                break
        except:
            pass
    while True:
        try:
            outtime = input("출차시간: ").strip()
            if not outtime:
                outtime = None
                break
            outtime = dt.strptime(outtime, dtformat)
        except:
            pass        
        
        cardata = {'num':number, 'in':intime, 'out':outtime}
        cars.append(cardata)

for car in cars:
    print(car['num'], car['in'], car['out'])
