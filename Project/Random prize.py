from random import randint
Teams=["Mancity","Realmadrid","AC Milan","Bayen","Barcelona","Liverpool"]
x=randint(1,len(Teams))#refrence mancity do not win troffee
print(x)
Teams=Teams[x]
print(f"{Teams} won the troffee")
