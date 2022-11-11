'''BT OOP: tạo class có tên TruongThuySon với các thuộc tính: VuKhi, Tuoi. 
1. Phương thức info in ra thông tin các thuộc tính 
2. Gọi 2 đối tượng và truyền các giá trị thuộc tính nhập vào từ bàn phím TTS1, TTS2
3. Tạo class con TruongVoKy kế thừa class TruongThuySon thêm thuộc tính level 
và phương thức riêng là infoTruongVoKy – 
phương thức này in ra các thuộc tính kế thừa class cha và thuộc tính level'''

class TruongThuySon():
    VuKhi = ""
    Tuoi = 0
    def __init__(self, VuKhi, Tuoi):
        self.VuKhi = VuKhi
        self.Tuoi = Tuoi
    def info(self):
        print("Vu khi: ", self.VuKhi)
        print("Tuoi: ", self.Tuoi)

class TruongVoKy(TruongThuySon):
    def __init__(self, VuKhi, Tuoi, Lev):
        super().__init__(VuKhi, Tuoi)
        self.Lev = Lev
    def infoTruongVoKy(self):
        print("Vu khi: ", self.VuKhi)
        print("Tuoi: ", self.Tuoi)
        print("Lev: ", self.Lev)



