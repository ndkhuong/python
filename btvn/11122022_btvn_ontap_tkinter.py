
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import json 

# root window
root = tk.Tk()
root.geometry('800x650')
root.title('Form send data')
root.grid()

Y = 10
X1 = 10
X2 = 100
X3 = 210
X4 = 310
h = 35
label_font = ("Arial", 9)
pad_y = 7
dropdown_width = 9

#---COLUMN 1---
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

X_checkbtn += 50
ra_var = tk.IntVar()
ra_checkbtn = tk.Checkbutton(root, text="RA", variable=ra_var, onvalue=1, offvalue=0)
ra_checkbtn.place(x=X_checkbtn, y=Y)

X_checkbtn += 50
esp_var = tk.IntVar(value=1)
ra_checkbtn = tk.Checkbutton(root, text="ESP", variable=esp_var, onvalue=1, offvalue=0)
ra_checkbtn.place(x=X_checkbtn, y=Y)

X_checkbtn += 50
msp_var = tk.IntVar()
ra_checkbtn = tk.Checkbutton(root, text="MSP", variable=msp_var, onvalue=1, offvalue=0)
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
receive_btn = tk.Button(root, text="Receive", command="")
receive_btn.config(font=label_font, width=10)
receive_btn.place(x=X1, y=Y)

Y += h
X_checkbtn = X2 + 50
send_repeat_var = tk.IntVar()
send_repeat_checkbtn = tk.Checkbutton(root, text="Send repeat", variable=send_repeat_var, onvalue=1, offvalue=0, command= lambda: send_repeat())
send_repeat_checkbtn.place(x=X_checkbtn, y=Y)

Y += h
send_cmd1_btn = tk.Button(root, text="Send cmd1", command=lambda: send_cmd_data(1))
send_cmd1_btn.config(font=label_font, width=10)
send_cmd1_btn.place(x=X1, y=Y)
send_cmd1_entry = tk.Entry(root)
send_cmd1_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd1_nr_var = tk.IntVar()
send_cmd1_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd1_nr_var, onvalue=1, offvalue=0)
send_cmd1_nr.place(x=X4, y=Y)

Y += h
send_cmd2_btn = tk.Button(root, text="Send cmd2", command=lambda: send_cmd_data(2))
send_cmd2_btn.config(font=label_font, width=10)
send_cmd2_btn.place(x=X1, y=Y)
send_cmd2_entry = tk.Entry(root)
send_cmd2_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd2_nr_var = tk.IntVar()
send_cmd2_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd2_nr_var, onvalue=1, offvalue=0)
send_cmd2_nr.place(x=X4, y=Y)

Y += h
send_cmd3_btn = tk.Button(root, text="Send cmd3", command=lambda: send_cmd_data(3))
send_cmd3_btn.config(font=label_font, width=10)
send_cmd3_btn.place(x=X1, y=Y)
send_cmd3_entry = tk.Entry(root)
send_cmd3_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd3_nr_var = tk.IntVar()
send_cmd3_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd3_nr_var, onvalue=1, offvalue=0)
send_cmd3_nr.place(x=X4, y=Y)

Y += h
send_cmd4_btn = tk.Button(root, text="Send cmd4", command=lambda: send_cmd_data(4))
send_cmd4_btn.config(font=label_font, width=10)
send_cmd4_btn.place(x=X1, y=Y)
send_cmd4_entry = tk.Entry(root)
send_cmd4_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd4_nr_var = tk.IntVar()
send_cmd4_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd4_nr_var, onvalue=1, offvalue=0)
send_cmd4_nr.place(x=X4, y=Y)

Y += h
send_cmd5_btn = tk.Button(root, text="Send cmd5", command=lambda: send_cmd_data(5))
send_cmd5_btn.config(font=label_font, width=10)
send_cmd5_btn.place(x=X1, y=Y)
send_cmd5_entry = tk.Entry(root)
send_cmd5_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd5_nr_var = tk.IntVar()
send_cmd5_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd5_nr_var, onvalue=1, offvalue=0)
send_cmd5_nr.place(x=X4, y=Y)

