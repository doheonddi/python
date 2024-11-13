# week12_04.py

'''
# week12_02모듈에서 add를 가져와 쓰겠어
from week12_02 import add
# week12_02모듈에서 sub를 가져와 쓰겠어
from week12_02 import sub
'''

'''
# 되도록이면 사용하지 말라고 많이 경고함.
from week12_02 import *
'''
from week12_02 import add, sub

print(add(3, 4))
print(sub(3, 4))
