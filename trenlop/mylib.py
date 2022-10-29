def cong(a, b):
    return a+b
def tru(a, b):
    return a-b
def nhan(a, b):
    return a*b
def chia(a, b):
    return a/b

class Person():
    ten = ""
    tuoi = 0
    diachi = ""
    def __init__(self, ten, tuoi, diachi):
        self.ten = ten
        self.tuoi = tuoi
        self.diachi = diachi
    def hienthi(self):
        print("Ten: ", self.ten)
        print("Tuoi: ", self.tuoi)
        print("Dia chi: ", self.diachi)

