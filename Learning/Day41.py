#Inheritance
class Employee:
    def __init__(self,Name,Gender):
        self.Name=Name
        self.Gender=Gender
    def info(self):
        print(f"Name: {self.Name}\nGender: {self.Gender}")

# a=Employee('Pabi','Male')
# a.info()

class Programmer(Employee):
    def Show_Language(slef):
        print("Python")

a=Programmer('Rama','Female')
a.Show_Language()
a.info()
