import tkinter as tk
login_window = tk.Tk()
login_window.geometry("400x250")
login_window.title("Dang nhap")
username = tk.Label(login_window, text="Username: ").place(x=30, y=50)
entry1 = tk.Entry(login_window).place(x=100, y=50)
login_window.mainloop()