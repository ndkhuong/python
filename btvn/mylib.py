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