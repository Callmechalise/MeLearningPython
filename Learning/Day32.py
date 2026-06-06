"""lambda function"""
# def double(x):
#     return x*2
# print(double(5))

double=lambda x: x*2
print(double(10))

import math
cube=lambda x: math.pow(x,3)
print(cube(3))

avg = lambda x,y,z: (x+y+z)/3
print(avg(1,2,3))