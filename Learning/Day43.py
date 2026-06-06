#Static method
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def student_info(self):
            print(f"Name:{self.name}\nAge:{self.age}\nGrade:{self.grade}")
a=Student("Pabitra",19,13)
a.student_info()
#Static method is a decorater
#decorator is fx which inputs a fx and outputs a fx
class Student:
    @staticmethod #So the fx become static self nachaini fx ma use garna milxa
    def student_info(self):
            print(f"Name:Pabitra")
a=Student()
print(a)

class MyClass:
    @staticmethod
    def my_static_method(param1, param2):
        return param1 + param2

# Example usage
print(MyClass.my_static_method(3, 5))  # Outputs: 8

obj = MyClass()
print(obj.my_static_method(4, 6))      # Outputs: 10
