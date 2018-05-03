import builtins
builtins.Z3_LIB_DIRS = ['D:\\Z3\\z3-4.6.0-x64-win\\bin']

from z3 import *

x1 = 1
y1 = 1
res1 = 2

x2 = 1
y2 = 3
res2 = 0

m = Int('m')
n = Int('n')
s = Solver()
s.add(m*x1 + n*y1 == res1, m +n <=3,m+n >= 0,m>=-1,n>=-1,m<=3,n<=3)
s.add(m*x2 + n*y2 == res2, m +n <=3,m+n >= 0,m>=-1,n>=-1,n<=3,n<=3)
# s.add(n==-1 and m==3)
# s.add((m == 1 and n == -1)
#       or (m == -1 and n == 1)
#       or (m == 2 and n == -1)
#       or (m == -1 and n == 2)
#       or (m == 1 and n == 2)
#       or (m == 2 and n == 1)
#       or (m == 3 and n == -1)
#       or (m == -1 and n == 3)
#       or (m == 1 and n == 1))
print(s.check())
print(s.model())
