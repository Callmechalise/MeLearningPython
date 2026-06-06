# Dictionary

dict1 = {
    "Person1": "GroupA",
    "Person2": "GroupB",
    "Person3": "GroupC",
    "Person4": "GroupD"
}

print(dict1["Person3"])

emp = {
    1: "Employee1",
    2: "Employee2",
    3: "Employee3",
    4: "Employee4",
    5: "Employee5"
}

# print(emp[5])      # Works
# print(emp[6])      # KeyError
# print(emp.get(5))  # Safe lookup
# print(emp.get(6))  # Returns None

# print(emp.keys())    # Show all keys
# print(emp.values())  # Show all values

print(emp.items())     # Show key-value pairs

for key, value in emp.items():
    print(f"The key is {key} and the value is {value}")

emp = {
    12: "EmployeeA",
    13: "EmployeeB",
    14: "EmployeeC",
    15: "EmployeeD"
}

emp.update({16: "EmployeeE"})

emp2 = {
    17: "EmployeeF",
    18: "EmployeeG"
}

emp.update(emp2)

print(emp)
print(emp.keys())
print(emp.items())
print(emp.values())

emp2.clear()  # Remove all elements
print(emp2)