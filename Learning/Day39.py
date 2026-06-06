#Constructer
class Human:
    def __init__(self):
        print('HEllo World')

    def info(self):
        pass
a=Human()#init function CALL HUNXA HUNXA


class Human:
    def __init__(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation

    def info(self):
        print(f"His name is {self.name}.He is {self.age} years old and.He is a {self.occupation}")
a=Human('Pabitra','19','Engennier')
a.info()