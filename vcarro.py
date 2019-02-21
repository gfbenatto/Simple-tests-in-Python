v = int(input("Digite a velocidade do carro."))
if v > 110:
    m = 5 * (v - 110)
    print("Voce foi multado no valor de ", m)
else:
    print("Voce nao foi multado.")