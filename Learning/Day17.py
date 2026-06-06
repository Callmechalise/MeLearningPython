#Fstrings

#Normal string formatting
# letter="Hey my name is pabitra kumar {} and i am from {}"
# country="Nepal"
# surname="Chalise"
# x=letter.format(surname,country)
# print(x)
# letter="Hey my name is pabitra kumar {0} and i am from {1}"
# x=letter.format(surname,country)
# print(x)

#Fstrings
surname=input("Enter surname:\n")
country=input("Enter country name:\n")
print(f"""Hey my name is pabitra kumar{surname}  and i am from {country} """)
price=473454.45475
print(f"{price:.2f}")
print(f"{2.60*44.67}")

#For as it is display:
print(f"""Hey my name is pabitra kumar{{surname}}  and i am from {{country}} """)
