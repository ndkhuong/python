from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import mysql.connector as mysql

root = Tk()
root.geometry("600x500")
root.title("part Manager")
#Label
pn=Label(root,text='Part Name', font=('f',10))
pn.place(x=20,y=30)
retailer=Label(root,text='Retailer', font=('f',10))
retailer.place(x=20,y=60)
customer=Label(root,text='Customer', font=('f',10))
customer.place(x=300,y=30)
price=Label(root,text='Price', font=('f',10))
price.place(x=300,y=60)

#Entry
e_pn=Entry()
e_pn.place(x=150,y=30)
e_retailer=Entry()
e_retailer.place(x=150,y=60)
e_customer=Entry()
e_customer.place(x=400,y=30)
e_price=Entry()
e_price.place(x=400,y=60)


def add():
    pn = e_pn.get()
    retailer = e_retailer.get()
    customer = e_customer.get()
    price = e_price.get()
    print(pn, retailer, customer, price)
    if (pn == "" or retailer == "" or customer == "" or price == "") :
        messagebox.showinfo("Add info", "Cần nhập thêm thông tin vào ô trống")
    else:
        conn = mysql.connect(host="localhost", user="root", database="tkinter")
        cursor = conn.cursor()

        sql = "INSERT INTO tkinter (pn, retailer, customer, price) VALUES (%s, %s, %s, %s)"
        val = (pn, retailer, customer, price)
        cursor.execute(sql, val)

        conn.commit()
        print(cursor.rowcount, "record inserted.")
        print("1 record inserted, ID:", cursor.lastrowid)

        #reset field
        e_pn.delete(0, 'end')
        e_retailer.delete(0, 'end')
        e_customer.delete(0, 'end')
        e_price.delete(0, 'end')

        messagebox.showinfo("add status", "Add thành công")

def show() :
    conn = mysql.connect(host="localhost", user="root", database="tkinter")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tkinter")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def remove():
    if (e_pn.get() == ""):
        messagebox.showinfo("remove thong tin", "Nhập thêm thông tin cần xóa")
    else:
        conn = mysql.connect(host="localhost", user="root", database="tkinter")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tkinter WHERE pn = %s", (e_pn.get(),)) #tub need at least two value
        cursor.execute("commit")
        conn.close()

        e_pn.delete(0, "end")


add_btn=Button(root,text='Add', font=('f',10), command=add)
add_btn.place(x=20,y=90)

show_btn=Button(root,text='Show', font=('f',10), command=show)
show_btn.place(x=60,y=90)

del_btn=Button(root,text='Delete', font=('f',10), command=remove)
del_btn.place(x=120,y=90)

root.mainloop()
