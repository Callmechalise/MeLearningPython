A=input("Enter first no A:\n")
B=input("Enter second no B\n")
print("What is operation you want to perform?\n")
x={"1 for addition,2 for substraction,3 for multiplication,4 for division"}
print(x)
y=input("==>")
c=int(y)
if(c==1):
    print(int(A)+int(B))
elif(c==2):
    print(int(A)-int(B))
elif(c==3):
    print(int(A)*int(B))
elif(c==4):
    print(int(A)/int(B))
else:
    print("oops error")
         
