"""
This program ask a value between 0 and 10,
and show a message if de value are invalid and keep showing until user inform a valid value.
 
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.
 """

nota = int(input("Digite uma nota entre 0 e 10: "))
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    if nota not in array:
       nota = int(input("Digite uma nota entre 0 e 10: "))
    else:
        print(nota)
        break