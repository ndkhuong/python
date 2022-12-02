'''Dùng thanh tiến trình, 
khi đạt 20 % in ra hình BTVN from đăng ký, 
khi dạt 50%, xuất hiện màn hình popup là Spinbox, 
khi đạt 80% xuất hiện man hình popup là khung nhập cho người dùng. 
100%, xuất hiện màn hình popup là  menu có phím bấm "Quit"
'''

import tkinter as tk
from tkinter import ttk
import time
import formlib

# root window
root = tk.Tk()
root.geometry('400x500')
root.title('Progressbar')
root.grid()

# progressbar
pb = ttk.Progressbar(root, orient='horizontal', length=380)
pb.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

def start_progress():
    for i in range(0, 110, 10):
        pb["value"] = i
        
        if (i == 20):
            formlib.show_register_form(root)
        elif (i == 50):
            formlib.show_popup_spinbox(root)
        elif (i == 80):
            formlib.show_popup_textarea(root) 
        elif (i == 100):
            formlib.show_popup_quit(root)

        root.update()
        time.sleep(0.5)

start_button = ttk.Button(root, text='Start', command=start_progress)
start_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
root.mainloop()