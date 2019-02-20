import random
"""
Get a string and return scrambled.
"""

def shuffles(word):
    list1 = list(word)
    random.shuffle(list1)
    return ''.join(list1)


print(shuffles('scrambled'))
