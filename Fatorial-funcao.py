def factorial(fat):
    c = 1
    while fat > 0:
        c = c * fat
        fat -= 1
    print(c)

factorial(5)