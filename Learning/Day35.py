#Reduce 
from functools import reduce
from Raw import tup
sum=reduce(lambda x,y:x+y,tup)
print(sum)

lst=[0,1,2,3,4,5,6,7,8,9]
l2=reduce(lambda x,y:x+y,lst)
print(l2)

