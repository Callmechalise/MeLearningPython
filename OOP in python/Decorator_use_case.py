def say_hello_decorator(func):
    def wrapper():
        print("Hello!")
        func()
    return wrapper

@say_hello_decorator
def my_function():
    print("I am running")

my_function()
