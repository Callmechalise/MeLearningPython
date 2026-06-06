class student:
    def __init__(self,Name,Age,roll_no,Gender):
        self.Name=Name
        self.Age=Age
        self.roll_no=roll_no
        self.Gender=Gender
    def info(self):
        print(f'Name of student is {self.Name} and {self.Gender} is {self.Age} years old and roll no is {self.roll_no}')

x=input('Enter Name of student:\n')
y=input('Enter Gender of student (he/she):\n')
z=int(input('Enter age of student:\n'))
za=int(input('Enter roll no of student;\n'))
a=student(x,z,za,y)
a.info()