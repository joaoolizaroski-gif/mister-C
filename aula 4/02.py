class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = ""
        self.__idade = 0

        self.set_nome(nome)
        self.set_idade(idade)

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("Nome inválido")

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            print("Idade inválida")

    def apresentar(self):
        print("Nome:", self.__nome)
        print("Idade:", self.__idade)


pessoa = Pessoa("João", 18)
pessoa.apresentar()