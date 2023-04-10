from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import sqlite3
from tkcalendar import DateEntry
from datetime import datetime
import os

#exec file: $ pyinstaller --hidden-import babel.numbers filename.py

class quan_ly_vat_tu():
    def __init__(self, root, window_width, window_height):
        self.root = root
        self.window_width = window_width
        self.window_height = window_height#active scrollbar
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.permission = {"master": 0, "add": 0, "edit": 0, "delete": 0, "export": 0, "import": 0}
        self.username_var = StringVar(master=self.root)
        self.password_var = StringVar(master=self.root)
        self.msp_var = StringVar(master=self.root)
        self.serial_var = StringVar(master=self.root)
        self.model_var = StringVar(master=self.root)
        self.nsx_var = StringVar(master=self.root)
        self.ngay_mua_var = ""
        self.gia_var = IntVar(master=self.root)
        self.hop_dong_var = StringVar(master=self.root)
        self.dia_phuong_var = StringVar(master=self.root)

    def conn_db(self):
        conn = sqlite3.connect("quan_ly_vat_tu.db") 
        return conn

    def query(self, sql, data_bind = []):
        conn = self.conn_db()
        conn.row_factory = sqlite3.Row #alert that we want to get key: value
        cur = conn.cursor()
        cur.execute(sql, data_bind)
        rows = [dict(row) for row in cur.fetchall()] #convert tup to dict
        conn.close()
        return rows
    
    def exe_query(self, sql, data_bind = []):
        conn = self.conn_db()
        cur = conn.cursor()
        cur.execute(sql, data_bind)
        conn.commit()
        conn.close()
        insert_id = 0
        if ("INSERT " in sql):
            insert_id = cur.lastrowid
        return insert_id

    def create_table(self):
        self.exe_query('''CREATE TABLE IF NOT EXISTS nha_san_xuat (
                    nsx_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nsx_ten varchar(300));''')
        self.insert_nsx()

        self.exe_query('''CREATE TABLE IF NOT EXISTS vat_tu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    msp varchar(100),
                    serial varchar(100) NULL,
                    model varchar(100) NULL,
                    nsx varchar(300) NULL,
                    ngay_mua date NULL,
                    gia int(11) NULL,
                    hop_dong varchar(300) NULL,
                    dia_phuong varchar(300) NULL);''')
        self.insert_product()
        
        self.exe_query('''CREATE TABLE IF NOT EXISTS admin (
                    `username` varchar(100) PRIMARY KEY,
                    `password` varchar(100) NULL,
                    `master` tinyint(1) DEFAULT 0,
                    `add` tinyint(1) DEFAULT 0,
                    `edit` tinyint(1) DEFAULT 0,
                    `delete` tinyint(1) DEFAULT 0,
                    `export` tinyint(1) DEFAULT 0,
                    `import` tinyint(1) DEFAULT 0);''')
        
        self.insert_master_admin()
        self.insert_admin('khuong', '123')
        self.insert_admin('khuong1', '123')
        self.insert_admin('khuong2', '123')
        self.insert_admin('khuong3', '123')
        self.insert_admin('khuong4', '123')
        self.insert_admin('khuong5', '123')
        self.insert_admin('khuong6', '123')
        self.insert_admin('khuong7', '123')
        self.insert_admin('khuong8', '123')
        self.insert_admin('khuong9', '123')
        self.insert_admin('khuong10', '123')

    def insert_nsx(self):
        sql = '''INSERT INTO nha_san_xuat (nsx_ten) VALUES 
        ('HUAWEI'), ('NOKIA'), ('Cisco'), ('NEC'), ('Siae Microelettronica'), ('JUNIPER'), ('ALCATEL'), ('DELTA'), 
        ('AGISSON'), ('EMERSON'), ('AEG'), ('ERICSSON'), ('ELTEK'), ('3Y Power Technology'), ('Fiber Home'), ('Grentech'), 
        ('SEAGATE'), ('BENNING'), ('Cherokee'), ('SAFT'), ('Sunnada'), ('ALU'), ('TỰ MUA SẮM'), ('ZTE'), ('HW'), ('ERA'), 
        ('HP'), ('CIENA'), ('HGST'), ('SOLID'), ('CERAGON'), ('FUJITSU'), ('SAMSUNG'), ('Tekelec'), ('VERTIV'), ('EATON'), 
        ('RAISECOM'), ('TOSHIBA'), ('Dynamic Power'), ('Rosenberger'), ('Super Stack'), ('Khác')'''
        self.exe_query(sql)

    def insert_product(self):
        sql = "SELECT msp FROM vat_tu LIMIT 1"
        rows = self.query(sql)
        if not rows:
            sql = '''INSERT INTO vat_tu (msp, serial, model, nsx, ngay_mua, gia, hop_dong, dia_phuong) VALUES
            ('MRFU 900', '2102310KBU10E2000438', 'BTS/ Node B', 'HUAWEI', '23/08/2022', '36966000', 'HĐ01', 'Đài viễn thông Nghệ An'),
            ('MRFU 900', '2102310KBU10E2000451', 'BTS/ Node B', 'HUAWEI', '23/08/2022', '15403000', 'HĐ02', 'Đài viễn thông Nghệ An'),
            ('MRFU 900', '2102310KBU10E2000637', 'BTS/ Node B', 'HUAWEI', '23/08/2022', '47070000', 'HĐ03', 'Đài viễn thông Nghệ An'),
            ('MRFU 900', '2102310KBU10D1002004', 'BTS/ Node B', 'HUAWEI', '23/08/2022', '33623000', 'HĐ04', 'Đài viễn thông Nghệ An'),
            ('MRFU 900', '2102310KBU10D2001045', 'BTS/ Node B', 'HUAWEI', '23/08/2022', '33656000', 'HĐ05', 'Đài viễn thông Nghệ An'),
            ('WRFU 2100', '21023192314MAB007867', 'BTS/ Node B', 'HUAWEI', '22/08/2022', '61817000', 'HĐ06', 'Đài viễn thông Vĩnh Phúc'),
            ('MRFU 900B', '2102310KBU10E2000564', 'BTS/ Node B', 'HUAWEI', '07/09/2022', '24701000', 'HĐ07', 'Đài viễn thông Hà Nội 2'),
            ('MRFU 1800', '2102310KBH10E4000770', 'BTS/ Node B', 'HUAWEI', '23/08/2022', '34419000', 'HĐ08', 'Đài viễn thông Nghệ An'),
            ('FXED', 'S1M201102929', 'BTS/ Node B', 'NOKIA', '22/08/2022', '63243000', 'HĐ09', 'Đài viễn thông Vĩnh Phúc'),
            ('R4850G', '2102312QTDLULC002714', 'Nguồn', 'HUAWEI', '23/08/2022', '81259000', 'HĐ10', 'Đài viễn thông Nghệ An'),
            ('Router Cisco ASR901', 'CAT2313U4G1', 'Truyền Dẫn', 'Cisco', '23/08/2022', '99061000', 'HĐ11', 'Đài viễn thông Nghệ An'),
            ('Router Cisco ASR901', 'CAT2313U1E9', 'Truyền Dẫn', 'Cisco', '23/08/2022', '62394000', 'HĐ12', 'Đài viễn thông Nghệ An'),
            ('Router Cisco ASR 920', 'FOC2502NK4Q', 'Truyền Dẫn', 'CISCO', '23/08/2022', '72910000', 'HĐ13', 'Đài viễn thông Nghệ An'),
            ('Router Cisco ASR901', 'CAT2304U13S', 'Truyền Dẫn', 'Cisco', '23/08/2022', '91907000', 'HĐ14', 'Đài viễn thông Nghệ An'),
            ('Router Cisco ASR 920', 'FOC2505NRN4', 'Truyền Dẫn', 'CISCO', '23/08/2022', '16497000', 'HĐ15', 'Đài viễn thông Nghệ An'),
            ('MRFU 900B', '2102310KBU10DA001230', 'BTS/ Node B', 'HUAWEI', '07/09/2022', '26703000', 'HĐ16', 'Đài viễn thông Hà Nội 2'),
            ('WRFU 2100', '21023192314MAB005934', 'BTS/ Node B', 'HUAWEI', '19/09/2022', '29771000', 'HĐ17', 'Đài viễn thông Vĩnh Phúc'),
            ('FXED', 'S1M170335362', 'BTS/ Node B', 'NOKIA', '07/09/2022', '29548000', 'HĐ18', 'Đài viễn thông Hà Nội 2'),
            ('FXED', 'S1M180907283', 'BTS/ Node B', 'NOKIA', '07/09/2022', '46674000', 'HĐ19', 'Đài viễn thông Hà Nội 2'),
            ('FXED', 'S1M180907037', 'BTS/ Node B', 'NOKIA', '07/09/2022', '1391000', 'HĐ20', 'Đài viễn thông Hà Nội 2'),
            ('FXED', 'S1M170808871', 'BTS/ Node B', 'NOKIA', '07/09/2022', '89496000', 'HĐ21', 'Đài viễn thông Hà Nội 1'),
            ('IDU VR4', '11111', 'Pasolink', 'NEC', '19/09/2022', '83760000', 'HĐ22', 'Đài viễn thông Hải Phòng'),
            ('WMPT', '020JQE6TB8601301', 'BTS/ Node B', 'HUAWEI', '19/09/2022', '33425000', 'HĐ23', 'Đài viễn thông Hải Phòng'),
            ('WMPT', '020JQE4M99170094', 'BTS/ Node B', 'HUAWEI', '19/09/2022', '50741000', 'HĐ24', 'Đài viễn thông Vĩnh Phúc'),
            ('ALCplus2e IDU', '1414273400100701D', 'Truyền Dẫn', 'Siae Microelettronica', '23/08/2022', '99756000', 'HĐ25', 'Đài viễn thông Nghệ An'),
            ('ALCplus2e IDU', '10165528900151D', 'Truyền Dẫn', 'Siae Microelettronica', '22/08/2022', '58378000', 'HĐ26', 'Đài viễn thông Vĩnh Phúc'),
            ('ASNK15', '10161852700020C', 'Truyền Dẫn', 'Siae Microelettronica', '08/08/2022', '46332000', 'HĐ27', 'Đài viễn thông Thái Nguyên'),
            ('ASN15', '01422325001320', 'Truyền Dẫn', 'Siae Microelettronica', '02/06/2022', '84149000', 'HĐ28', 'Đài viễn thông Vĩnh Phúc'),
            ('ACX1000', 'HT0219260357', 'Truyền Dẫn', 'JUNIPER', '08/08/2022', '32658000', 'HĐ29', 'Đài viễn thông Thái Nguyên'),
            ('ACX2100-DC', 'NK0216270362', 'Truyền Dẫn', 'JUNIPER', '07/09/2022', '78771000', 'HĐ30', 'Đài viễn thông Hà Nội 1')'''
            self.exe_query(sql)

    def insert_master_admin(self):
        sql = "SELECT username FROM admin WHERE username = 'root' LIMIT 1"
        rows = self.query(sql)
        if not rows:
            sql = "INSERT INTO admin (username, password, master) VALUES ('root', '123', 1)"
            self.exe_query(sql)

    def insert_admin(self, username, password):
        sql = "SELECT username FROM admin WHERE username = ? LIMIT 1"
        rows = self.query(sql, [username,])
        if not rows:
            sql = "INSERT INTO admin (username, password, master) VALUES (?, ?, 0)"
            self.exe_query(sql, [username, password])
            if username == 'khuong':
                sql = "UPDATE admin SET `add` = 1, `edit` = 1, `delete` = 1, `import` = 1, `export` = 1 WHERE username = 'khuong'"
                self.exe_query(sql)
    
    def get_login_form(self):
        self.login_form = Frame(self.root, width=self.window_width, height= 200)
        self.login_form.grid(row=0, column=0, padx=5, pady=5, sticky='ns')

        ROW = 0
        Label(self.login_form, text="Username").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(self.login_form, textvariable=self.username_var).grid(row=ROW, column=1, padx=5, pady=5)
        
        ROW = 1
        Label(self.login_form, text="Password").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(self.login_form, textvariable=self.password_var).grid(row=ROW, column=1, padx=5, pady=5)

        ROW = 2
        Button(self.login_form, text="Đăng nhập", command=lambda: self.check_login()).grid(row=ROW, column=1, padx=5, pady=5, ipadx=10, sticky=E)

    def check_login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        if (username == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Username")
            return
        if (password == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Password")
            return
        sql = "SELECT * FROM admin WHERE username = ? AND password = ? LIMIT 1"
        rows = self.query(sql, [username, password])
        if not rows:
            messagebox.showinfo("Thông báo lỗi", "Username hoặc Password không đúng")
            return
        else:
            self.permission = rows[0]
            self.login_form.destroy()
            self.get_add_form()
            self.get_list_product()
    
    def get_add_form(self):
        global ngay_bat_dau_var
        add_form = Frame(self.root)
        add_form.grid(row=0, column=0, padx=10, pady=5, sticky='wn')
        
        ROW = 0
        Label(add_form, text="Mã sản phẩm").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.msp_var).grid(row=ROW, column=1, padx=5, pady=5)
        
        Label(add_form, text="Serial").grid(row=ROW, column=2, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.serial_var).grid(row=ROW, column=3, padx=5, pady=5)
        
        ROW = 1
        Label(add_form, text="Model").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.model_var).grid(row=ROW, column=1, padx=5, pady=5)
        
        Label(add_form, text="Nhà sản xuất").grid(row=ROW, column=2, padx=5, pady=5, sticky=W)
        list_opt = self.get_list_nsx()
        field = ttk.OptionMenu(add_form, self.nsx_var, *list_opt)
        field.config(width=15)
        field.grid(row=ROW, column=3, padx=5, pady=5, sticky=W)

        ROW = 2
        today = datetime.today()
        Label(add_form, text="Ngày mua").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        self.ngay_mua_var = DateEntry(add_form, width=17,date_pattern='dd/mm/yyyy' , selectmode='day', year = today.year, month = today.month, day = today.day)
        self.ngay_mua_var.grid(row=ROW, column=1, padx=5, pady=5)

        Label(add_form, text="Giá").grid(row=ROW, column=2, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.gia_var).grid(row=ROW, column=3, padx=5, pady=5)
        
        ROW = 3
        Label(add_form, text="Hợp đồng").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.hop_dong_var).grid(row=ROW, column=1, padx=5, pady=5)

        Label(add_form, text="Địa phương").grid(row=ROW, column=2, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.dia_phuong_var).grid(row=ROW, column=3, padx=5, pady=5)
        
        ROW = 4
        btn_tool = Frame(add_form, width=window_width, height= 30)
        btn_tool.grid(row=ROW, column=0, padx=0, pady=5, columnspan=10, sticky=W)
        
        Button(btn_tool, text="Tất cả", command=lambda: self.refresh_list()).grid(row=ROW, column=0, padx=5, pady=5, ipadx=10, sticky=W)
        Button(btn_tool, text="Tìm kiếm", command=lambda: self.find_product()).grid(row=ROW, column=1, padx=5, pady=5, ipadx=10, sticky=W)
        if self.permission["master"] == 1 or self.permission["add"] == 1:
            Button(btn_tool, text="Thêm sản phẩm", command=lambda: self.add_new_product()).grid(row=ROW, column=2, padx=5, pady=5, ipadx=10, sticky=W)
        if self.permission["master"] == 1 or self.permission["export"] == 1:
            Button(btn_tool, text="Export CSV", command=lambda: self.export_product()).grid(row=ROW, column=3, padx=5, pady=5, ipadx=10, sticky=W)
        if self.permission["master"] == 1 or self.permission["import"] == 1:
            Button(btn_tool, text="Import CSV ", command=lambda: self.import_product()).grid(row=ROW, column=4, padx=5, pady=5, ipadx=10, sticky=W)
        if self.permission["master"] == 1:
            Button(btn_tool, text="Quản lý Admin", command=lambda: self.show_admin_form()).grid(row=ROW, column=5, padx=5, pady=5, ipadx=10, sticky=W)
    
    def get_list_nsx(self):
        sql = "SELECT * FROM nha_san_xuat"
        rows = self.query(sql)
        list_nsx = []
        for row in rows:
            list_nsx.append(row["nsx_ten"])
        return list_nsx

    def export_product(self):
        sql = "SELECT * FROM vat_tu"
        rows = self.query(sql)
        if not rows:
            messagebox.showinfo("Thông báo", "Không có dữ liệu")
            return

        userprofile = os.environ['USERPROFILE']
        file_path = os.path.join(userprofile, 'Downloads', '', 'QUAN_LY_VAT_TU.csv')
        with open(file_path, 'w', encoding="utf-8-sig") as file:
            file.write("Mã sản phẩm;Serial;Model;Nhà sản xuất;Ngày mua;Giá;Hợp đồng;Địa phương\n")
            for row in rows:
                string = str(row["msp"]) + ';'
                string += str(row["serial"]) + ';'
                string += str(row["model"]) + ';'
                string += str(row["nsx"]) + ';'
                string += str(row["ngay_mua"]) + ';'
                string += str(row["gia"]) + ';'
                string += str(row["hop_dong"]) + ';'
                string += str(row["dia_phuong"]) + "\n"
                file.write(string)
            file.close()
        file_path = os.path.join(userprofile, 'Downloads', '', '')
        os.startfile(file_path)

    def import_product(self):
        filename = filedialog.askopenfilename(filetypes=[("Text file", "*.csv")])
        with open(filename, 'r', encoding='utf-8-sig') as file:
            cnt = 0
            for row in file.readlines():
                if cnt == 0:
                    cnt = 1
                    continue
                row = row.rstrip('\n')
                row = row.split(";")
                print(row)
                sql = ''' INSERT INTO vat_tu (msp, serial, model, nsx, ngay_mua, gia, hop_dong, dia_phuong)
                VALUES(?,?,?,?,?,?,?,?) '''
                data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
                self.exe_query(sql, data)
            file.close()
        self.get_list_product()

    def show_admin_form(self):
        self.admin_popup_width = 500
        self.admin_popup_height = 400

        self.admin_popup = Toplevel(self.root) #make new popup is top level
        self.admin_popup.grab_set() #root window is freeze now
        self.admin_popup.wm_title("QUẢN LÝ ADMIN")

        # get screen width and height
        ws = self.admin_popup.winfo_screenwidth() # width of the screen
        hs = self.admin_popup.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (self.admin_popup_width/2)
        y = (hs/2) - (self.admin_popup_height/2) - 100
        self.admin_popup.geometry('%dx%d+%d+%d' % (self.admin_popup_width, self.admin_popup_height, x, y))

        self.admin_popup.minsize(self.admin_popup_width, self.admin_popup_height)
        self.admin_popup.maxsize(self.admin_popup_width, self.admin_popup_height)

        self.get_admin_form()
        self.get_list_admin()

        self.admin_popup.mainloop()

    def get_admin_form(self):
        self.admin_form = Frame(self.admin_popup)
        #self.admin_form = Frame(self.admin_popup, width=self.window_width, height=100, highlightbackground="grey", highlightthickness=1)
        self.admin_form.grid(row=0, column=0, padx=5, pady=5, sticky='wn')

        self.username_add_var = StringVar(master=self.admin_popup)
        self.password_add_var = StringVar(master=self.admin_popup)

        ROW = 0
        Label(self.admin_form, text="Username").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(self.admin_form, textvariable=self.username_add_var).grid(row=ROW, column=1, padx=5, pady=5)
        
        ROW = 1
        Label(self.admin_form, text="Password").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(self.admin_form, textvariable=self.password_add_var).grid(row=ROW, column=1, padx=5, pady=5)

        ROW = 2
        Button(self.admin_form, text="Thêm admin", command=lambda: self.add_admin()).grid(row=ROW, column=0, padx=5, pady=5, ipadx=10, sticky=W)

    def add_admin(self):
        username = self.username_add_var.get()
        password = self.password_add_var.get()
        if (username == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Username", parent=self.admin_form)
            return
        if (password == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Password", parent=self.admin_form)
            return
        sql = "SELECT username FROM admin WHERE username = ? LIMIT 1"
        rows = self.query(sql, [username,])
        if not rows:
            self.insert_admin(username, password)
            self.get_list_admin()
        else:
            messagebox.showinfo("Thông báo lỗi", "Username đã tồn tại", parent=self.admin_form)

    def get_list_admin(self):
        try:
            if isinstance(self.admin_tree, ttk.Treeview):
                self.admin_tree.delete(*self.admin_tree.get_children())
        except Exception:
            pass
        
        self.list_admin_form = Frame(self.admin_popup, width=self.window_width, height=100)
        self.list_admin_form.grid(row=1, column=0, padx=5, pady=5, sticky='wn')
                
        self.admin_tree = ttk.Treeview(self.list_admin_form, height=10, selectmode="browse", column=("0", "1"), show='headings')
        
        col = 1
        self.admin_tree.heading("#" + str(col), text="STT")
        self.admin_tree.column("#" + str(col), minwidth=0, width=50, stretch=False, anchor=CENTER)
        
        col += 1
        self.admin_tree.heading("#" + str(col), text="Username")
        self.admin_tree.column("#" + str(col), minwidth=0, width=100, stretch=False, anchor=CENTER)

        sql = "SELECT * FROM admin"
        rows = self.query(sql)
        stt = 0
        for row in rows:
            stt += 1
            #print(row) # it print all records in the database
            data = (
                stt,
                row["username"]
            )
            self.admin_tree.insert("", END, values=data)

        self.admin_tree.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.list_admin_form, orient=VERTICAL, command=self.admin_tree.yview)
        self.admin_tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        #active scrollbar
        self.list_admin_form.columnconfigure(0, weight=1)
        self.list_admin_form.rowconfigure(0, weight=1)

        self.admin_tree.bind('<<TreeviewSelect>>', self.admin_selected)

    def admin_selected(self, event): 
        for selected_item in self.admin_tree.selection():
            item = self.admin_tree.item(selected_item)
            username = item['values'][1]
        self.get_permission_form(username)

    def get_permission_form(self, username):
        try:
            self.permission_form.destroy()
        except Exception:
            pass

        self.permission_form = Frame(self.list_admin_form, bd=1, relief="sunken")
        self.permission_form.grid(row=0, column=2, padx=5, pady=5, sticky='wn')

        sql = "SELECT * FROM admin WHERE username = ?"
        row = self.query(sql, [username,])

        self.master_var = StringVar(master=self.admin_popup, value=row[0]["master"])
        self.add_var = StringVar(master=self.admin_popup, value=row[0]["add"])
        self.edit_var = StringVar(master=self.admin_popup, value=row[0]["edit"])
        self.delete_var = StringVar(master=self.admin_popup, value=row[0]["delete"])
        self.export_var = StringVar(master=self.admin_popup, value=row[0]["export"])
        self.import_var = StringVar(master=self.admin_popup, value=row[0]["import"])

        ROW = 0
        Label(self.permission_form, text="Username: " + username).grid(row=ROW, column=0, columnspan=5, padx=5, pady=5, sticky=W)
        
        ROW = 1
        cb = ttk.Checkbutton(self.permission_form, text="Master", variable=self.master_var, onvalue=1, offvalue=0, command=lambda: self.save_permission(username, 'master', self.master_var))
        cb.grid(row=ROW, column=0, padx=5, pady=5, sticky='w')
        cb = ttk.Checkbutton(self.permission_form, text="Thêm", variable=self.add_var, onvalue=1, offvalue=0, command=lambda: self.save_permission(username, 'add', self.add_var))
        cb.grid(row=ROW, column=1, padx=5, pady=5, sticky='w')
        cb = ttk.Checkbutton(self.permission_form, text="Sửa", variable=self.edit_var, onvalue=1, offvalue=0, command=lambda: self.save_permission(username, 'edit', self.edit_var))
        cb.grid(row=ROW, column=2, padx=5, pady=5, sticky='w')
        cb = ttk.Checkbutton(self.permission_form, text="Xóa", variable=self.delete_var, onvalue=1, offvalue=0, command=lambda: self.save_permission(username, 'delete', self.delete_var))
        cb.grid(row=ROW, column=3, padx=5, pady=5, sticky='w')

        ROW = 2
        cb = ttk.Checkbutton(self.permission_form, text="Xuất file", variable=self.export_var, onvalue=1, offvalue=0, command=lambda: self.save_permission(username, 'export', self.export_var))
        cb.grid(row=ROW, column=0, padx=5, pady=5, sticky='w')
        cb = ttk.Checkbutton(self.permission_form, text="Nhập file", variable=self.import_var, onvalue=1, offvalue=0, command=lambda: self.save_permission(username, 'import', self.import_var))
        cb.grid(row=ROW, column=1, padx=5, pady=5, sticky='w')

        ROW = 3        
        Button(self.permission_form, text="Xoá admin", command=lambda: self.delete_admin(username)).grid(row=ROW, column=0, padx=5, pady=5, ipadx=10, sticky=W)

    def save_permission(self, username, field, checkbox):
        val = checkbox.get()
        sql = "UPDATE admin SET `" + field + "`= ? WHERE username = ?"
        self.exe_query(sql, [val, username])
            
    def delete_admin(self, username):
        print(username)
        sql = "DELETE FROM admin WHERE username = ?"
        self.exe_query(sql, [username,])
        self.get_list_admin()
        try:
            self.permission_form.destroy()
        except Exception:
            pass

    def get_list_product(self, search={}):
        try:
            if isinstance(self.tree, ttk.Treeview):
                self.tree.delete(*self.tree.get_children())
        except Exception:
            pass
        
        ROW = 1
        list_student_frame = Frame(self.root)
        list_student_frame.grid(row=1, column=0, padx=10)

        #extended = can select multi row
        #browse = can only select single row
        self.tree = ttk.Treeview(list_student_frame, height=15, selectmode="browse", column=("0", "1", "2", "3", "4", "5", "6", "7", "8"), show='headings')
        
        col = 1
        self.tree.heading("#" + str(col), text="STT")
        self.tree.column("#" + str(col), minwidth=0, width=50, stretch=False, anchor=CENTER)
        
        col += 1
        self.tree.heading("#" + str(col), text="Mã sản phẩm")
        self.tree.column("#" + str(col), minwidth=0, width=150, stretch=False, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="Serial")
        self.tree.column("#" + str(col), minwidth=0, width=150, stretch=False, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="Model")
        self.tree.column("#" + str(col), minwidth=0, width=100, stretch=False, anchor=W)

        col += 1
        self.tree.heading("#" + str(col), text="Nhà sản xuất")
        self.tree.column("#" + str(col), minwidth=0, width=100, stretch=False, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="Ngày mua")
        self.tree.column("#" + str(col), minwidth=0, width=100, stretch=False, anchor=CENTER)

        col += 1
        self.tree.heading("#" + str(col), text="Giá")
        self.tree.column("#" + str(col), minwidth=0, width=100, stretch=False, anchor=CENTER)
        
        col += 1
        self.tree.heading("#" + str(col), text="Hợp đồng")
        self.tree.column("#" + str(col), minwidth=0, width=100, stretch=False, anchor=CENTER)
        
        col += 1
        self.tree.heading("#" + str(col), text="Địa phương")
        self.tree.column("#" + str(col), minwidth=0, width=200, stretch=False, anchor=CENTER)
                
        data_bind = []
        sql = "SELECT * FROM vat_tu"
        conds = ""
        if ("msp" in search and search["msp"] != ""):
            conds += " AND msp = ?"
            data_bind.append(search["msp"])
        if ("serial" in search and search["serial"] != ""):
            conds += " AND serial = ?"
            data_bind.append(search["serial"])
        if ("model" in search and search["model"] != ""):
            conds += " AND model = ?"
            data_bind.append(search["model"])
        if ("nsx" in search and search["nsx"] != ""):
            conds += " AND nsx = ?"
            data_bind.append(search["nsx"])
        if ("gia" in search and search["gia"] != "" and search["gia"] > 0):
            conds += " AND gia = ?"
            data_bind.append(search["gia"])
        if ("hop_dong" in search and search["hop_dong"] != ""):
            conds += " AND hop_dong = ?"
            data_bind.append(search["hop_dong"])
        if ("dia_phuong" in search and search["dia_phuong"] != ""):
            conds += " AND dia_phuong = ?"
            data_bind.append(search["dia_phuong"])

        if (conds != ""):
            sql += " WHERE " + conds.lstrip(" AND")
        rows = self.query(sql, data_bind)

        for row in rows:
            data = (
                row["id"],
                row["msp"],
                row["serial"],
                row["model"],
                row["nsx"],
                row["ngay_mua"],
                '{:,d}'.format(row["gia"]).replace(',','.'),
                row["hop_dong"],
                row["dia_phuong"]
            )
            self.tree.insert("", END, values=data)

        self.tree.grid(row=0, column=0, padx=5, pady=5)
        
        # add a scrollbar
        scrollbar = ttk.Scrollbar(list_student_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        treeXScroll = ttk.Scrollbar(list_student_frame, orient=HORIZONTAL)
        treeXScroll.configure(command=self.tree.xview)
        self.tree.configure(xscrollcommand=treeXScroll.set)
        treeXScroll.grid(row=1, column=0, sticky='we')
        
        #active scrollbar
        list_student_frame.columnconfigure(0, weight=1)
        list_student_frame.rowconfigure(0, weight=1)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

    def add_new_product(self):
        msp = self.msp_var.get()
        serial = self.serial_var.get()
        model = self.model_var.get()
        nsx = self.nsx_var.get()
        ngay_mua = self.ngay_mua_var.get_date()
        gia = int(self.gia_var.get())
        hop_dong = self.hop_dong_var.get()
        dia_phuong = self.dia_phuong_var.get()

        if (msp == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Mã sản phẩm")
            return
        if (serial == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Serial")
            return
        if (model == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Model")
            return
        if (nsx == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Nhà sản xuất")
            return
        if (ngay_mua == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Ngày mua")
            return
        if (gia == "" or gia == 0):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Giá")
            return
        if (hop_dong == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Hợp đồng")
            return
        if (dia_phuong == ""):
            messagebox.showinfo("Thông báo lỗi", "Bạn cần nhập Địa phương")
            return
        
        sql = ''' INSERT INTO vat_tu (msp, serial, model, nsx, ngay_mua, gia, hop_dong, dia_phuong)
                VALUES(?,?,?,?,?,?,?,?) '''
        data = [msp, serial, model, nsx, ngay_mua, gia, hop_dong, dia_phuong]
        insert_id = self.exe_query(sql, data)

        self.get_list_product()
        return insert_id

    def refresh_list(self):   
        self.msp_var.set('')
        self.model_var.set('')
        self.serial_var.set('')
        self.nsx_var.set('')
        self.gia_var.set(0)
        self.hop_dong_var.set('')
        self.dia_phuong_var.set('')
        return self.get_list_product()

    def find_product(self):
        search = {}
        msp = self.msp_var.get()
        serial = self.serial_var.get()
        model = self.model_var.get()
        nsx = self.nsx_var.get()
        ngay_mua = self.ngay_mua_var.get_date()
        gia = int(self.gia_var.get())
        hop_dong = self.hop_dong_var.get()
        dia_phuong = self.dia_phuong_var.get()
        if (msp != ''):
            search["msp"] = msp
        if (serial != ''):
            search["serial"] = serial
        if (model != ''):
            search["model"] = model
        if (nsx != ''):
            search["nsx"] = nsx
        if (ngay_mua != ''):
            search["ngay_mua"] = ngay_mua
        if (gia != ''):
            search["gia"] = gia
        if (hop_dong != ''):
            search["hop_dong"] = hop_dong
        if (dia_phuong != ''):
            search["dia_phuong"] = dia_phuong
        return self.get_list_product(search)

    def item_selected(self, event): 
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            id = item['values'][0]
        self.show_update_form(id)

    def show_update_form(self, id):
        self.popup_width = 500
        self.popup_height = 180

        self.popup = Toplevel(self.root) #make new popup is top level
        self.popup.grab_set() #root window is freeze now
        self.popup.wm_title("CẬP NHẬT THÔNG TIN SẢN PHẨM")

        # get screen width and height
        ws = self.popup.winfo_screenwidth() # width of the screen
        hs = self.popup.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (self.popup_width/2)
        y = (hs/2) - (self.popup_height/2) - 100
        self.popup.geometry('%dx%d+%d+%d' % (self.popup_width, self.popup_height, x, y))

        self.popup.minsize(self.popup_width, self.popup_height)
        self.popup.maxsize(self.popup_width, self.popup_height)

        self.get_update_form(id)

        self.popup.mainloop()

    def get_update_form(self, id):
        sql = '''SELECT * FROM vat_tu WHERE id = ?'''
        data = self.query(sql, [id])
        data = data[0]

        add_form = Frame(self.popup)
        add_form.grid(row=0, column=0, padx=10, pady=5, sticky='wn')
        
        ROW = 0
        self.update_msp_var = StringVar(master=self.popup, value=data["msp"])
        Label(add_form, text="Mã sản phẩm").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_msp_var).grid(row=ROW, column=1, padx=5, pady=5)
        
        self.update_serial_var = StringVar(master=self.popup, value=data["serial"])
        Label(add_form, text="Serial").grid(row=ROW, column=2, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_serial_var).grid(row=ROW, column=3, padx=5, pady=5)
        
        ROW = 1
        self.update_model_var = StringVar(master=self.popup, value=data["model"])
        Label(add_form, text="Model").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_model_var).grid(row=ROW, column=1, padx=5, pady=5)
        
        self.update_nsx_var = StringVar(master=self.popup)
        Label(add_form, text="Nhà sản xuất").grid(row=ROW, column=2, padx=5, pady=5, sticky=W)
        list_opt = self.get_list_nsx()
        field = ttk.OptionMenu(add_form, self.update_nsx_var, *list_opt)
        self.update_nsx_var.set(data["nsx"])
        field.config(width=15)
        field.grid(row=ROW, column=3, padx=5, pady=5)
        
        ROW = 2
        ngay_mua = datetime.strptime(data["ngay_mua"], '%d/%m/%Y')
        Label(add_form, text="Ngày mua").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        self.update_ngay_mua_var = DateEntry(add_form, width=17,date_pattern='dd/mm/yyyy' , selectmode='day', year = ngay_mua.year, month = ngay_mua.month, day = ngay_mua.day)
        self.update_ngay_mua_var.grid(row=ROW, column=1, padx=5, pady=5)

        self.update_gia_var = IntVar(master=self.popup, value=data["gia"])
        Label(add_form, text="Giá").grid(row=ROW, column=2, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_gia_var).grid(row=ROW, column=3, padx=5, pady=5)
        
        ROW = 3
        self.update_hop_dong_var = StringVar(master=self.popup, value=data["hop_dong"])
        Label(add_form, text="Hợp đồng").grid(row=ROW, column=0, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_hop_dong_var).grid(row=ROW, column=1, padx=5, pady=5)
        
        self.update_dia_phuong_var = StringVar(master=self.popup, value=data["dia_phuong"])
        Label(add_form, text="Địa phương").grid(row=ROW, column=2, padx=5, pady=5, sticky=W)
        Entry(add_form, textvariable=self.update_dia_phuong_var).grid(row=ROW, column=3, padx=5, pady=5)
        
        ROW = 5
        btn_tool = Frame(add_form)
        btn_tool.grid(row=ROW, column=0, padx=0, pady=5, columnspan=4, sticky=E)
        
        if self.permission["master"] == 1 or self.permission["edit"] == 1:
            Button(btn_tool, text="Cập nhật", command=lambda: self.update_product(id)).grid(row=ROW, column=0, padx=5, pady=5, ipadx=10, sticky=W)
        if self.permission["master"] == 1 or self.permission["delete"] == 1:
            Button(btn_tool, text="Xóa", padx=10, command=lambda: self.delete_product(id)).grid(row=ROW, column=1, padx=5, pady=5, ipadx=10, sticky=W)
                   
    def update_product(self, id):
        msp = self.update_msp_var.get()
        serial = self.update_serial_var.get()
        model = self.update_model_var.get()
        nsx = self.update_nsx_var.get()
        ngay_mua = self.update_ngay_mua_var.get_date()
        gia = self.update_gia_var.get()
        hop_dong = self.update_hop_dong_var.get()
        dia_phuong = self.update_dia_phuong_var.get()

        if (msp == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Mã sản phẩm")
            return
        if (serial == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Serial")
            return
        if (model == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Ngày bắt Model")
            return
        if (nsx == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Nhà sản xuất")
            return
        if (ngay_mua == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Ngày mua")
            return    
        if (gia == 0 or gia == ""): 
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Giá")
            return
        if (hop_dong == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Hợp đồng")
            return
        if (dia_phuong == ""):
            messagebox.showinfo(parent=self.popup, title="Thông báo lỗi", message="Bạn cần nhập Địa phương")
            return
        
        data = (
            msp,
            serial,
            model,
            nsx,
            ngay_mua,
            gia,
            hop_dong,
            dia_phuong,
            id
        )

        sql = ''' UPDATE vat_tu SET 
        msp = ?,
        serial = ?,
        model = ?,
        nsx = ?,
        ngay_mua = ?,
        gia = ?,
        hop_dong = ?,
        dia_phuong = ?
        WHERE id = ? '''
        
        self.exe_query(sql, data)
        self.popup.destroy()
        self.refresh_list()

    def delete_product(self, id):
        rs = messagebox.askyesno(parent=self.popup, title="Cảnh báo", message="Bạn có chắn muốn xóa sản phẩm này?")
        if (rs == False):
            return

        sql = '''DELETE FROM vat_tu WHERE msp = ?'''
        self.exe_query(sql, [id])

        self.popup.destroy()
        self.refresh_list()


#####################################################################
window_width = 650
window_height = 550

root = Tk()  # create root window
root.title("QUẢN LÝ VẬT TƯ")

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (window_width/2)
y = 50
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))
#root.minsize(window_width, window_height)
#root.maxsize(window_width, window_height)

ql = quan_ly_vat_tu(root, window_width, window_height)
ql.create_table()
#ql.get_login_form()
#ql.show_admin_form()
ql.get_add_form()
ql.get_list_product()

root.mainloop()