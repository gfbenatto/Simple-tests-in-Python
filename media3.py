array = []
soma =0 
x =1
while x <=4:
    v = float(input("Digite a nota %d: " %x))
    array.append(v)
    soma += v
    x += 1
print("Notas: ", array)
print("Media: ", (soma/4))