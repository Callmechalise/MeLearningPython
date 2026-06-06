#Local and global variable
x=10
print(x)

def hello():
    x=5
    print(x)
    print(f"The local x is {x}")
hello()
print(f"The global x is {x}")
#I cant use local variable outside function
#For that
def hello():
    global x
    x=5

print(x)
