#Sets
# s={2,4,3,4,5,6,3,4,5,7}#No repetation while printing
# print(s)
# #There is no order gurantee in sets
# # accessing value on sets
# for value in s:
#     print(value) 
# #For empty set
# s=set()

#set methods aba
# s1={1,5,6,7,2,43,5,6,8}
# s2={1,4,5,687,43,5,6,7,2,5,8}
# s2.add(1)#Add element in set
# x=s1.union(s2)
# print(x)#union fo sets
# y=s1.update(s2)#s1 include value of s2 which is not in s1
# print(y)
# z=s1.symmetric_difference(s2)
# s1.intersection(s2)
# s1.intersection_update(s2)
# s1.symmetric_difference(s2)
# s1.difference(s2)
# s1.difference_update(s2)


# a=s1.isdisjoint(s2)#relation xa ki nai herxA
# print(a)
# b=s1.issuperset(s2)
# print(b)
# c=s1.issubset(s2)
# print(c)

s={"pabi","Hari","Annu","Puku"}
s.remove("pabi")#s ma pabi rainxa vaney error dinxa discard le dinna
s.discard("Ramey")
print(s)
s.pop()#Random value jhikdinxa
s.clear()#clear all items
del s #Delete set
