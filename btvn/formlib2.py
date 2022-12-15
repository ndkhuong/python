import tkinter as tk
from tkinter import messagebox

global Y, h


def show_send_data_form(root):
    Y = 10
    X1 = 10
    X2 = 100
    X3 = 210
    h = 35
    label_font = ("Arial", 9)
    pad_y = 7
    dropdown_width = 9

    
    CheckVar2 = tk.IntVar(value=1)
    C2 = tk.Checkbutton(root, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5)
    C2.pack()

    serial_port_var = tk.StringVar(value="COM3")
    list_opt = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5']
    label = tk.Label(root, text="Serial port", anchor='w')
    label.config(font=label_font, pady=pad_y)
    label.place(x=X1, y=Y)
    field = tk.OptionMenu(root, serial_port_var, *list_opt)
    field.config(width=dropdown_width)
    field.place(x=X2, y=Y)

    Y += h
    baud_rate_var = tk.IntVar(value="115200")
    list_opt = ['115200', '115201', '115202', '115203', '115204']
    label = tk.Label(root, text="Baud rate", anchor='w')
    label.config(font=label_font, pady=pad_y)
    label.place(x=X1, y=Y)
    field = tk.OptionMenu(root, baud_rate_var, *list_opt)
    field.config(width=dropdown_width)
    field.place(x=X2, y=Y)

    Y += h
    check_bits_var = tk.IntVar(value=3)
    list_opt = [1, 2, 3, 4, 5]
    label = tk.Label(root, text="Check bits", anchor='w')
    label.config(font=label_font, pady=pad_y)
    label.place(x=X1, y=Y)
    field = tk.OptionMenu(root, check_bits_var, *list_opt)
    field.config(width=dropdown_width)
    field.place(x=X2, y=Y)

    X_checkbtn = X3
    stm_var = tk.IntVar()
    stm_checkbtn = tk.Checkbutton(root, text="STM", variable=stm_var, onvalue=1, offvalue=0)
    stm_checkbtn.place(x=X_checkbtn, y=Y)

    X_checkbtn += 55
    ra_var = tk.IntVar(value=1)
    ra_checkbtn = tk.Checkbutton(root, text="RA", variable=ra_var, onvalue=1, offvalue=0)
    ra_checkbtn.place(x=X_checkbtn, y=Y)

    


    Y += h
    data_bits = tk.IntVar(value=5)
    list_opt = [1, 2, 3, 4, 5, 6, 7, 8]
    label = tk.Label(root, text="Data bits", anchor='w')
    label.config(font=label_font, pady=pad_y)
    label.place(x=X1, y=Y)
    field = tk.OptionMenu(root, data_bits, *list_opt)
    field.config(width=dropdown_width)
    field.place(x=X2, y=Y)

    Y += h
    stop_bits = tk.IntVar(value=8)
    list_opt = [1, 2, 3, 4, 5, 6, 7, 8]
    label = tk.Label(root, text="Stop bits", anchor='w')
    label.config(font=label_font, pady=pad_y)
    label.place(x=X1, y=Y)
    field = tk.OptionMenu(root, stop_bits, *list_opt)
    field.config(width=dropdown_width)
    field.place(x=X2, y=Y)

    Y += h
    open_port_btn = tk.Button(root, text="Open port", command="")
    open_port_btn.config(font=label_font, width=10)
    open_port_btn.place(x=X1, y=Y)

    close_port_btn = tk.Button(root, text="Close port", command="")
    close_port_btn.config(font=label_font, width=10)
    close_port_btn.place(x=X2, y=Y)

    Y += h
    open_port_btn = tk.Button(root, text="Receive", command="")
    open_port_btn.config(font=label_font, width=10)
    open_port_btn.place(x=X1, y=Y)


