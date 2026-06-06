#Access Modifiers
# Public,Private,Protected

#Public:
class student:
    def  __init__(self):
        self.Name='Pabiii'
    def real_name(self):
        return "Pabitra"
a=student()
print(a.real_name())
print(a.Name) #Accessing Public Variable

#Private
class student:
    def  __init__(self):
        self.__Name='Pabiii'
a=student()
print(a._student__Name)

#Protected
class Student:
    def __init__(self):  # Fixed the typo here
        self._name = 'Ram'
    
    def _funname(self):
        return "Ram is cool"

class Subject(Student):
    pass

obj = Student()
obj2 = Subject()

print(obj._name)          # Accessing the protected variable
print(obj._funname())    # Calling the protected method

# Accessing the protected member from the subclass
print(obj2._name)        # Accessing protected variable from subclass (not recommended)
print(obj2._funname())   # Calling the protected method from subclass
