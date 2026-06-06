# dir, __dict__ and help method in Python 
x=[1,2,3,4]
print(dir(x))#Shows method attributes and all
print(x.__len__)#Tell about len

class person:
    def __init__(self,name):
        self.name=name
p=person("Pabitra")
print(person.__dict__)#Shows all attributes of class
print(p.__dict__)#Shows all slef.--- vars

print(help(person))#Class ma k  kasri garni bujxauxa