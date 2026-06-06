#parameterized constructer
class Comp:
    #for default value variable (Same for every class)
    @staticmethod
    def greet():
        print("Hello") #Default constructer without self argument
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2
    def sum(self):
        sum=self.c1+self.c2
        print(f"Sum:{sum}i")
c1=Comp(3,2)
c1.greet()
c1.sum()
c2=Comp(1,2)
c1.sum()

#Overloading garidaina
