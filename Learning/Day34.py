#Filter
def func(x):
    return x>=4

from Raw import tup
l=filter(func,tup)
print(list(l))
