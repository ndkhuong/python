from tkinter import *
class Shape:
    def __init__(self, master):
        self.canvas = Canvas(master)
        self.canvas.pack(fill=BOTH) #start from left

    def create_oval(self):
        self.canvas.create_oval(10,10,50,50, fill='red', width=1) 
    def create_rectangle(self):
        self.canvas.create_rectangle(60,10,100,70, fill='grey', width=1)
    def create_arc(self):
        self.canvas.create_arc(110,10,160,50, fill='red', width=1)  
    def create_polygon(self):
        self.canvas.create_polygon(150,75,225,0,300,75, 320, 150,225,150, fill='red', width=1)        
    def create_line(self):
        self.canvas.create_line(350, 10, 400, 100, fill='red', width=2)

mater = Tk()
s1 = Shape(mater)
s1.create_oval()
s1.create_rectangle()
s1.create_arc()
s1.create_polygon()
s1.create_line()
mater.geometry('500x300')
mainloop()

