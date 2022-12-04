'''Lưu thông tin form vào file
'''

import tkinter as tk
from tkinter import ttk
import time
import formlib

# root window
root = tk.Tk()
root.geometry('400x500')
root.title('Form đăng ký')
root.grid()

formlib.show_register_form2(root)
root.mainloop()