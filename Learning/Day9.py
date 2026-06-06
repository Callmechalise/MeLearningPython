#Matchcase
x=int(input("A number?"))
match x:
 case 0:
  print("Number is zero")
 case _ if x==100:
  print("is hundred")
 case _:
  print(x)
