#decorator
def greet(fx):
    def greeting():
        print("Gukhaaaa...")
        fx()
        print("thanks for using this function")
    return greeting
        
@greet
def hey():
    print("Hey user")
