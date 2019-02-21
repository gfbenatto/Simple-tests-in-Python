array = []
x = 1
while x <= 10:
    cont = 1
    v = int(input("Digite o valor %d: " %x))
    array.append(v)
    while cont <= 10:
        array.sort(reverse=True)
        cont += 1
    x += 1
print("Lista reversa é: ", array)