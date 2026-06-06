def function_print(a,b,c,d):
    print(a,b,c,d)
function_print(1,2,3,4)
#function_print(1,2,3,4,5) will give error hera
#scaling garda kando dekhaidyo

ar=[1,2,3,4,5]
def funargs(*args):
    print(args[0])
funargs(ar)
#wah ji wa maja aagaya

def ajhaifunargs(normal,*args):
    print(f"hey normal:{normal}")
    for items in args:
        print(f"hey args:{items}")
funargs("i am normal",ar)
#quargs for key value pair
def print_pet_names(**kwargs):
    for pet, name in kwargs.items():
        print(f"My {pet} is named {name}.")

print_pet_names(dog="Buddy", cat="Mittens", fish="Goldie")
