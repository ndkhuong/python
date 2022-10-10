l = [1, 2, 5, 3, 4, "8", "-5"]

#in list
for i in range(len(l)):
    print(l[i])

#chuyển sang kiểu int để tính min, max, sort
sum = 0
for i in range(len(l)):
    l[i] = int(l[i])
    sum += l[i]

print("len = {}, sum = {}, max = {}, min = {}".format(len(l), sum, max(l), min(l)))
l.sort()
print("sort: ", l)

del l[2]
print("del index 2: ", l)

#xoa toan bo list
del l