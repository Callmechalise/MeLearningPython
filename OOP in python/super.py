class Bau:
    def __init__(self):
        self.eye=input("Enter eye color")
        self.tall=input("Enter tall or not")
    def show(self):
        print(f"Eye:{self.eye}")

class xoro(Bau):
    def __init__(self,colour,eye):
        self.rang=colour
        self.eye=eye
    def printf(self):
        print(f"color:{self.rang}")
        super.__init__(self)
y=Bau()
x=xoro("khaire","red")
x.printf()