texto = str(input("Digite o texto."))

if texto == texto[::-1]:
    print("É um palindromo.")
else:
    print("Não é um palindromo.")