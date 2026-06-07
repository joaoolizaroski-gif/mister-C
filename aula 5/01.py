class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo")


class Cachorro(Animal):
    def latir(self):
        print("Au au!")


cachorro = Cachorro("Rex")

cachorro.comer()
cachorro.latir()