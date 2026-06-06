class Bau:
    def __init__(self,eyei,tall):
        self.eye=eyei
        self.tall=tall
    def show(self):
        print(f"Eye:{self.eye}")

class xoro(Bau):
    def __init__(self,colour,eye):
        self.rang=colour
        self.eye=eye
    def printf(self):
        print(f"color:{self.rang}")

y=Bau("red",True)
x=xoro("khaire","Green")
x.printf()
x.show()
#DATA MEMBER inherit garna mildaina without super

