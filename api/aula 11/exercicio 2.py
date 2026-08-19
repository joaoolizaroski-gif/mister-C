import sqlite3

conexao = sqlite3.connect("loja.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")
todos = cursor.fetchall()

for linha in todos:
    print(dict(linha))

conexao.close()