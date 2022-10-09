l = []
for i in range(10):
    l.append(int(input("Nhập phần tử thứ {} của list: ".format(i + 1))))
print("Bạn đã nhập list: ")
print(l)
print("Độ dài list: ", len(l))

max = min = l[0]
for i in l:
    if (i > max):
        max = i
    if (i < min):
        min = i
print("max = ", max)
print("min = ", min)

print("Sort l: ")
l.sort()
print(l)

del l[2]
print(l)

del l