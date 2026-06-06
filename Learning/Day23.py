#Try exept
# Prompt the user to enter a number
try:
    a = int(input("Enter a number\n"))  # Attempt to convert the input to an integer
    print(f"Multiplication table of {a} is :\n")
    
    # Loop through numbers from 1 to 10 and print the multiplication table
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")
        
except ValueError:
    # Handle the case where the input is not an integer
    print("Muji euta kam dhanga le garna aaunna talai hai")

except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")

print("!Thanks for executing the code")
#There are index error,value error,Key error and much more
