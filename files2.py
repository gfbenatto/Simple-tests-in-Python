file = open('numeros.txt', 'r')
for line in file.readlines():
    print(line.rstrip())
file.close()