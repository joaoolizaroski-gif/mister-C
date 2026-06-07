class Instrumento:
    def tocar(self):
        print("Som genérico")


class Violao(Instrumento):
    def tocar(self):
        print("Plim plim")


class Bateria(Instrumento):
    def tocar(self):
        print("Tum tum")


class Piano(Instrumento):
    def tocar(self):
        print("Dó Ré Mi")


instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()