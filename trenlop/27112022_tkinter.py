import tkinter as tk
from tkinter import ttk
import time

# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar')

root.grid()

# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

def start_progress():
    for i in range(0, 110, 10):
        pb["value"] = i
        root.update()
        time.sleep(0.5)


# start button
start_button = ttk.Button(
    root,
    text='Start',
    command=start_progress
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(
    root,
    text='Stop',
    command=pb.stop
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


root.mainloop()

'''Dùng thanh tiến trình, khi đạt 20 % in ra hình BTVN from đăng ký, khi dạt 50%, xuất hiện màn hình popup là Spinbox, khi đạt 80% xuất hiện man hình popup là khung nhập cho người dùng. 100%, xuất hiện màn hình popup là  menu có phím bấm "Quit"
'''