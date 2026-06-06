#Constructer
class Car:
    name=""
    color=""
    def __init__(self):
        print("Enter name:")
        self.name=input()
        self.color=input("Enter section:")
    def display(self):
        print(f"Name:{self.name}")
        print(f"color:{self.color}")
c1=Car()
c1.display()