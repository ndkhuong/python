x = []
x.append(int(input("nhập hoành độ của x: ")))
x.append(int(input("nhập tung độ của x: ")))
while x[0] != 2 or x[1] != 4:
    key = input("nhập hướng đi của bạn: ")
    if (key == 's'):
        x[1] -= 1
    elif (key == 'w'):
        x[1] += 1
    elif (key == 'a'):
        x[0] -= 1
    elif (key == 'd'):
        x[0] += 1
    print("x = [{}, {}]".format(x[0], x[1]))
print("Bạn đã đến đích")
