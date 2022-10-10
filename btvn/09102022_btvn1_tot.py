def nhap_toa_do(name):
    diem = []
    diem.append(int(input("Nhập hoành độ x của {}: ".format(name))))
    diem.append(int(input("Nhập tung độ y của {}: ".format(name))))
    return diem

def di_chuyen(tot):
    key = input("Nhập hướng đi của tốt (a: lùi, d: tới, w: lên, s: xuống): ")
    if (key == 'a'):
        tot[0] -= 1
    elif (key == 'd'):
        tot[0] += 1
    elif (key == 's'):
        tot[1] -= 1
    elif (key == 'w'):
        tot[1] += 1
    print("vị trí của tốt: ", tot)
    return tot

#############################################

vua = nhap_toa_do("vua")
tot = nhap_toa_do("tot")
print("vị trí của vua: ", vua)
print("vị trí của tốt: ", tot)

while (tot[0] != vua[0] or tot[1] != vua[1]):
    di_chuyen(tot)
print("Bạn đã đến đích")


