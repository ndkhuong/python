t = (11, 3, 5, 19, 23, 100, 90, 88, 71, 65)
print("Bạn đã nhập tuple: ")
print(t)
print("Độ dài tuple: ", len(t))

sum = 0
for i in t:
    sum += i
print("len = ", len(t))
print("sum = ", sum)
print("max = ", max(t))
print("min = ", min(t))

del t