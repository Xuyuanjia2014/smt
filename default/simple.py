import builtins
builtins.Z3_LIB_DIRS = ['E:\\ProgrammingTools\\z3-4.6.0-x64-win\\bin']
from z3 import *

x = Real('x')
y = Real('y')
z = Real('z')
s = Solver()
s.add(x + y > 5, x > 1, y > 1)
s.add(x*x+y*y+z*z < 100, z*z>100)
print(s.check())
print(s.model())
