a=input("Input numbers seperate with comma:\n")
x=a.split(",")
print(f"\n Your list is\n{x}")
b=input("Press a for ascending order and d for descending:\n")
if b=="a":
    x.sort()
    print(x)
elif b=="d":
    x.sort(reverse=True)
    print(x)
else:
    print("Heh")