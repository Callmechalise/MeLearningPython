class Students:
    Collage="ABC"
    def __init__(self,namei,marks):
        self.name=namei
        self.marks=marks
    def display(self):
        print(f"Your name:{self.name}")
        avg=0
        counter=0
        for val in self.marks:
            avg=avg+val
            counter=counter+1
        print(f"Your Average marks is :{avg/counter}")

h1=Students("Ram", [20, 50, 60])
h1.display()