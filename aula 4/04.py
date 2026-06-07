class Sensor:
    def __init__(self):
        self.__temperatura = 0

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Temperatura inválida")

    def status(self):
        if self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"


sensor = Sensor()

sensor.set_temperatura(25)
print(sensor.status())

sensor.set_temperatura(90)
print(sensor.status())

sensor.set_temperatura(130)
print(sensor.status())

sensor.set_temperatura(-10)
print(sensor.status())