#  week10_03.py

f=open(r"c:\202444066\jeondoheon02.txt",'r')

#readlines() -> 리스
lines = f.readlines()
#print(lines)
for line in lines:
    print(line.strip())


#readline()
#while True:
#    line = f.readline()
#    if not line:
#       break
#    print(line.strip())

#read()
#data=f.read()
#print(data)

f.close()
