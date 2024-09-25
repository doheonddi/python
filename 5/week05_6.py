#week05_06.py

while True:
    name = input("이름:").strip().lower()
    if name == "jeon":
        break
    elif name == "전":
        continue
    else:
        print(name)

"""
active = True
while active:
    name = input("이름:").strip().lower()
    if name == "jeon":
        active = False
    else:
        print(name)
"""
    
"""
name=""
while name.strip().lower() != "jeon":
    name = input("이름:")
    print(name)
"""


"""
name=""
while name != "전도헌":
    name = input("이름:")
    print(name)
"""
