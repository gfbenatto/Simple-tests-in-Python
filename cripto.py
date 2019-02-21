"""
Exchange vowels by '*' in a file.
"""

text = open('mensagem.txt')
out = open('cripto.txt', 'w')
for line in text.readlines():
    for letter in line:
        if letter in 'aeiou':
            out.write('*')
        else:
            out.write(letter)
text.close()
out.close()


    
