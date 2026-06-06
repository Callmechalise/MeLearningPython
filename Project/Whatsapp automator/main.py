import sys
import pywhatkit
import message_sending
from message_sending import message
import image_sending
from image_sending import image
Number = "+977" + input("Enter number:")
time_h = int(input('Enter time in hour:'))
time_m = int(input("Enter time in min:"))
wait_time=50
tab_close=True
close_time=15

def menu():
    while True:
        print("Enter no according to required service (:\n")
        print("1.Message sending")
        print("2.Image sending")
        print("3.Quit")
        inp=int(input("Enter no::::>"))
        if(inp==1):
            message(Number,time_h,time_m,wait_time,tab_close,close_time)
        elif(inp==2):
            image(Number)
        elif(inp==3):
            sys.exit()
menu()


