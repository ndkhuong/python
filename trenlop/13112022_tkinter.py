import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.title("Dang nhap")

x1 = 10
x2 = 120
h = 20
step = 30

username = tk.Label(window, text="Họ tên: ").place(x=x1, y=h)
entry1 = tk.Entry(window).place(x=x2, y=h)

h += step
email = tk.Label(window, text="Email: ").place(x=x1, y=h)
entry2 = tk.Entry(window).place(x=x2, y=h)

h += step
dt = tk.Label(window, text="Điện thoại: ").place(x=x1, y=h)
entry3 = tk.Entry(window).place(x=x2, y=h)

h += step
gt = tk.Label(window, text="Chọn giới tính: ").place(x=x1, y=h)
var_gt = tk.IntVar(window)
var_gt.set(1)
entry4 = tk.Radiobutton(text="Nam", value=1, variable=var_gt).place(x=x2, y=h)
entry5 = tk.Radiobutton(text="Nu", value=0, variable=var_gt).place(x=x2 + 50, y=h)
entry6 = tk.Radiobutton(text="Khác", value=2, variable=var_gt).place(x=x2 + 100, y=h)

h += step
var_qg = tk.IntVar(window)
var_qg.set('Việt Nam')
dt = tk.Label(window, text="Quốc gia: ").place(x=x1, y=h)
list_opt = ["Việt Nam", "Lào", "Campuchia"]
entry3 = tk.OptionMenu(window, var_qg, *list_opt).place(x=x2, y=h)

h += step
dt = tk.Label(window, text="Password: ").place(x=x1, y=h)
entry3 = tk.Entry(window).place(x=x2, y=h)

h += step
dt = tk.Label(window, text="Re-enter Password: ").place(x=x1, y=h)
entry3 = tk.Entry(window).place(x=x2, y=h)


h += step
submit = tk.Button(window, text="Submit", activebackground="red").place(x=x1, y=h)

window.mainloop()