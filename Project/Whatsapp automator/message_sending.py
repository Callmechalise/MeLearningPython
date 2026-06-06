import pywhatkit
def message(Number,time_h,time_m,wait_time,tab_close,close_time):
    message = input("Enter message:")
    pywhatkit.sendwhatmsg(Number, message, time_h, time_m, wait_time, tab_close, close_time)