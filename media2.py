array = []
x =1
while x <= 4:
    v = int(input("Digite a nota %d: " %x))
    array.append(v)
    x += 1
soma = 0
x = 0
while x <= 3:
    soma += array[x]
    x += 1

print("Notas: ", array)
print("Media: ", (soma/4))