Y += h
send_cmd6_btn = tk.Button(root, text="Send cmd6", command=lambda: send_cmd_data(6))
send_cmd6_btn.config(font=label_font, width=10)
send_cmd6_btn.place(x=X1, y=Y)
send_cmd6_entry = tk.Entry(root)
send_cmd6_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd6_nr_var = tk.IntVar()
send_cmd6_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd6_nr_var, onvalue=1, offvalue=0)
send_cmd6_nr.place(x=X4, y=Y)

Y += h
send_cmd7_btn = tk.Button(root, text="Send cmd7", command=lambda: send_cmd_data(7))
send_cmd7_btn.config(font=label_font, width=10)
send_cmd7_btn.place(x=X1, y=Y)
send_cmd7_entry = tk.Entry(root)
send_cmd7_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd7_nr_var = tk.IntVar()
send_cmd7_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd7_nr_var, onvalue=1, offvalue=0)
send_cmd7_nr.place(x=X4, y=Y)

Y += h
send_cmd8_btn = tk.Button(root, text="Send cmd8", command=lambda: send_cmd_data(8))
send_cmd8_btn.config(font=label_font, width=10)
send_cmd8_btn.place(x=X1, y=Y)
send_cmd8_entry = tk.Entry(root)
send_cmd8_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd8_nr_var = tk.IntVar()
send_cmd8_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd8_nr_var, onvalue=1, offvalue=0)
send_cmd8_nr.place(x=X4, y=Y)

Y += h
send_cmd9_btn = tk.Button(root, text="Send cmd9", command=lambda: send_cmd_data(9))
send_cmd9_btn.config(font=label_font, width=10)
send_cmd9_btn.place(x=X1, y=Y)
send_cmd9_entry = tk.Entry(root)
send_cmd9_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd9_nr_var = tk.IntVar()
send_cmd9_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd9_nr_var, onvalue=1, offvalue=0)
send_cmd9_nr.place(x=X4, y=Y)

Y += h
send_cmd10_btn = tk.Button(root, text="Send cmd10", command=lambda: send_cmd_data(10))
send_cmd10_btn.config(font=label_font, width=10)
send_cmd10_btn.place(x=X1, y=Y)
send_cmd10_entry = tk.Entry(root)
send_cmd10_entry.place(x=X2, y=Y, width=200,height=25)
send_cmd10_nr_var = tk.IntVar()
send_cmd10_nr = tk.Checkbutton(root, text="\\n,r", variable=send_cmd10_nr_var, onvalue=1, offvalue=0)
send_cmd10_nr.place(x=X4, y=Y)

#---END COLUMN 1---

#---COLUMN 2---
X1 = 450
X2 = 600
X3 = 500
X4 = 540
Y = 10

label = tk.Label(root, text="Send data:", anchor='w')
label.config(font=label_font, pady=pad_y)
label.place(x=X1, y=Y)

clear_send_data_btn = tk.Button(root, text="Clear send data", command= lambda: clear_send_data())
clear_send_data_btn.place(x=X2, y=Y, width=120)

Y += h
send_data_var = tk.Text(root, width=40, height=12)
send_data_var.place(x=X3, y=Y)

Y = 250
label = tk.Label(root, text="Receive data:", anchor='w')
label.config(font=label_font, pady=pad_y)
label.place(x=X1, y=Y)

clear_send_data_btn = tk.Button(root, text="Clear received data", command= lambda: clear_received_data())
clear_send_data_btn.place(x=X2, y=Y, width=120)

Y += h
receive_data_var = tk.Text(root, width=40, height=12)
receive_data_var.place(x=X3, y=Y)

Y = 455
X_btn = X4
load_file_btn = tk.Button(root, text="Load file", command= lambda: load_file())
load_file_btn.place(x=X_btn, y=Y, width=60)

X_btn += 80
save_file_btn = tk.Button(root, text="Save file", command= lambda: save_all_cmd_to_file())
save_file_btn.place(x=X_btn, y=Y, width=60)

