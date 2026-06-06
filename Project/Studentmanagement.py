class Student:
    def __init__(self, name, age, grade,  Student_id):
        self.name=name
        self.age=age
        self.grade=grade
        self.Student_id=Student_id
    def Student_info(self):
        print(f'Student name : {self.name},Student Age : {self.age},Student Grade : {self.grade} Student id:')

class College:
    def  __init__(self):
        self.students=[]
    def Add_student(self,student):
        self.students.append(student)
    def Show_students():
        if not self.students:
            print("No students in college")
        for student in self.students:
            print(Student,'\n',student.info())

def main():
    print('--**College Database**--')
    college=College()
    while True:
        print('1.Add students')
        print('1.Show students')
        Todo:Complete_project#we can add to do is python yk that??