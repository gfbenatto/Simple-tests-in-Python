def change(text):
    swap = ""
    for letter in text:
        if letter in "aeiou":
            swap = swap + "*"
        else:
            swap = swap + letter
    return swap


t = input('Digite um texto: ')
result = change(t)
print(result)
