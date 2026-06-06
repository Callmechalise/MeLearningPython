import functools
import time
#value memoize garxa 5 halda kati aathyo
#Tyo yaad garxa ani feri tei value sanga call garda
#ans fatafat return garxa very important for python
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*n
print(fx(5))
print("Done for 5")
print(fx(55))
print("Done for 55")
print(fx(5))
print("Done for 5")
print(fx(5))
print("Done for 5")

# @functools.lru_cache(maxsize=None)
# def fib(n):
#     if n==0:
#         time.sleep(3)
#         return 0
#     elif n==1:
#         time.sleep(3)
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(5):
#     print(f"{fib(i)}")
