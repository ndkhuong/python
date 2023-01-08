from tkinter import *
from tkinter import ttk
import time
import subprocess
import win32api, win32con
import keyboard

class control():
    def __init__(self, root, window_width, window_height):
        self.root = root
        self.window_width = window_width
        self.window_height = window_height
        self.url_var = StringVar(master=self.root)
    
    def get_url_form(self):
        url_form  =  Frame(self.root,  width=self.window_width,  height=  100)
        url_form.grid(row=0,  column=0,  padx=10,  pady=5, sticky='wn')
        
        ROW = 0
        Label(url_form,  text="Your URL").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
        Entry(url_form, textvariable=self.url_var, width=100).grid(row=ROW,  column=1,  padx=5,  pady=5)
        Button(url_form,  text="Open", command=lambda: self.open_url()).grid(row=ROW,  column=2,  padx=5,  pady=5, ipadx=10, sticky=W)

    def open_url(self):
        #https://www.youtube.com/watch?v=KgOtLOUdCMQ
        url = self.url_var.get()
        print(url)

        subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
        time.sleep(3)

        self.click(200, 50)
        print('clicked')

        keyboard.write(url)
        print('typed')
        
        keyboard.press_and_release('enter')
        print('pressed Enter')

        time.sleep(3)
        self.click(450, 380)
        print('clicked to Play')

    def click(self, x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

###############################################
window_width = 800
window_height = 100

root  =  Tk()  
root.title("Open URL")

root.geometry('%dx%d' % (window_width, window_height))
root.minsize(window_width, window_height)
root.maxsize(window_width, window_height)

c = control(root, window_width, window_height)
c.get_url_form()

root.mainloop()