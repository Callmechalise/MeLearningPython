# Decorators
# ===========

def greet(fx):
    def mfx():
        print('Good morning')
        fx()
        print('Have a good day,Thanks for using this fx')
    return mfx
@greet
def sum():
    print('Hello world')
sum()
#*args=Tuple
#**args=Dictionary

