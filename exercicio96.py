def area(w, len):
    a = w * len
    print(f'Width is {w} Length is {len} and Area is {a} square meters')
    
    
#Programa principal
print('Controle de terrenos')
print('-' * 20)

width = float(input('Width: '))
length = float(input('Length: '))
area(width, length)
