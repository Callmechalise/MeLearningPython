#Tuple
#Change garna mildaina
# tup=("Ram","Shyam","hari","Geeta",3,2,1,4,6,5,7,8,0,9)
# print(type(tup))
# x=(1)#Is a string
# x=(1,)#is a tuple
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[-1])
# print(tup[len(tup)-1])#Same mathiko but +ve indexing

# if 6 in tup:#Same as list
#     print("xa")
# else:
#     print("xaina")
# tup1=tup
# tup1=tup[0:4]
# print(tup)#original print garxa i.e cant be change
# print(tup1)

#operations or methods in tuple

#Conversion of tuple to list
# countries=("Nepal","Japan","England","USA","UAE","Korea")
# countries2=list(countries)
# countries2.pop()#Last element gone
# print(countries2)
# countries2.pop(1)#element of index1 gone
# print(countries2)
# countries2[2]="finland"
# print(countries2)

tuple1=(1,2,4,3,7,6,8,9,0,2,1,3,4,5)
x=tuple1.count(3)#Count no of values
print(x)
x=tuple1.index(6)
print(x)#Give value in certain index
