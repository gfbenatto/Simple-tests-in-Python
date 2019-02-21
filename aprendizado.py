import string
file = open('alice.txt')
text = file.read()
text = text.lower()
for p in string.punctuation:
    text = text.replace(p, ' ') 
text = text.split()

dict = {}
for word in text:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

print('A palavra after aparece %s vezes no livro.' %dict['after']) 
file.close()