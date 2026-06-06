#Recurssion

#Factorial
#factorial(n)=n*factorial(n-1)

def factiorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factiorial(n-1)
x=int(input("enter a number:\n"))
print(f"{factiorial(x)}")


    