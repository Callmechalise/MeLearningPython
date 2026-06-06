#Finally
try:
    lst=[1,2,4,65,7,89,9]
    i=input("Enter index of object?\n")
    print(lst[i])
except:
    print("Error aayo")

    print("Aba ma print hunxu")
#While we are inside function without finally the normal print statement wont work
def func1():
    try:
        lst=[1,2,4,65,7,89,9]
        i=input("Enter index of object?\n")
        print(lst[i])
        return 1
    except:
        print("Error aayo")
        return 0
    finally:
        print("Aba ma print hunxu")
x=func1()
print(x)
