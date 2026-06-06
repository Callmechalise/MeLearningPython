import tkinter as tk
from tkinter import filedialog
import os
import pywhatkit

from main import time_h, time_m, wait_time, close_time

application_window = tk.Tk()
def image(Number):
    image = filedialog.askopenfilename(parent=application_window,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=[('all files', '.*')])
    caption=input("Enter caption")
    pywhatkit.sendwhats_image(Number, "Images/Hello.png",time_h,time_m,wait_time,close_time,"Hello")