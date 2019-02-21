file = open('numeros2.txt', 'w')
for line in range(1, 38):
    file.write('%d' %line)
file.close()