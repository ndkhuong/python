import tkinter as tk
window = tk.Tk()
window.geometry("250x200")
window.title("Đăng nhập")

i = 0
ten = tk.Label(window, text="Tên", width="10", anchor="w").grid(row=i, column=0)
ten_entry = tk.Entry(window).grid(row=i, column=1)

i += 1
email = tk.Label(window, text="Email", width="10", anchor="w").grid(row=i, column=0)
email_entry = tk.Entry(window).grid(row=i, column=1)

i += 1
quoc_gia = tk.Label(window, text="Quốc gia", width="10", anchor="w").grid(row=i, column=0)
quoc_gia_entry = tk.Entry(window).grid(row=i, column=1)

i += 1
var_gt = tk.IntVar()
var_gt.set(1)
gioi_tinh = tk.Label(window, text="Giới tính", width="10", anchor="w").grid(row=i, column=0)
nam_entry = tk.Radiobutton(window, text="Nam", variable=var_gt, value=1).grid(sticky="w", row=i, column=1)
i += 1
nu_entry = tk.Radiobutton(window, text="Nữ", variable=var_gt, value=2).grid(sticky="w", row=i, column=1)
i += 1
khac_entry = tk.Radiobutton(window, text="Khác", variable=var_gt, value=3).grid(sticky="w", row=i, column=1)

i += 1
submit = tk.Button(window, text="Submit").grid(sticky="w", row=i, column=0)
window.mainloop()
