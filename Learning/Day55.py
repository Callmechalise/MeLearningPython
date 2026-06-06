#multi threading YO CHAI BETTER THAN ASYNC IO ANI REALLY MY PROCESSOR LAI CONTROL GARDAI KAM GARXA
import threading
import time

def func(sec):
    time.sleep(sec)
    print("Lu sutdih 0")
def func1(sec):
    time.sleep(sec)
    print("Lu sutdih 2")
def func2(sec):
    time.sleep(sec)
    print("Lu sutdih 1")

t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func1,args=[2])
t3=threading.Thread(target=func2,args=[1])

t1.start()
t2.start()
t3.start()
#if i wanna print something after this it will print that before function runs
print("Ram")
#Tara i can exclude that by
t1.join()
t2.join()
t3.join()
print("Khub garis")