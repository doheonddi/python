# week11_05.py

class In:
    def func(self):
        print("In.func()")


class Out:
    def method(self):
        print("Out.method")

# 안되면 주석.
# func()
# method()
# In.func()
# Out.method()

i = In()
o = Out()
# 정식
In.func(i)
Out.method(o)
# 약식 (실제로 쓰는)
i.func()
o.method()

# 되지만 정삭적인 상황이 아님
# 코드가 복잡해지면 문제가 발생함.
# In.func(o)
# Out.method(i)

# o.func()
# i.method()
