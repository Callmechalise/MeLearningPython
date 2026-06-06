import time
Presenttime=time.strftime('%H:%M:%S')
print("Now time is \n",Presenttime)
Hour=int(time.strftime('%H'))
#min=time.strftime('%M')
#sec=time.strftime('%S')
if(Hour>6 and Hour<=12):
    print("Good morning")
elif(Hour>12 and Hour<=17):
    print("Afternoon")
elif(Hour>17 and Hour<=20):
    print("Good Evening")
elif(Hour>20 and Hour<=00 ):
    print("Gutumutu Nights")
elif(Hour>00 and Hour<=6):
    print("K garna uthya ehh??")
else:
    print("Hehh")