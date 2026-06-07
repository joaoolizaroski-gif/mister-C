class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco - (self.preco * percentual / 100)


produto = Produto("Monitor", 100.0)

print(produto.desconto(10))