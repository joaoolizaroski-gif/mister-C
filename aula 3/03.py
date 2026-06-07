class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

        if self.velocidade < 0:
            self.velocidade = 0


carro = Carro("Fiat", "Uno")

carro.acelerar()
carro.acelerar()
carro.acelerar()

carro.frear()

print(carro.velocidade)