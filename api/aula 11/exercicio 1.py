import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL
)
""")

cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Caderno", 15.50))
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Caneta", 3.20))
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Mochila", 120.00))

conexao.commit()
conexao.close()