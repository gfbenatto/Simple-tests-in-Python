metros = float(input("Entre co o valor e metros quadrados: "))

if metros % 54 == 0:
    latas = metros/54
else:
    latas = int(metros/54) + 1
valor = latas * 80
print("Latas = %.2f" %latas)
print("Valor = %.2f" %valor)