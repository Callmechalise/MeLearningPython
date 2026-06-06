fruits=["Apple","Banana","Mango","Kiwi"]
# i=0
# for fruit in fruits:
#     print(fruit)
#     if(i==2):
#         print("Keraaa")
#     i+=1

#Etro haribijok kina garnu heraaa

for index,fruit in enumerate(fruits):
    print(fruit)
    if(index==1):
        print("Keraaa")

marks=[56,78,98,54,67,32,45]
for i,num in enumerate(marks,start=1):
    print(num)
    if(i==3):
        print("oh oh")
