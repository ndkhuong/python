import sqlite3

conn = sqlite3.connect("quanlyhaisan.db") #chua co thi se tu tao moi
conn.execute("DROP TABLE IF EXISTS haisan")
conn.execute('''CREATE TABLE haisan
            (ma INT PRIMARY KEY NOT NULL,
            ten            TEXT      NOT NULL,
            gia    INT  NOT NULL,
            diachi CHAR(50));''')
print('tao bang thanh cong')
conn.close()