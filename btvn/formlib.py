import tkinter as tk

def show_popup_textarea(root):
    popup = tk.Tk()
    popup.wm_title("Popup")
    label = tk.Label(popup, text="Your Textbox")
    label.pack(side="top", fill="x", pady=10)

    w = tk.Text(popup, width=50, height=20)
    w.pack(padx=10, pady=10)

    B1 = tk.Button(popup, text="Quit", command= lambda: quit_and_close(popup))
    B1.pack(padx=10, pady=10)
    popup.mainloop()

def quit_all(popup, root):
    popup.quit()
    popup.destroy()
    root.destroy()

def quit_and_close(popup):
    popup.quit()
    popup.destroy()

def show_popup_quit(root):
    popup = tk.Tk()
    label = tk.Label(popup, text="Do you want to quit")
    label.pack(side="top", fill="x", pady=10)

    B1 = tk.Button(popup, text="Quit", command= lambda: quit_all(popup, root))
    B1.pack(padx=10, pady=10)
    popup.mainloop()

def show_popup_spinbox(root):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text="Your Spinbox")
    label.pack(side="top", fill="x", pady=10)

    w = tk.Spinbox(popup, from_=0, to=10)
    w.pack(padx=10, pady=10)

    B1 = tk.Button(popup, text="Quit", command= lambda: quit_and_close(popup))
    B1.pack(padx=10, pady=10)

    popup.mainloop()

def show_register_form(root):
    X1 = 10
    X2 = 130
    Y = 100
    h = 35
    tk.Label(root, text="Họ tên", anchor='w').place(x=X1, y=Y)
    fullname = tk.Entry(root).place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Email", anchor='w').place(x=X1, y=Y)
    email = tk.Entry(root).place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Điện thoại", anchor='w').place(x=X1, y=Y)
    phone = tk.Entry(root).place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Giới tính", anchor='w').place(x=X1, y=Y)
    var_gt = tk.IntVar()
    var_gt.set(1)
    iframe1 = tk.Frame(root, bd=1, relief=tk.SUNKEN)
    male_entry = tk.Radiobutton(iframe1, text="Nam", variable=var_gt, value=1).pack(side=tk.LEFT, anchor=tk.W)
    female_entry = tk.Radiobutton(iframe1, text="Nữ", variable=var_gt, value=2).pack(side=tk.LEFT, anchor=tk.W)
    other_entry = tk.Radiobutton(iframe1, text="Khác", variable=var_gt, value=3).pack(side=tk.LEFT, anchor=tk.W)
    iframe1.place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Quốc gia", anchor='w').place(x=X1, y=Y)
    var_qg = tk.IntVar(root)
    var_qg.set('Việt Nam')
    list_opt = ["Việt Nam", "Lào", "Campuchia"]
    country = tk.OptionMenu(root, var_qg, *list_opt).place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Password", anchor='w').place(x=X1, y=Y)
    password = tk.Entry(root).place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Re-Enter password", anchor='w').place(x=X1, y=Y)
    repassword = tk.Entry(root).place(x=X2, y=Y)

