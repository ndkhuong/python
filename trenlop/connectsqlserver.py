import pyodbc

print(pyodbc.drivers())

cn_str = ("Driver={ODBC Driver 17 for SQL Server};"
      "Server=DESKTOP-5CQEGAD;"
      "Database=acc;"
      "UID=user2;"
      "PWD=123456;"
    )

c = pyodbc.connect(cn_str)
c.cursor()
for row in c.execute("select * from taikhoan where username = 'khuong'"):
    print(row)
