array = []
x = 1
while x <= 10:
    v = float(input("Digite o valor: "))
    array.append(v)
    x += 1
    array.sort(reverse=True)
print(array)