X_btn += 80
send_file_btn = tk.Button(root, text="Send file", command="")
send_file_btn.place(x=X_btn, y=Y, width=60)

#---END COLUMN 2---

def send_repeat():
    if send_repeat_var.get() == 1:
        for button in range (1, 11):
            send_cmd_data(button)

def send_cmd_data(button):
    if (button == 1):
        add_text_to_content(send_cmd1_entry, send_cmd1_nr_var)
    elif(button == 2):
        add_text_to_content(send_cmd2_entry, send_cmd2_nr_var)
    elif(button == 3):
        add_text_to_content(send_cmd3_entry, send_cmd3_nr_var)
    elif(button == 4):
        add_text_to_content(send_cmd4_entry, send_cmd4_nr_var)
    elif(button == 5):
        add_text_to_content(send_cmd5_entry, send_cmd5_nr_var)
    elif(button == 6):
        add_text_to_content(send_cmd6_entry, send_cmd6_nr_var)
    elif(button == 7):
        add_text_to_content(send_cmd7_entry, send_cmd7_nr_var)
    elif(button == 8):
        add_text_to_content(send_cmd8_entry, send_cmd8_nr_var)
    elif(button == 9):
        add_text_to_content(send_cmd9_entry, send_cmd9_nr_var)
    elif(button == 10):
        add_text_to_content(send_cmd10_entry, send_cmd10_nr_var)

def add_text_to_content(entry, nr):
    text = entry.get()
    if (text != ""):
        send_data_var.insert(tk.END, text)
        if (nr.get() == 1):
            send_data_var.insert(tk.END, "\n")

def clear_send_data():
    send_data_var.delete(1.0, tk.END)

def clear_received_data():
    receive_data_var.delete(1.0, tk.END)

def save_all_cmd_to_file():
    save_file_cmd(send_cmd1_entry, 'cmd1_entry.txt', 1)
    save_file_cmd(send_cmd2_entry, 'cmd2_entry.txt', 2)
    save_file_cmd(send_cmd3_entry, 'cmd3_entry.txt', 3)
    save_file_cmd(send_cmd4_entry, 'cmd4_entry.txt', 4)
    save_file_cmd(send_cmd5_entry, 'cmd5_entry.txt', 5)
    save_file_cmd(send_cmd6_entry, 'cmd6_entry.txt', 6)
    save_file_cmd(send_cmd7_entry, 'cmd7_entry.txt', 7)
    save_file_cmd(send_cmd8_entry, 'cmd8_entry.txt', 8)
    save_file_cmd(send_cmd9_entry, 'cmd9_entry.txt', 9)
    save_file_cmd(send_cmd10_entry, 'cmd10_entry.txt', 10)

def save_file_cmd(entry, filename, cmd_index):
    text = entry.get()
    if (text != ""):
        dic = {'cmd_index': cmd_index, 'text': text}
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json.dumps(dic))
            file.close()

def load_file():
    file = fd.askopenfile(mode="r", filetypes=[("Text file", "*.txt")])
    if (file is not None):
        content = file.read()
        dic = json.loads(content)
        if (dic["cmd_index"] == 1):
            send_cmd1_entry.delete(0, tk.END)
            send_cmd1_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 2):
            send_cmd2_entry.delete(0, tk.END)
            send_cmd2_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 3):
            send_cmd3_entry.delete(0, tk.END)
            send_cmd3_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 4):
            send_cmd4_entry.delete(0, tk.END)
            send_cmd4_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 5):
            send_cmd5_entry.delete(0, tk.END)
            send_cmd5_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 6):
            send_cmd6_entry.delete(0, tk.END)
            send_cmd6_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 7):
            send_cmd7_entry.delete(0, tk.END)
            send_cmd7_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 8):
            send_cmd8_entry.delete(0, tk.END)
            send_cmd8_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 9):
            send_cmd9_entry.delete(0, tk.END)
            send_cmd9_entry.insert(0, dic["text"])
        elif (dic["cmd_index"] == 10):
            send_cmd10_entry.delete(0, tk.END)
            send_cmd10_entry.insert(0, dic["text"])

root.mainloop()