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
    