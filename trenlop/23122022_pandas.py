import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')

#new_df = df.dropna() #tao bien file moi

#df.fillna(100, inplace=True) #thay doi na->100 truc tiep tren file dang mo

#df["Calories"].fillna(100, inplace=True) #thay doi na->100 truc tiep tren COT file dang mo

#x = df["Calories"].mean() #gia tri trung binh cot Calories
#df["Calories"].fillna(x, inplace=True)

#x = df["Calories"].median() #gia tri o Giua cot Calories
#df["Calories"].fillna(x, inplace=True)

#x = df["Calories"].mode()[0] #gia tri so xuat hien nhieu nhat trong cot Calories
#df["Calories"].fillna(x, inplace=True)
#print(x)

df.loc[4, 'Pulse'] = 108 #set value = 108 cho dong 4, cot Pulse

#duyet file
for x in df.index:
    if (df.loc[x, 'Duration'] > 100) :
        #df.loc[x, 'Duration'] = 100
        df.drop(x, inplace=True)

#print(df.duplicated().to_string()) #tim dong bi trung

#df.drop_duplicates(inplace=True) #bo dong bi trung

#df.plot()
#plt.show()
#print(df.to_string())

#ve duong thang tao boi 2 diem tuong ung x va y: 5, 5 va 10, 50
#x = np.array([5, 10])
#y = np.array([5, 50])
#plt.plot(x, y, 'o')
#plt.show()

#ve bieu do x = index, y = value vd 0,5  1,2  3,1
x = np.array([5, 2, 1, 4, 9])
plt.plot(x, marker="o") #cac diem se co hinh dau cham "o"
plt.show()