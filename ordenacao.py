array = []
x = 1
while x <= 10:
    v = float(input("Digite o valor %d: " %x))
    array.append(v)
    x += 1
x = 9
while x >= 0:
    print(array[x])
    x -= 1