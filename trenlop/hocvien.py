from tkinter import *

root  =  Tk()  # create root window
root.title("QUẢN LÝ HỌC VIÊN")
root.geometry('930x620')

import hocvien_lib as lib
lib.create_table()

# Create left and right frames
main_frame  =  Frame(root,  width=lib.window_width,  height=  600)
main_frame.grid(row=0,  column=0,  padx=10,  pady=10, sticky='wn')

lib.get_add_form(main_frame)
lib.get_list_student(main_frame)

root.mainloop()