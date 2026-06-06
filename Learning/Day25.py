
while True:
    inp=input("Enter value between 1 and 9,9 and 1 are not included\n")
    
    if inp.lower()=='quit':
        print("Ok exitting the programme,Bye user")
        break
    try:
        inp=int(inp)
        if(inp<=1 or inp>=9):
            raise ValueError("euta kam garni dhanga hos na,Thukka")
    except ValueError as e:
        print(e)



