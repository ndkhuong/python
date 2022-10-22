import random as rd
import os
import mylib

xVua = rd.randrange(0, 5)
yVua = rd.randrange(0, 5)
xTot = int(input("nhap xTot: "))
yTot = int(input("nhap yTot: "))
mylib.ve_ban_co(xTot, yTot, xVua, yVua)

while (xTot != xVua or yTot != yVua):
    #di chuyen Tot va ve lai ban co
    xTot, yTot = mylib.di_chuyen(xTot, yTot, 'Tot')
    os.system('cls')
    mylib.ve_ban_co(xTot, yTot, xVua, yVua)

    #di chuyen Vua va ve lai ban co
    xVua, yVua = mylib.di_chuyen(xVua, yVua, 'Vua')
    os.system('cls')
    mylib.ve_ban_co(xTot, yTot, xVua, yVua)
print("Chien thang")