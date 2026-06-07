class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(
            f"Aluno: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula}"
        )


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(
            f"Professor: {self.nome} | Idade: {self.idade} | Salário: R$ {self.salario}"
        )


pessoas = [
    Aluno("João", 17, "2025001"),
    Professor("Maria", 35, 4500),
    Aluno("Ana", 16, "2025002"),
    Professor("Pedro", 42, 6000),
]

for pessoa in pessoas:
    pessoa.apresentar()