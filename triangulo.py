a = int(input("Digite o lado a."))
b = int(input("Digite o lado b."))
c = int(input("Digite o lado c."))

if a > b + c or b > a + c or c > a + b:
    print("Nao pode ser um triangulo")
    print("Um lado não pode ser maior que a soma dos outros dois lados.")
elif a == b == c:
    print("Equilatero")
elif a != b != c:
    print("Escaleno")
else:
    print("Isoceles")