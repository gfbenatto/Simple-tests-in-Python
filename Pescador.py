peso = float(input("Digite o peso dos peixes: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("Multa de R$ %.2f" %multa)
    print("Excesso de %.2f" %excesso)
else:
    excesso = 0
    print("Excesso de peso em %.2f" %excesso)