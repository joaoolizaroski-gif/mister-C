class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto1 = Produto("Mouse", 50.0)
produto2 = Produto("Teclado", 120.0)

print(produto1.nome, produto1.preco)
print(produto2.nome, produto2.preco)