file = open('surf.txt')
point = []
names = []
file = open('surf.txt')
score = {}

for line in file:
    name, points = line.split()
    score[float(points)] = name
file.close()

for s in sorted(score, reverse=True):
    print('%s te nota %4.2f' %(score[s], s))