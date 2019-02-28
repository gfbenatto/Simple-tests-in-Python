file = open('surf.txt')
score = []
for line in file:
    name, points = line.split()
    print(line)
    score.append(float(points))

file.close()
score.sort()
score.reverse()

print(score[0])
print(score[1])
print(score[3])