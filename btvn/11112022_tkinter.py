import tkinter as tk
window = tk.Tk()
window.geometry("300x400")
window.title("Đăng nhập")


def get_que_quan():
    print("Bạn đã nhập Tên: ", var_ten.get())
    print("Bạn đã chọn Giới tính: ", var_gioi_tinh.get())
    print("Bạn đã chọn Kết hôn: ", var_ket_hon.get())
    print("Bạn đã chọn quê quán: ", var_que_quan.get())

i = 0
var_ten = tk.StringVar(window)
ten = tk.Label(window, text="Tên", width="10", anchor="w").grid(row=i, column=0)
ten_entry = tk.Entry(window, textvariable=var_ten).grid(row=i, column=1)

i += 1
email = tk.Label(window, text="Email", width="10", anchor="w").grid(row=i, column=0)
email_entry = tk.Entry(window).grid(row=i, column=1)

i += 1
quoc_gia = tk.Label(window, text="Quốc gia", width="10", anchor="w").grid(row=i, column=0)
quoc_gia_entry = tk.Entry(window).grid(row=i, column=1)

i += 1
var_gioi_tinh = tk.IntVar(window)
var_gioi_tinh.set(1)
gioi_tinh = tk.Label(window, text="Giới tính", width="10", anchor="w").grid(row=i, column=0)
nam_entry = tk.Radiobutton(window, text="Nam", value=1, variable=var_gioi_tinh).grid(sticky="w", row=i, column=1)
i += 1
nu_entry = tk.Radiobutton(window, text="Nữ", value=2, variable=var_gioi_tinh).grid(sticky="w", row=i, column=1)
i += 1
khac_entry = tk.Radiobutton(window, text="Khác", value=3, variable=var_gioi_tinh).grid(sticky="w", row=i, column=1)

i += 1
var_ket_hon = tk.IntVar()
ket_hon = tk.Label(window, text="Kết hôn", width="10", anchor="w").grid(row=i, column=0)
ket_hon_entry = tk.Checkbutton(window, variable=var_ket_hon, onvalue=1, offvalue=0).grid(sticky="w", row=i, column=1)

i += 1
var_que_quan = tk.StringVar(window)
var_que_quan.set("Bình Dương")
que_quan = tk.Label(window, text="Quê quán", width="10", anchor="w").grid(row=i, column=0)
que_quan_entry = tk.OptionMenu(window, var_que_quan, "TpHCM", "Hà Nội", "Bình Dương").grid(sticky="w", row=i, column=1)

i += 1
submit = tk.Button(window, text="Submit", command=get_que_quan).grid(sticky="w", row=i, column=0)
window.mainloop()
