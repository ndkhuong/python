from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkcalendar import DateEntry
from datetime import datetime, timedelta

window_width = 800

#ADD VAR
global ngay_bat_dau_var
global tree
ho_ten_var = StringVar()
ma_lop_var = StringVar()
hoc_phi_var = IntVar()
so_buoi_hoc_var = IntVar()
thu_2_var = IntVar()
thu_3_var = IntVar()
thu_4_var = IntVar()
thu_5_var = IntVar()
thu_6_var = IntVar()
thu_7_var = IntVar()
cn_var = IntVar()

#UPDATE VAR
global update_ngay_bat_dau_var
global update_ngay_ket_thuc_var
global update_ho_ten_var 
global update_ma_lop_var 
global update_hoc_phi_var 
global update_so_buoi_hoc_var 
global update_thu_2_var  
global update_thu_3_var  
global update_thu_4_var  
global update_thu_5_var  
global update_thu_6_var 
global update_thu_7_var 
global update_cn_var 


def conn_db():
    conn = sqlite3.connect("quanly_hocvien.db") 
    return conn

def create_table():
    conn = conn_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS hocvien (
                id INTEGER PRIMARY KEY  AUTOINCREMENT,
                ho_ten  varchar(500) NOT NULL,
                ma_lop  varchar(500) NULL,
                tinh_trang tinyint(1) DEFAULT 1,
                ngay_bat_dau date NULL,
                ngay_ket_thuc date NULL,
                thu_2 tinyint(1) NULL,
                thu_3 tinyint(1) NULL,
                thu_4 tinyint(1) NULL,
                thu_5 tinyint(1) NULL,
                thu_6 tinyint(1) NULL,
                thu_7 tinyint(1) NULL,
                cn tinyint(1) NULL,
                so_buoi_hoc int(11) NULL,
                hoc_phi int(11) NULL,
                ngay_cap_nhat date NULL);''')
    conn.close()

def add_new_student(main_frame):
    global ngay_bat_dau_var

    ho_ten = ho_ten_var.get()
    ma_lop = ma_lop_var.get()
    ngay_bat_dau = ngay_bat_dau_var.get_date()
    hoc_phi = int(hoc_phi_var.get())
    so_buoi_hoc  = int(so_buoi_hoc_var.get())
    thu_2 = thu_2_var.get()
    thu_3 = thu_3_var.get()
    thu_4 = thu_4_var.get()
    thu_5 = thu_5_var.get()
    thu_6 = thu_6_var.get()
    thu_7 = thu_7_var.get()
    cn = cn_var.get()

    print(ngay_bat_dau)

    if (ho_ten == ""):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Họ tên")
        return
    if (ngay_bat_dau == ""):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Ngày bắt đầu")
        return
    if (so_buoi_hoc == 0):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Số buổi học")
        return
    if (hoc_phi == 0):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Học phí")
        return
    thu_hoc_cnt = thu_2 + thu_3 + thu_4 + thu_5 + thu_6 + thu_7 + cn
    if (thu_hoc_cnt == 0):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần chọn Thứ học")
        return

    ngay_ket_thuc = get_ngay_ket_thuc(ngay_bat_dau, so_buoi_hoc, thu_2, thu_3, thu_4, thu_5, thu_6, thu_7, cn)
    data = (
        ho_ten,
        ma_lop,
        ngay_bat_dau,
        ngay_ket_thuc,
        thu_2,
        thu_3,
        thu_4,
        thu_5,
        thu_6,
        thu_7,
        cn,
        so_buoi_hoc,
        hoc_phi,
    )
    sql = ''' INSERT INTO hocvien(ho_ten, ma_lop, ngay_bat_dau, ngay_ket_thuc, thu_2, thu_3, thu_4, thu_5, thu_6, thu_7, cn, so_buoi_hoc, hoc_phi, ngay_cap_nhat)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?, CURRENT_TIMESTAMP) '''
    
    conn = conn_db()
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    conn.close()

    get_list_student(main_frame)
    return cur.lastrowid

def delete_student(id):
    print(11)

def get_ngay_ket_thuc(ngay_bat_dau, so_buoi_hoc, thu_2, thu_3, thu_4, thu_5, thu_6, thu_7, cn):
    thu_hoc = []
    if (thu_2 == 1):
        thu_hoc.append('Monday')
    if (thu_3 == 1):
        thu_hoc.append('Tuesday')
    if (thu_4 == 1):
        thu_hoc.append('Wednesday')
    if (thu_5 == 1):
        thu_hoc.append('Thursday')
    if (thu_6 == 1):
        thu_hoc.append('Friday')
    if (thu_7 == 1):
        thu_hoc.append('Saturday')
    if (cn == 1):
        thu_hoc.append('Sunday')

    current_date = datetime(ngay_bat_dau.year, ngay_bat_dau.month, ngay_bat_dau.day)
    cnt = 0
    i = 0
    while (cnt < so_buoi_hoc):
        next_date = current_date + timedelta(days=i)
        next_day_name = next_date.strftime("%A")
        if (next_day_name in thu_hoc):
            cnt += 1
        i += 1

    last_date = next_date.strftime("%Y-%m-%d")
    return last_date

def get_add_form(main_frame):
    global ngay_bat_dau_var
    add_form  =  Frame(main_frame,  width=window_width,  height=  200)
    add_form.grid(row=0,  column=0,  padx=10,  pady=5, sticky='w' + 'n')
    
    ROW = 0
    Label(add_form,  text="Họ tên").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
    Entry(add_form, textvariable=ho_ten_var).grid(row=ROW,  column=1,  padx=5,  pady=5)
    
    Label(add_form,  text="Mã lớp").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
    Entry(add_form, textvariable=ma_lop_var).grid(row=ROW,  column=3,  padx=5,  pady=5)
    
    ROW = 1
    today = datetime.today()
    Label(add_form,  text="Ngày bắt đầu").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
    ngay_bat_dau_var = DateEntry(add_form, width=17,date_pattern='yyyy-mm-dd' , selectmode='day', year = today.year, month = today.month, day = today.day)
    ngay_bat_dau_var.grid(row=ROW,  column=1,  padx=5,  pady=5)

    Label(add_form,  text="Số buổi học").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
    Entry(add_form, textvariable=so_buoi_hoc_var).grid(row=ROW,  column=3,  padx=5,  pady=5)
    
    ROW = 2
    Label(add_form,  text="Học phí").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
    Entry(add_form, textvariable=hoc_phi_var).grid(row=ROW,  column=1,  padx=5,  pady=5)
    
    ROW = 3
    thu_form  =  Frame(add_form,  width=window_width,  height=  60)
    thu_form.grid(row=ROW,  column=0,  padx=0,  pady=5, columnspan=4, sticky=W)

    Label(thu_form,  text="Thứ học").grid(row=0,  column=0,  padx=5,  pady=5, sticky=W, columnspan=7)
    Checkbutton(thu_form, text="Thứ 2", variable=thu_2_var, onvalue=1, offvalue=0).grid(row=1,  column=0,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 3", variable=thu_3_var, onvalue=1, offvalue=0).grid(row=1,  column=1,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 4", variable=thu_4_var, onvalue=1, offvalue=0).grid(row=1,  column=2,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 5", variable=thu_5_var, onvalue=1, offvalue=0).grid(row=1,  column=3,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 6", variable=thu_6_var, onvalue=1, offvalue=0).grid(row=1,  column=4,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 7", variable=thu_7_var, onvalue=1, offvalue=0).grid(row=1,  column=5,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Chủ nhật", variable=cn_var, onvalue=1, offvalue=0).grid(row=1,  column=6,  padx=5,  pady=5)

    ROW = 4
    btn_tool  =  Frame(add_form,  width=window_width,  height=  60)
    btn_tool.grid(row=ROW,  column=0,  padx=0,  pady=5, columnspan=4, sticky=W)

    Button(btn_tool,  text="Thêm học viên", command=lambda: add_new_student(main_frame)).grid(row=ROW,  column=0,  padx=5,  pady=5, ipadx=10, sticky=W)
    Button(btn_tool,  text="Tìm kiếm", command=lambda: find_student(main_frame)).grid(row=ROW,  column=1,  padx=5,  pady=5, ipadx=10, sticky=W)
    Button(btn_tool,  text="Tất cả", command=lambda: refresh_list(main_frame)).grid(row=ROW,  column=2,  padx=5,  pady=5, ipadx=10, sticky=W)
    Button(btn_tool,  text="Sắp hết khóa", command=lambda: find_student(main_frame, end_course=1)).grid(row=ROW,  column=3,  padx=5,  pady=5, ipadx=10, sticky=W)

def get_thu_hoc(row):
    str = ""
    if (row["thu_2"] == 1):
        str += "2, "
    if (row["thu_3"] == 1):
        str += "3, "
    if (row["thu_4"] == 1):
        str += "4, "
    if (row["thu_5"] == 1):
        str += "5, "
    if (row["thu_6"] == 1):
        str += "6, "
    if (row["thu_7"] == 1):
        str += "7, "
    if (row["cn"] == 1):
        str += "CN, "
    return str.rstrip(', ')

def refresh_list(main_frame):
    return get_list_student(main_frame)

def find_student(main_frame, end_course = 0):
    search = {}
    if (end_course == 0):
        ho_ten = ho_ten_var.get()
        if (ho_ten != ''):
            search["ho_ten"] = ho_ten
    else:
        search["end_course"] = 1
    return get_list_student(main_frame, search)

def get_list_student(main_frame, search={}):
    global tree

    if 'tree' in locals():
        tree.delete(*tree.get_children())

    ROW = 1
    list_student_frame  =  Frame(main_frame,  width=window_width,  height=  300)
    list_student_frame.grid(row=ROW,  column=0,  padx=10,  pady=5)

    #extended = can select multi row
    #browse = can only select single row
    tree = ttk.Treeview(list_student_frame, height=15, selectmode="browse", column=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), show='headings')
    
    col = 1
    tree.heading("#" + str(col), text="STT")
    tree.column("#" + str(col), minwidth=0, width=30, stretch=NO, anchor=CENTER)

    col += 1
    tree.heading("#" + str(col), text="ID")
    tree.column("#" + str(col), minwidth=0, width=30, stretch=NO, anchor=CENTER)

    col += 1
    tree.heading("#" + str(col), text="Họ tên")
    tree.column("#" + str(col), minwidth=0, width=160, stretch=NO, anchor=W)

    col += 1
    tree.heading("#" + str(col), text="Mã lớp")
    tree.column("#" + str(col), minwidth=0, width=100, stretch=NO, anchor=CENTER)

    col += 1
    tree.heading("#" + str(col), text="Ngày bắt đầu")
    tree.column("#" + str(col), minwidth=0, width=90, stretch=NO, anchor=CENTER)

    col += 1
    tree.heading("#" + str(col), text="Ngày kết thúc")
    tree.column("#" + str(col), minwidth=0, width=95, stretch=NO, anchor=CENTER)
    
    col += 1
    tree.heading("#" + str(col), text="Số buổi học")
    tree.column("#" + str(col), minwidth=0, width=80, stretch=NO, anchor=CENTER)
    
    col += 1
    tree.heading("#" + str(col), text="Thứ học")
    tree.column("#" + str(col), minwidth=0, width=120, stretch=NO, anchor=CENTER)
    
    col += 1
    tree.heading("#" + str(col), text="Học phí")
    tree.column("#" + str(col), minwidth=0, width=100, stretch=NO, anchor=CENTER)

    col += 1
    tree.heading("#" + str(col), text="Tình trạng")
    tree.column("#" + str(col), minwidth=0, width=100, stretch=NO, anchor=CENTER)
    
    data_bind = []
    sql = "SELECT * FROM hocvien"
    conds = ""
    if ("ho_ten" in search and search["ho_ten"] != ""):
        conds += "AND ho_ten LIKE ?"
        data_bind.append('%' + search["ho_ten"] + '%')

    if ("end_course" in search and search["end_course"] == 1):
        today = datetime.today()
        curr_year = today.year
        curr_month = today.month
        if (curr_month < 10):
            curr_month = '0' + str(curr_month)
        conds += "AND ngay_ket_thuc LIKE ?"
        data_bind.append(str(curr_year) + '-' + str(curr_month) + '%')

    if (conds != ""):
        sql += " WHERE" + conds.lstrip("AND")
    sql += " ORDER BY ngay_cap_nhat DESC"

    conn = conn_db()
    conn.row_factory = sqlite3.Row #alert that we want to get key: value
    cur = conn.cursor()
    cur.execute(sql, data_bind)
    rows = [dict(row) for row in cur.fetchall()] #convert tup to dict

    stt = 0
    sum = 0
    for row in rows:
        stt += 1
        sum += row["hoc_phi"]
        #print(row) # it print all records in the database
        thu_hoc = get_thu_hoc(row)
        if (row["tinh_trang"] == 1):
            tinh_trang = "Đang học"
        else:
            tinh_trang = "Nghỉ"
        data = (
            stt,
            row["id"],
            row["ho_ten"],
            row["ma_lop"],
            row["ngay_bat_dau"],
            row["ngay_ket_thuc"],
            row["so_buoi_hoc"],
            thu_hoc,
            '{:,d}'.format(row["hoc_phi"]).replace(',','.'),
            tinh_trang,
        )
        tree.insert("", END, values=data)
    conn.close()

    tree.grid(row=0,  column=0,  padx=5,  pady=5, sticky=W)
    
    # add a scrollbar
    scrollbar = ttk.Scrollbar(list_student_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    tree.bind('<<TreeviewSelect>>', item_selected)

    sum = '{:,d}'.format(sum).replace(',','.')
    Label(list_student_frame, font=("Arial", 10),  text="Tổng học phí: " + str(sum)).grid(row=1,  column=0,  padx=5,  pady=5, sticky=W)

def item_selected(event): 
    global tree
    print(tree.selection())
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
    id = record[1]
    show_update_form(id)

def show_update_form(student_id):
    popup = Tk()
    popup.wm_title("CẬP NHẬT THÔNG TIN HỌC VIÊN")
    popup.geometry('510x230')

    get_update_form(popup, student_id)

    popup.mainloop()

def get_update_form(popup, student_id):
    global update_ngay_bat_dau_var
    global update_ngay_ket_thuc_var
    global update_ho_ten_var 
    global update_ma_lop_var 
    global update_hoc_phi_var 
    global update_so_buoi_hoc_var 
    global update_thu_2_var  
    global update_thu_3_var  
    global update_thu_4_var  
    global update_thu_5_var  
    global update_thu_6_var 
    global update_thu_7_var 
    global update_cn_var 

    sql = '''SELECT * FROM hocvien WHERE id = ?'''
    conn = conn_db()
    conn.row_factory = sqlite3.Row #alert that we want to get key: value
    cur = conn.cursor()
    cur.execute(sql, [student_id])
    data = dict(cur.fetchone())

    add_form  =  Frame(popup,  width=600,  height=  200)
    add_form.grid(row=0,  column=0,  padx=10,  pady=5, sticky='w' + 'n')
    
    ROW = 0
    update_ho_ten_var = StringVar(master=popup, value=data["ho_ten"])
    Label(add_form,  text="Họ tên").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
    Entry(add_form, textvariable=update_ho_ten_var).grid(row=ROW,  column=1,  padx=5,  pady=5)
    
    update_ma_lop_var = StringVar(master=popup, value=data["ma_lop"])
    Label(add_form,  text="Mã lớp").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
    Entry(add_form, textvariable=update_ma_lop_var).grid(row=ROW,  column=3,  padx=5,  pady=5)
    
    ROW = 1
    ngay_bat_dau = datetime.strptime(data["ngay_bat_dau"], '%Y-%m-%d')
    Label(add_form,  text="Ngày bắt đầu").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
    update_ngay_bat_dau_var = DateEntry(add_form, width=17,date_pattern='yyyy-mm-dd' , selectmode='day', year = ngay_bat_dau.year, month = ngay_bat_dau.month, day = ngay_bat_dau.day)
    update_ngay_bat_dau_var.grid(row=ROW,  column=1,  padx=5,  pady=5)

    update_so_buoi_hoc_var = StringVar(master=popup, value=data["so_buoi_hoc"])
    Label(add_form,  text="Số buổi học").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
    Entry(add_form, textvariable=update_so_buoi_hoc_var).grid(row=ROW,  column=3,  padx=5,  pady=5)
    
    ROW = 2
    update_hoc_phi_var = StringVar(master=popup, value=data["hoc_phi"])
    Label(add_form,  text="Học phí").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
    Entry(add_form, textvariable=update_hoc_phi_var).grid(row=ROW,  column=1,  padx=5,  pady=5)
    
    ngay_ket_thuc = datetime.strptime(data["ngay_ket_thuc"], '%Y-%m-%d')
    Label(add_form,  text="Ngày kết thúc").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
    update_ngay_ket_thuc_var = DateEntry(add_form, width=17,date_pattern='yyyy-mm-dd' , selectmode='day', year = ngay_ket_thuc.year, month = ngay_ket_thuc.month, day = ngay_ket_thuc.day)
    update_ngay_ket_thuc_var.grid(row=ROW,  column=3,  padx=5,  pady=5)
    
    ROW = 3
    thu_form  =  Frame(add_form,  width=window_width,  height=  60)
    thu_form.grid(row=ROW,  column=0,  padx=0,  pady=5, columnspan=4, sticky=W)

    Label(thu_form,  text="Thứ học").grid(row=0,  column=0,  padx=5,  pady=5, sticky=W, columnspan=7)
    update_thu_2_var = IntVar(master=popup, value=data["thu_2"])
    update_thu_3_var = IntVar(master=popup, value=data["thu_3"])
    update_thu_4_var = IntVar(master=popup, value=data["thu_4"])
    update_thu_5_var = IntVar(master=popup, value=data["thu_5"])
    update_thu_6_var = IntVar(master=popup, value=data["thu_6"])
    update_thu_7_var = IntVar(master=popup, value=data["thu_7"])
    update_cn_var = IntVar(master=popup, value=data["cn"])
    Checkbutton(thu_form, text="Thứ 2", variable=update_thu_2_var, onvalue=1, offvalue=0).grid(row=1,  column=0,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 3", variable=update_thu_3_var, onvalue=1, offvalue=0).grid(row=1,  column=1,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 4", variable=update_thu_4_var, onvalue=1, offvalue=0).grid(row=1,  column=2,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 5", variable=update_thu_5_var, onvalue=1, offvalue=0).grid(row=1,  column=3,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 6", variable=update_thu_6_var, onvalue=1, offvalue=0).grid(row=1,  column=4,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Thứ 7", variable=update_thu_7_var, onvalue=1, offvalue=0).grid(row=1,  column=5,  padx=5,  pady=5)
    Checkbutton(thu_form, text="Chủ nhật", variable=update_cn_var, onvalue=1, offvalue=0).grid(row=1,  column=6,  padx=5,  pady=5)

    ROW = 4
    btn_tool  =  Frame(add_form,  width=window_width,  height=  60)
    btn_tool.grid(row=ROW,  column=0,  padx=0,  pady=5, columnspan=4, sticky=E)

    Button(btn_tool,  text="Cập nhật", command=lambda: update_student(student_id)).grid(row=ROW,  column=0,  padx=5,  pady=5, ipadx=10, sticky=W)
    Button(btn_tool,  text="Xóa", padx=10, command=lambda: delete_student(student_id)).grid(row=ROW,  column=1,  padx=5,  pady=5, ipadx=10, sticky=W)

def update_student(student_id):
    global update_ngay_bat_dau_var
    global update_ngay_ket_thuc_var
    global update_ho_ten_var 
    global update_ma_lop_var 
    global update_hoc_phi_var 
    global update_so_buoi_hoc_var 
    global update_thu_2_var  
    global update_thu_3_var  
    global update_thu_4_var  
    global update_thu_5_var  
    global update_thu_6_var 
    global update_thu_7_var 
    global update_cn_var 

    ho_ten = update_ho_ten_var.get()
    ma_lop = update_ma_lop_var.get()
    ngay_bat_dau = update_ngay_bat_dau_var.get_date()
    ngay_ket_thuc = update_ngay_ket_thuc_var.get_date()
    hoc_phi = int(update_hoc_phi_var.get())
    so_buoi_hoc  = int(update_so_buoi_hoc_var.get())
    thu_2 = update_thu_2_var.get()
    thu_3 = update_thu_3_var.get()
    thu_4 = update_thu_4_var.get()
    thu_5 = update_thu_5_var.get()
    thu_6 = update_thu_6_var.get()
    thu_7 = update_thu_7_var.get()
    cn = update_cn_var.get()

    print(ngay_bat_dau)

    if (ho_ten == ""):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Họ tên")
        return
    if (ngay_bat_dau == ""):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Ngày bắt đầu")
        return
    if (so_buoi_hoc == 0):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Số buổi học")
        return
    if (hoc_phi == 0):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Học phí")
        return
    if (ngay_ket_thuc == ""):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Ngày kết thúc")
        return    
    thu_hoc_cnt = thu_2 + thu_3 + thu_4 + thu_5 + thu_6 + thu_7 + cn
    if (thu_hoc_cnt == 0):
        messagebox.showinfo("Thông báo lỗi", "Bạn cần chọn Thứ học")
        return

    data = (
        ho_ten,
        ma_lop,
        ngay_bat_dau,
        ngay_ket_thuc,
        thu_2,
        thu_3,
        thu_4,
        thu_5,
        thu_6,
        thu_7,
        cn,
        so_buoi_hoc,
        hoc_phi,
        ngay_ket_thuc,
        student_id
    )

    sql = ''' UPDATE hocvien SET ho_ten= ?, ma_lop= ?, ngay_bat_dau= ?, ngay_ket_thuc= ?, thu_2= ?, thu_3= ?, thu_4= ?, 
    thu_5= ?, thu_6= ?, thu_7= ?, cn= ?, so_buoi_hoc= ?, hoc_phi = ?, ngay_ket_thuc = ? 
    WHERE id = ? '''
    
    conn = conn_db()
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    conn.close()
