import random

list1 = []
while len(list1) < 15:
    x = random.randint(10, 100)
    if x not in list1:
        list1.append(x)
list1.sort()
print(list1)