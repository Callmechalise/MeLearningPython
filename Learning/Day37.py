# Class and Object

class Human:
    name = "Person"
    occupation = "Student"
    age = 20
    race = "Human"
    gender = "Unknown"
    net_worth = 1000000


a = Human()

print(f"Name: {a.name}, Age: {a.age}, Gender: {a.gender}")

# Change the name for this object
a.name = "Alex"

print(f"Name: {a.name}, Age: {a.age}, Gender: {a.gender}")

# Change the occupation for this object
a.occupation = "Software Developer"

print(f"Name: {a.name}, Age: {a.age}, Occupation: {a.occupation}")