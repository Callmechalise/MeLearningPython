#Introducing methods
class Human:
    Name = "Ram"
    Occupation = "Fankiini"
    Age = 16
    Race='White'
    Gender='Female'
    Nerworth=10000000
    def info(self):
        print(f"Name: {self.Name}")

a=Human()
a.info()
#name ferdim
a.Name='Pabitra'
a.info()
#self is tyo object jasko lagi method call hudai xa
#eg
b=Human()
b.Name='Ramkrishna'
b.info()