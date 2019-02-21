valor = float(input("Qual o valor por hora: "))
hora = float(input("Quantidade de horas trabalhasdas no mês: "))

bruto = valor * hora
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind

print("Salario Bruto = R$ %.2f " %bruto)
print("IR = R$ %.2f" %ir)
print("INSS = R$ %.2f" %inss)
print("Sindicato = R$ %.2f" %sind)
print("Liquido = R$ %10.2f" %liquido)