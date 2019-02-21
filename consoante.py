array = []
x = 1
while x <= 10:
    v = str(input("Digite a letra %d:" %x))
    array.append(v)
    x += 1
x = 0
cont = 0
while x <= 9:
    if array[x] not in "aeiou":
       cont += 1
    x += 1
print(cont)