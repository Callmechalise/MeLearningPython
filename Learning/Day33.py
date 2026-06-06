#Map
import math
def cube(x):
    return math.pow(x,3)

print(cube(2))
#Normal method

l=[1,3,4,2,5,6,98,54,323,122]
# l2=[]
# for i in l:
#     l2.append(cube(i))
# print(l2)

#Using map
l2=list(map(cube,l))#Map object return garxa teslai list banaunu jaruri xa
print(l2)
doubled_list=list(map(lambda x:x*2,l))
print(doubled_list)