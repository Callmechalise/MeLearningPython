#lists
l=[1,2,3,4,5,6,7]
# print(l)
# print(type(l))
# print(l[0])
l=[4,5,6,"A","b"]
colors=["red","green","Blue"]
# print(colors)
#print(colors[:])
#print(colors[1:])
#print(l[::2])#Jump hanxa 2 4 6 esari
# print(colors[-1])#negative indexing
# print(colors[-2])
# print(colors[-3])
# print(colors[len(colors)-2])#positive indexing(Convert to +ve)

# if 7 in colors:
#     print("7 xa")
# else:
#     print("Xaina")
# if "red" in colors:
#     print("xaa")
# else:
#     print("xaina")
# if "ed" in colors[0]:
#     print("xa")
# else:
#     print("xaina")
lst=[i for i in range(10)]
print(lst)
print(lst[1:])
lst=[i*i for i in range(10)]
print(lst)
print(lst[1:])
lst=[i for i in range(10) if i%2==0]
print(lst)
print(lst[1:])