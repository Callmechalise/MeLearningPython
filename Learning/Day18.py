#Doc string right below function
def cube(a):
    '''Takes input and give cube of that number
    '''
    a=a**3
    print(f"The output is:\n{a}")
input=int(input("Enter number:\n"))
cube(input)
#Docstring is not only comment
print(cube.__doc__)
#It can be used as stirng too
