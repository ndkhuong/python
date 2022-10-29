import mylib as lib

person1 = lib.Person("Duong Van A", 33, "Ho Chi Minh")
person1.hienthi()

print()
person2 = lib.Person("Duong Van B", 20, "Ha Noi")
person2.hienthi()

person2.tuoi = 30
person2.gioitinh = "Nam"
person2.hienthi()
print("Gioi tinh: ", person2.gioitinh)

print("kiem tra thuoc tinh cccd: ", hasattr(person2, "cccd"))
person2.cccd = "123123131231"
print("Ten class: ", person2.__class__.__name__)