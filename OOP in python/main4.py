class Human:
    species="Homosapiens"
    def __init__(self,namei,heighti,colori):
        self.name=namei
        self.height=heighti
        self.color=colori
    def display(self):
        print(f"Your name:{self.name}")
        print(f"Your Height:{self.height}")
        print(f"Your Color:{self.color}")
        print(f"Your species:{self.species}")

h1=Human("Ram",5.5,"brown")
h1.display()