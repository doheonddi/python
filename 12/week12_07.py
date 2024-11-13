# week12_07.py

import week12_06 as model
from week12_06 import PI
from week12_06 import PI as pi  # 많이 씀

print(model.PI)
print(PI)
print(pi)

print(model.add(model.PI, 4.5))

m = model.Math()
print(m.solv(2))
