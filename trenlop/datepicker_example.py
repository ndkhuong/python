import tkinter  as tk 
from tkcalendar import DateEntry
from  datetime import date

my_w = tk.Tk()
cal=DateEntry(my_w,selectmode='day', year = 2020, month = 5, day = 22)
cal.grid(row=1,column=1,padx=15)

dt=date(2021,8,19) # specific date Year, month , day
#cal.set_date(dt) # Set the selected date 
#cal.set_date('8/16/2021') # Set the local calendar format 

def grad_date():
    date.config(text = "Selected Date is: " + str(cal.get_date()))

# Add Button and Label
tk.Button(my_w, text = "Get Date", command = grad_date).grid(row=2,column=0,padx=15)
date = tk.Label(my_w, text = "")
date.grid(row=3,column=0,padx=15)

my_w.mainloop()