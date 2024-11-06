# week11_06.py

class Test:
    def __init__(self):
        self.name = "메롱"
        self.age = 1000
    def func(self, name, age):
        self.name = name
        print(age)

t = Test()
print(t.name)
print(t.age)

t = Test()
t.func("김인하", 20)
print(t.name)
print(t.age)
