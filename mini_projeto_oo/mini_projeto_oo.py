class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.__nome = nome
        self.__matricula = matricula
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario >= 0:
            self.__salario = salario
        else:
            print("Salário inválido!")

    def calcular_salario(self):
        pass

    def exibir(self):
        print(
            f"Nome: {self.get_nome()} | "
            f"Matricula: {self.get_matricula()} | "
            f"Tipo: {self.__class__.__name__} | "
            f"Salario: R$ {self.calcular_salario():.2f}"
        )


class CLT(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def calcular_salario(self):
        return self.get_salario()


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, vendas):
        super().__init__(nome, matricula, salario)
        self.vendas = vendas

    def calcular_salario(self):
        return self.get_salario() + (self.vendas * 0.10)


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def calcular_salario(self):
        return self.get_salario() + 1500


func1 = CLT("Ana", "001", 3000)
func2 = Vendedor("Bruno", "002", 2000, 12000)
func3 = Gerente("Carla", "003", 5000)

funcionarios = [func1, func2, func3]

for funcionario in funcionarios:
    funcionario.exibir()