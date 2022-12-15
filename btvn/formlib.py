import tkinter as tk
from tkinter import messagebox



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


def show_register_form2(root):
    X1 = 10
    X2 = 130
    Y = 10
    h = 35
    tk.Label(root, text="Họ tên", anchor='w').place(x=X1, y=Y)
    fullname = tk.Entry(root)
    fullname.place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Email", anchor='w').place(x=X1, y=Y)
    email = tk.Entry(root)
    email.place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Điện thoại", anchor='w').place(x=X1, y=Y)
    phone = tk.Entry(root)
    phone.place(x=X2, y=Y)

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
    var_qg = tk.StringVar(root)
    var_qg.set('Việt Nam')

    country_file = open("country.txt", 'r')
    country_list = []
    for country in country_file:
        country_list.append(country.rstrip("\n"))

    country = tk.OptionMenu(root, var_qg, *country_list).place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Password", anchor='w').place(x=X1, y=Y)
    password = tk.Entry(root)
    password.place(x=X2, y=Y)

    Y += h
    tk.Label(root, text="Re-Enter password", anchor='w').place(x=X1, y=Y)
    repassword = tk.Entry(root)
    repassword.place(x=X2, y=Y)

    def validate_and_save_file():
        if (fullname.get() == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Họ tên")
            fullname.focus_set()
            return
        if (email.get() == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Email")
            email.focus_set()
            return
        if (phone.get() == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Điện thoại")
            phone.focus_set()
            return
        if (var_gt.get() == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Giới tính")
            return
        if (var_qg.get() == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Quốc gia")
            return
        if (password.get() == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Password")
            password.focus_set()
            return
        if (repassword.get() == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Re-password")
            repassword.focus_set()
            return
        if (password.get() != repassword.get()):
            messagebox.showinfo("Thông báo lỗi", "Password và Re-password phải giống nhau")
            repassword.focus_set()
            return
        with open('register_data.txt', 'w', encoding="utf-8") as file:
            file.write("fullname:" + fullname.get() + "\n")
            file.write("email:" + email.get() + "\n")
            file.write("phone:" + phone.get() + "\n")
            file.write("gender:" + str(var_gt.get()) + "\n")
            file.write("country:" + str(var_qg.get()) + "\n")
            file.write("password:" + password.get() + "\n")
            file.write("repassword:" + repassword.get() + "\n")
            file.close()

    Y += h
    tk.Button(root, text="Register", command=validate_and_save_file).place(x=X1, y=Y)
