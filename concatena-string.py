texto = input("Digite o texto: ")
x = 0
troca = ""
while x < len(texto):
    if texto[x] in "aeiou":
        troca = troca + "*"
    else:
        troca = troca + texto[x]
    x += 1
print(troca)
    