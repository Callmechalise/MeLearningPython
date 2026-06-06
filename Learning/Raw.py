import functools
import time

@functools.lru_cache(maxsize=None)
def fib(n):
    if n==0:
        time.sleep(10)
        return 0
    elif n==1:
        time.sleep(10)
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(25):
    print(f"{fib(i)}")
