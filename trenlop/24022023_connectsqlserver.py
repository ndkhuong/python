import pyodbc

print(pyodbc.drivers())
#ten = input("moi ban nhap ten can tim:")
cn_str = ("Driver={ODBC Driver 17 for SQL Server};"
      "Server=DESKTOP-5CQEGAD;"
      "Database=hoc_sql;"
      "UID=user2;"
      "PWD=123456;"
    )
c = pyodbc.connect(cn_str)
c.cursor()
for row in c.execute("select STT,HV, _SDT, TRANGTHAI  from hocvien WHERE HV = N'Hồ Minh Thiệu'"):
    print(row)
