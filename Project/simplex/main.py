from z3 import *

x=Int('x')
y=Int('y')
z=Int('z')

s = Solver()

s.add(z==-3*x+7*y)
s.add(2*x+3*y<=5)
s.add(5*x+2*y>=5)
s.add(y<=1)
s.add(x>0,y>0)

if s.check()==sat:
    print(s.model())
else:
    print("no optimal solution found")