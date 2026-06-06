#function arguments
def average(a,b):
    x=(a+b)/2
    return x
print(average(5,3))

def average(a=5,b=3):
    x=(a+b)/2
    return x
print(average())

def average(a=6,b=4):
    x=(a+b)/2
    return x
print(average(5,3))

def average(a=6,b=4):
    x=(a+b)/2
    return x
print(average(5))

def average(a=6,b=4):
    x=(a+b)/2
    return x
print(average(b=3))

def name(fname, mname="MiddleName", lname="LastName"):
    print("Hi", fname, mname, lname)
name("FirstName")
name("FirstName", "MiddleName", "LastName")