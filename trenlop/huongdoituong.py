class nhan_vien():
    def __init__(self, hoten, namsinh):
        self.hoten = hoten
        self.namsinh = namsinh
    def get_hoten(self):
        return self.hoten
nv = nhan_vien('Khuong', 1989)
print(nv.get_hoten())

class hcn():
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def chuvi(self):
        return 2 * (self.dai + self.rong)
    def dientich(self):
        return self.dai * self.rong

hcn = hcn(5, 10)
print(hcn.chuvi())
print(hcn.dientich())