class Forma:
    def area(self):
        return 0


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


formas = [
    Triangulo(10, 5),
    Quadrado(4),
    Triangulo(8, 6),
    Quadrado(7)
]

for forma in formas:
    print(forma.area())