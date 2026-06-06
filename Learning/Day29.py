#Now i can use math function

import math
x=int(input("Enter a number:\n"))
x=math.sqrt(x)
print(f"The square root of input no is {x}")

#use can only use on function by from keyboard

from math import sin,pi
a=int(input("Enter a angle:\n"))
a=math.sin(a)*pi
print(a)

#Importing everything can be done by

from math import*
now=math.pow(1,33)
print(now)

#Importing as a certain keyboard

import math as m
x=sqrt(9)#m. not important
y=m.factorial(5)
print(x,y)

# from math import sqrt as s
# x=math.s(9)
# print(x)

print(dir(math))#Print all function of math

#i can import variables and function from other file
from Raw import func,lst
x=func()
print(x)
