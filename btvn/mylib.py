
class TruongThuySon():
    vukhi = ''
    tuoi = 0
    def __init__(self, vukhi, tuoi):
        self.vukhi = vukhi
        self.tuoi = tuoi
    def info(self):
        print('Vu khi: ', self.vukhi)
        print('Tuoi: ', self.tuoi)

class TruongVoKy(TruongThuySon):
    lev = 0
    def __init__(self, vukhi, tuoi, lev):
        super().__init__(vukhi, tuoi)
        self.lev = lev
    def infoTruongVoKy(self):
        self.info()
        print("Level: ", self.lev)

class NhanVat():
    def __init__(self, ten, tuoi, monphai, lev):
        self.ten = ten
        self.tuoi = tuoi
        self.monphai = monphai
        self.lev = lev
    def info(self):
        print("Ten: {}, Tuoi: {}, Mon phai: {}, Level: {}".format(self.ten, self.tuoi, self.monphai, self.lev))

def in_list_nv(list_nv):
    for nv in list_nv:
        nv.info()

def tim_nv_max_lev(list_nv):
    nv_max = list_nv[0]
    for nv in list_nv:
        if nv.lev > nv_max.lev:
            nv_max = nv
    nv_max.info()
    return nv_max

def tim_nv_min_lev(list_nv):
    nv_min = list_nv[0]
    for nv in list_nv:
        if nv.lev < nv_min.lev:
            nv_min = nv
    nv_min.info()
    return nv_min

def sap_xep_lev_tang(list_nv):
    for i in range(len(list_nv)):
        for j in range(len(list_nv) - i - 1):
            if (list_nv[j].lev > list_nv[j+1].lev):
                temp = list_nv[j]
                list_nv[j] = list_nv[j+1]
                list_nv[j+1] = temp
    in_list_nv(list_nv)
    return list_nv

def sap_xep_lev_giam(list_nv):
    for i in range(len(list_nv)):
        for j in range(len(list_nv) - i - 1):
            if (list_nv[j].lev < list_nv[j+1].lev):
                temp = list_nv[j]
                list_nv[j] = list_nv[j+1]
                list_nv[j+1] = temp
    in_list_nv(list_nv)
    return list_nv

def tim_nv_lev_lon_hon_5(list_nv):
    for nv in list_nv:
        if (nv.lev > 5):
            nv.info()

def tim_nv_monphai_vovinam(list_nv):
    for nv in list_nv:
        if (nv.monphai == 'VoViNam'):
            nv.info()

def nhap_x():
    retry = True
    while (retry == True):
        try:
            x = int(input("Nhap so thu tu cua chuc nang: "))
            if (x < 2 or x > 7):
                print("Vui long nhap so 2 - 7")
                retry = True
            else:
                retry = False
        except ValueError:
            print("Vui long nhap so")
            retry = True
    return x



import math
class dien_tich():
    s = 0
    def in_s(self):
        print("Dien tich: {:.2f}".format(self.s))
        
    def s_hbh(self):
        print("Tinh dien tich hinh binh hanh")
        a = int(input("Nhap do dai canh day: "))
        h = int(input("Nhap do dai chieu cao: "))
        self.s = a * h
        self.in_s()
        return self.s
        
    def s_hinhtru(self):
        print("Tinh dien tich hinh tru")
        r = int(input("Nhap do dai ban kinh: "))
        h = int(input("Nhap do dai chieu cao: "))
        self.s = 2*3.14*r*r + 2*3.14*r*h
        self.in_s()
        return self.s
        
    def s_hinhthoi(self):
        print("Tinh dien tich hinh thoi")
        d1 = int(input("Nhap do dai duong cheo 1: "))
        d2 = int(input("Nhap do dai duong cheo 2: "))
        self.s = 0.5 * d1 * d2
        self.in_s()
        return self.s
        
    def s_ngugiac(self):
        print("Tinh dien tich hinh ngu giac deu")
        c = int(input("Nhap do dai canh: "))
        self.s = 5*c*c/(4*math.sqrt(5 - 2*math.sqrt(5)))
        self.in_s()
        return self.s




def ve_ban_co(xTot, yTot, xVua, yVua):
    m = 6
    n = 6
    a = []
    for i in range(m):
        b = []
        for j in range(n):
            b.append(0)
        a.append(b)
    
    a[xVua][yVua] = 1
    a[xTot][yTot] = 2

    for i in range(m):
        for j in range(n):
            if (a[i][j] == 1):
                print('▲', end='')
            elif (a[i][j] == 2):
                print('●', end='')
            else: 
                print('□', end='')
        print('')

def di_chuyen(i, j, name):
    key = input("nhap huong di cua {} (a: lui, d: toi, s: xuong, w: len): ".format(name))
    if (key == 'w'):
        i -= 1
    elif (key == 's'):
        i += 1
    elif (key == 'a'):
        j -= 1
    elif (key == 'd'):
        j += 1
    return (i, j)


#ham tinh toan
def giai_thua(n):
    if (n == 0):
        return 1
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s
    
def cong(a, b):
    return a + b
    
def tru(a, b):
    return a - b
    
def nhan(a, b):
    return a * b
    
def chia(a, b):
    return a / b
    
def s_hinh_thoi(d1, d2):
    return 0.5 * d1 * d2
    
def s_hinh_vuong(a):
    return a * a


    