from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkcalendar import DateEntry
from datetime import datetime, timedelta

#exec file: $ pyinstaller --hidden-import babel.numbers filename.py

class quan_ly_hoc_vien():
    def __init__(self, root, window_width, window_height):
        self.root = root
        self.window_width = window_width
        self.window_height = window_height
        self.ngay_bat_dau_var = ""
        self.tree = {}
        self.ho_ten_var = StringVar(master=self.root)
        self.ma_lop_var = StringVar(master=self.root)
        self.hoc_phi_var = IntVar(master=self.root)
        self.so_buoi_hoc_var = IntVar(master=self.root)
        self.thu_2_var = IntVar(master=self.root)
        self.thu_3_var = IntVar(master=self.root)
        self.thu_4_var = IntVar(master=self.root)
        self.thu_5_var = IntVar(master=self.root)
        self.thu_6_var = IntVar(master=self.root)
        self.thu_7_var = IntVar(master=self.root)
        self.cn_var = IntVar(master=self.root)

    def conn_db(self):
        conn = sqlite3.connect("quanly_hocvien_new.db") 
        return conn

    def create_table(self):
        conn = self.conn_db()
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
                    ngay_cap_nhat date NULL,
                    da_dong_hoc_phi tinyint(1) DEFAULT 0);''')
        conn.close()

    def get_add_form(self):
        global ngay_bat_dau_var
        add_form  =  Frame(self.root,  width=self.window_width,  height=  200)
        add_form.grid(row=0,  column=0,  padx=10,  pady=5, sticky='wn')
        
        ROW = 0
        Label(add_form,  text="Họ tên").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
        Entry(add_form, textvariable=self.ho_ten_var).grid(row=ROW,  column=1,  padx=5,  pady=5)
        
        Label(add_form,  text="Mã lớp").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
        Entry(add_form, textvariable=self.ma_lop_var).grid(row=ROW,  column=3,  padx=5,  pady=5)
        
        ROW = 1
        today = datetime.today()
        Label(add_form,  text="Ngày bắt đầu").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
        self.ngay_bat_dau_var = DateEntry(add_form, width=17,date_pattern='yyyy-mm-dd' , selectmode='day', year = today.year, month = today.month, day = today.day)
        self.ngay_bat_dau_var.grid(row=ROW,  column=1,  padx=5,  pady=5)

        Label(add_form,  text="Số buổi học").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
        Entry(add_form, textvariable=self.so_buoi_hoc_var).grid(row=ROW,  column=3,  padx=5,  pady=5)
        
        ROW = 2
        Label(add_form,  text="Học phí").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
        Entry(add_form, textvariable=self.hoc_phi_var).grid(row=ROW,  column=1,  padx=5,  pady=5)
        
        ROW = 3
        thu_form  =  Frame(add_form,  width=window_width,  height=  60)
        thu_form.grid(row=ROW,  column=0,  padx=0,  pady=5, columnspan=4, sticky=W)

        Label(thu_form,  text="Thứ học").grid(row=0,  column=0,  padx=5,  pady=5, sticky=W, columnspan=7)
        Checkbutton(thu_form, text="Thứ 2", variable=self.thu_2_var, onvalue=1, offvalue=0).grid(row=1,  column=0,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 3", variable=self.thu_3_var, onvalue=1, offvalue=0).grid(row=1,  column=1,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 4", variable=self.thu_4_var, onvalue=1, offvalue=0).grid(row=1,  column=2,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 5", variable=self.thu_5_var, onvalue=1, offvalue=0).grid(row=1,  column=3,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 6", variable=self.thu_6_var, onvalue=1, offvalue=0).grid(row=1,  column=4,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 7", variable=self.thu_7_var, onvalue=1, offvalue=0).grid(row=1,  column=5,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Chủ nhật", variable=self.cn_var, onvalue=1, offvalue=0).grid(row=1,  column=6,  padx=5,  pady=5)

        ROW = 4
        btn_tool  =  Frame(add_form,  width=window_width,  height=  60)
        btn_tool.grid(row=ROW,  column=0,  padx=0,  pady=5, columnspan=4, sticky=W)

        Button(btn_tool,  text="Thêm học viên", command=lambda: self.add_new_student()).grid(row=ROW,  column=0,  padx=5,  pady=5, ipadx=10, sticky=W)
        Button(btn_tool,  text="Tìm kiếm", command=lambda: self.find_student()).grid(row=ROW,  column=1,  padx=5,  pady=5, ipadx=10, sticky=W)
        Button(btn_tool,  text="Tất cả", command=lambda: self.refresh_list()).grid(row=ROW,  column=2,  padx=5,  pady=5, ipadx=10, sticky=W)
        Button(btn_tool,  text="Sắp hết khóa", command=lambda: self.end_course()).grid(row=ROW,  column=3,  padx=5,  pady=5, ipadx=10, sticky=W)

    def get_list_student(self, search={}):
        if isinstance(self.tree, ttk.Treeview):
            self.tree.delete(*self.tree.get_children())

        ROW = 1
        list_student_frame  =  Frame(self.root,  width=self.window_width,  height=  300)
        list_student_frame.grid(row=ROW,  column=0,  padx=10,  pady=5)

        #extended = can select multi row
        #browse = can only select single row
        self.tree = ttk.Treeview(list_student_frame, height=15, selectmode="browse", column=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), show='headings')
        
        col = 1
        self.tree.heading("#" + str(col), text="STT")
        self.tree.column("#" + str(col), minwidth=0, width=30, stretch=NO, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="ID")
        self.tree.column("#" + str(col), minwidth=0, width=30, stretch=NO, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="Họ tên")
        self.tree.column("#" + str(col), minwidth=0, width=160, stretch=NO, anchor=W)

        col += 1
        self.tree.heading("#" + str(col), text="Mã lớp")
        self.tree.column("#" + str(col), minwidth=0, width=100, stretch=NO, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="Ngày bắt đầu")
        self.tree.column("#" + str(col), minwidth=0, width=90, stretch=NO, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="Ngày kết thúc")
        self.tree.column("#" + str(col), minwidth=0, width=95, stretch=NO, anchor=CENTER)
        
        col += 1
        self.tree.heading("#" + str(col), text="Số buổi học")
        self.tree.column("#" + str(col), minwidth=0, width=80, stretch=NO, anchor=CENTER)
        
        col += 1
        self.tree.heading("#" + str(col), text="Thứ học")
        self.tree.column("#" + str(col), minwidth=0, width=120, stretch=NO, anchor=CENTER)
        
        col += 1
        self.tree.heading("#" + str(col), text="Học phí")
        self.tree.column("#" + str(col), minwidth=0, width=100, stretch=NO, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="Tình trạng")
        self.tree.column("#" + str(col), minwidth=0, width=100, stretch=NO, anchor=CENTER)
        
        data_bind = []
        sql = "SELECT * FROM hocvien"
        conds = ""
        if ("ho_ten" in search and search["ho_ten"] != ""):
            conds += " AND ho_ten LIKE ?"
            data_bind.append('%' + search["ho_ten"] + '%')

        if ("end_course" in search and search["end_course"] == 1):
            today = datetime.today()
            curr_year = today.year
            curr_month = today.month
            if (curr_month < 10):
                curr_month = '0' + str(curr_month)
            conds += " AND ngay_ket_thuc LIKE ?"
            data_bind.append(str(curr_year) + '-' + str(curr_month) + '%')

        if (conds != ""):
            sql += " WHERE" + conds.lstrip(" AND")
        sql += " ORDER BY ngay_cap_nhat DESC"

        conn = self.conn_db()
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
            thu_hoc = self.get_thu_hoc(row)
            if (row["tinh_trang"] == 1):
                tinh_trang = "Đang học"
            else:
                tinh_trang = "Nghỉ"

            if (row["da_dong_hoc_phi"] == 1):
                hp = " (Rồi)"
            else:
                hp = ""

            data = (
                stt,
                row["id"],
                row["ho_ten"],
                row["ma_lop"],
                row["ngay_bat_dau"],
                row["ngay_ket_thuc"],
                row["so_buoi_hoc"],
                thu_hoc,
                '{:,d}'.format(row["hoc_phi"]).replace(',','.') + hp,
                tinh_trang,
            )
            self.tree.insert("", END, values=data)
        conn.close()

        self.tree.grid(row=0,  column=0,  padx=5,  pady=5, sticky=W)
        
        # add a scrollbar
        scrollbar = ttk.Scrollbar(list_student_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        sum = '{:,d}'.format(sum).replace(',','.')
        Label(list_student_frame, font=("Arial", 10),  text="Tổng học phí: " + str(sum)).grid(row=1,  column=0,  padx=5,  pady=5, sticky=W)

    def get_thu_hoc(self, row):
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

    def add_new_student(self):
        ho_ten = self.ho_ten_var.get()
        ma_lop = self.ma_lop_var.get()
        ngay_bat_dau = self.ngay_bat_dau_var.get_date()
        hoc_phi = int(self.hoc_phi_var.get())
        so_buoi_hoc  = int(self.so_buoi_hoc_var.get())
        thu_2 = self.thu_2_var.get()
        thu_3 = self.thu_3_var.get()
        thu_4 = self.thu_4_var.get()
        thu_5 = self.thu_5_var.get()
        thu_6 = self.thu_6_var.get()
        thu_7 = self.thu_7_var.get()
        cn = self.cn_var.get()

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

        ngay_ket_thuc = self.get_ngay_ket_thuc(ngay_bat_dau, so_buoi_hoc, thu_2, thu_3, thu_4, thu_5, thu_6, thu_7, cn)
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
        
        conn = self.conn_db()
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        conn.close()

        self.get_list_student()
        return cur.lastrowid

    def get_ngay_ket_thuc(self, ngay_bat_dau, so_buoi_hoc, thu_2, thu_3, thu_4, thu_5, thu_6, thu_7, cn):
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

    def refresh_list(self):   
        self.ho_ten_var.set('')
        self.ma_lop_var.set('')
        self.so_buoi_hoc_var.set(0)
        self.hoc_phi_var.set(0)
        self.thu_2_var.set(0)
        self.thu_3_var.set(0)
        self.thu_4_var.set(0)
        self.thu_5_var.set(0)
        self.thu_6_var.set(0)
        self.thu_7_var.set(0)
        self.cn_var.set(0)
        return self.get_list_student()
    
    def end_course(self):
        search = {}
        search["end_course"] = 1
        return self.get_list_student(search)

    def find_student(self):
        search = {}
        ho_ten = self.ho_ten_var.get()
        if (ho_ten != ''):
            search["ho_ten"] = ho_ten
        return self.get_list_student(search)

    def item_selected(self, event): 
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            id = item['values'][1]
        self.show_update_form(id)

    def show_update_form(self, student_id):
        self.popup_width = 510
        self.popup_height = 250

        self.popup = Toplevel(self.root) #make new popup is top level
        self.popup.grab_set() #root window is freeze now
        self.popup.wm_title("CẬP NHẬT THÔNG TIN HỌC VIÊN")

        # get screen width and height
        ws = self.popup.winfo_screenwidth() # width of the screen
        hs = self.popup.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (self.popup_width/2)
        y = (hs/2) - (self.popup_height/2) - 100
        self.popup.geometry('%dx%d+%d+%d' % (self.popup_width, self.popup_height, x, y))

        self.popup.minsize(self.popup_width, self.popup_height)
        self.popup.maxsize(self.popup_width, self.popup_height)

        self.get_update_form(student_id)

        self.popup.mainloop()

    def get_update_form(self, student_id):
        sql = '''SELECT * FROM hocvien WHERE id = ?'''
        conn = self.conn_db()
        conn.row_factory = sqlite3.Row #alert that we want to get key: value
        cur = conn.cursor()
        cur.execute(sql, [student_id])
        data = dict(cur.fetchone())

        add_form  =  Frame(self.popup,  width=self.popup_width,  height=  200)
        add_form.grid(row=0,  column=0,  padx=10,  pady=5, sticky='w' + 'n')
        
        ROW = 0
        self.update_ho_ten_var = StringVar(master=self.popup, value=data["ho_ten"])
        Label(add_form,  text="Họ tên").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_ho_ten_var).grid(row=ROW,  column=1,  padx=5,  pady=5)
        
        self.update_ma_lop_var = StringVar(master=self.popup, value=data["ma_lop"])
        Label(add_form,  text="Mã lớp").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_ma_lop_var).grid(row=ROW,  column=3,  padx=5,  pady=5)
        
        ROW = 1
        self.ngay_bat_dau = datetime.strptime(data["ngay_bat_dau"], '%Y-%m-%d')
        Label(add_form,  text="Ngày bắt đầu").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
        self.update_ngay_bat_dau_var = DateEntry(add_form, width=17,date_pattern='yyyy-mm-dd' , selectmode='day', year = self.ngay_bat_dau.year, month = self.ngay_bat_dau.month, day = self.ngay_bat_dau.day)
        self.update_ngay_bat_dau_var.grid(row=ROW,  column=1,  padx=5,  pady=5)

        self.update_so_buoi_hoc_var = StringVar(master=self.popup, value=data["so_buoi_hoc"])
        Label(add_form,  text="Số buổi học").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_so_buoi_hoc_var).grid(row=ROW,  column=3,  padx=5,  pady=5)
        
        ROW = 2
        self.update_hoc_phi_var = StringVar(master=self.popup, value=data["hoc_phi"])
        Label(add_form,  text="Học phí").grid(row=ROW,  column=0,  padx=5,  pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_hoc_phi_var).grid(row=ROW,  column=1,  padx=5,  pady=5)
        
        self.ngay_ket_thuc = datetime.strptime(data["ngay_ket_thuc"], '%Y-%m-%d')
        Label(add_form,  text="Ngày kết thúc").grid(row=ROW,  column=2,  padx=5,  pady=5, sticky=W)
        self.update_ngay_ket_thuc_var = DateEntry(add_form, width=17,date_pattern='yyyy-mm-dd' , selectmode='day', year = self.ngay_ket_thuc.year, month = self.ngay_ket_thuc.month, day = self.ngay_ket_thuc.day)
        self.update_ngay_ket_thuc_var.grid(row=ROW,  column=3,  padx=5,  pady=5)
        
        ROW = 3
        thu_form  =  Frame(add_form,  width=window_width,  height=  60)
        thu_form.grid(row=ROW,  column=0,  padx=0,  pady=3, columnspan=4, sticky=W)

        Label(thu_form,  text="Thứ học").grid(row=0,  column=0,  padx=5,  pady=0, sticky=W, columnspan=7)
        self.update_thu_2_var = IntVar(master=self.popup, value=data["thu_2"])
        self.update_thu_3_var = IntVar(master=self.popup, value=data["thu_3"])
        self.update_thu_4_var = IntVar(master=self.popup, value=data["thu_4"])
        self.update_thu_5_var = IntVar(master=self.popup, value=data["thu_5"])
        self.update_thu_6_var = IntVar(master=self.popup, value=data["thu_6"])
        self.update_thu_7_var = IntVar(master=self.popup, value=data["thu_7"])
        self.update_cn_var = IntVar(master=self.popup, value=data["cn"])
        Checkbutton(thu_form, text="Thứ 2", variable=self.update_thu_2_var, onvalue=1, offvalue=0).grid(row=1,  column=0,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 3", variable=self.update_thu_3_var, onvalue=1, offvalue=0).grid(row=1,  column=1,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 4", variable=self.update_thu_4_var, onvalue=1, offvalue=0).grid(row=1,  column=2,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 5", variable=self.update_thu_5_var, onvalue=1, offvalue=0).grid(row=1,  column=3,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 6", variable=self.update_thu_6_var, onvalue=1, offvalue=0).grid(row=1,  column=4,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Thứ 7", variable=self.update_thu_7_var, onvalue=1, offvalue=0).grid(row=1,  column=5,  padx=5,  pady=5)
        Checkbutton(thu_form, text="Chủ nhật", variable=self.update_cn_var, onvalue=1, offvalue=0).grid(row=1,  column=6,  padx=5,  pady=5)

        ROW = 4
        tinh_trang_form  =  Frame(add_form,  width=window_width,  height=  60)
        tinh_trang_form.grid(row=ROW,  column=0,  padx=0,  pady=0, columnspan=4, sticky=W)

        self.update_tinh_trang_var = IntVar(master=self.popup, value=data["tinh_trang"])
        self.update_da_dong_hoc_phi_var = IntVar(master=self.popup, value=data["da_dong_hoc_phi"])
        Checkbutton(tinh_trang_form, text="Đang học", variable=self.update_tinh_trang_var, onvalue=1, offvalue=0).grid(row=0,  column=0,  padx=5,  pady=5)
        Checkbutton(tinh_trang_form, text="Đã đóng HP", variable=self.update_da_dong_hoc_phi_var, onvalue=1, offvalue=0).grid(row=0,  column=1,  padx=5,  pady=5)

        ROW = 5
        btn_tool  =  Frame(add_form,  width=window_width,  height=  60)
        btn_tool.grid(row=ROW,  column=0,  padx=0,  pady=5, columnspan=4, sticky=E)

        Button(btn_tool,  text="Cập nhật", command=lambda: self.update_student(student_id)).grid(row=ROW,  column=0,  padx=5,  pady=5, ipadx=10, sticky=W)
        Button(btn_tool,  text="Xóa", padx=10, command=lambda: self.delete_student(student_id)).grid(row=ROW,  column=1,  padx=5,  pady=5, ipadx=10, sticky=W)

    def update_student(self, student_id):
        ho_ten = self.update_ho_ten_var.get()
        ma_lop = self.update_ma_lop_var.get()
        ngay_bat_dau = self.update_ngay_bat_dau_var.get_date()
        ngay_ket_thuc = self.update_ngay_ket_thuc_var.get_date()
        hoc_phi = int(self.update_hoc_phi_var.get())
        so_buoi_hoc  = int(self.update_so_buoi_hoc_var.get())
        thu_2 = self.update_thu_2_var.get()
        thu_3 = self.update_thu_3_var.get()
        thu_4 = self.update_thu_4_var.get()
        thu_5 = self.update_thu_5_var.get()
        thu_6 = self.update_thu_6_var.get()
        thu_7 = self.update_thu_7_var.get()
        cn = self.update_cn_var.get()
        tinh_trang = self.update_tinh_trang_var.get()
        da_dong_hoc_phi = self.update_da_dong_hoc_phi_var.get()

        if (ho_ten == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Họ tên")
            return
        if (ngay_bat_dau == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Ngày bắt đầu")
            return
        if (so_buoi_hoc == 0):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Số buổi học")
            return
        if (hoc_phi == 0):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Học phí")
            return
        if (ngay_ket_thuc == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Ngày kết thúc")
            return    
        thu_hoc_cnt = thu_2 + thu_3 + thu_4 + thu_5 + thu_6 + thu_7 + cn
        if (thu_hoc_cnt == 0):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần chọn Thứ học")
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
            tinh_trang,
            da_dong_hoc_phi,
            student_id
        )

        sql = ''' UPDATE hocvien SET ho_ten= ?, ma_lop= ?, ngay_bat_dau= ?, ngay_ket_thuc= ?, thu_2= ?, thu_3= ?, thu_4= ?, 
        thu_5= ?, thu_6= ?, thu_7= ?, cn= ?, so_buoi_hoc= ?, hoc_phi = ?, ngay_ket_thuc = ?, tinh_trang = ?, da_dong_hoc_phi = ? 
        WHERE id = ? '''
        
        conn = self.conn_db()
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        conn.close()

        self.popup.destroy()
        self.refresh_list()

    def delete_student(self, student_id):
        rs = messagebox.askyesno(parent=self.popup, title="Cảnh báo", message="Bạn có chắn muốn xóa học viên này?")
        if (rs == False):
            return

        sql = '''DELETE FROM hocvien WHERE id = ?'''
        conn = self.conn_db()
        conn.row_factory = sqlite3.Row #alert that we want to get key: value
        cur = conn.cursor()
        cur.execute(sql, [student_id])
        conn.commit()

        self.popup.destroy()
        self.refresh_list()


#####################################################################
window_width = 930
window_height = 630

root  =  Tk()  # create root window
root.title("QUẢN LÝ HỌC VIÊN")

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (window_width/2)
y = 50
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))
root.minsize(window_width, window_height)
root.maxsize(window_width, window_height)

ql = quan_ly_hoc_vien(root, window_width, window_height)
ql.create_table()
ql.get_add_form()
ql.get_list_student()

root.mainloop()