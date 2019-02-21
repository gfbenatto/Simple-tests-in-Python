notas = [7, 9, 4.2, 7.7, 10]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print("Media é %.2f: " % (soma/x))


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def full_name(self):
        return "{} {}".format(self.name, self.surname)

    def first_name(self):
        return self.name

    def get_surname(self)
        return self.surname
p = Person("Giovani", "Benatto")
print(f"meu nome eh {p.full_name()}")
