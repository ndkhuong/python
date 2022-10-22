import mylib

n = 5
print("{}! = ".format(n), mylib.giai_thua(n))

a = 10
b = 5
print("{} + {} = ".format(a, b), mylib.cong(a, b))
print("{} - {} = ".format(a, b), mylib.tru(a, b))
print("{} * {} = ".format(a, b), mylib.nhan(a, b))
print("{} / {} = ".format(a, b), mylib.chia(a, b))

#hinh thoi
d1 = 10 #duong cheo 1
d2 = 15 #duong cheo 2
print("Dien tich hinh thoi co 2 duong cheo d1 = {} va d2 = {}: ".format(d1, d2), mylib.s_hinh_thoi(d1, d2))

#hinh vuong
a = 100
print("Dien tich hinh vuong co canh = {}: ".format(a), mylib.s_hinh_vuong(a))
