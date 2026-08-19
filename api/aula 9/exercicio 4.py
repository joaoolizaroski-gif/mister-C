from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00, "disponivel": True},
    {"id": 2, "nome": "Mouse sem fio", "preco": 89.90, "disponivel": True},
    {"id": 3, "nome": "Teclado Mecânico", "preco": 250.00, "disponivel": False},
    {"id": 4, "nome": "Monitor 24 polegadas", "preco": 750.00, "disponivel": True}
]

@app.route("/produtos/disponiveis")
def produtos_disponiveis():
    lista_disponiveis = []
    
    # Filtra os produtos disponíveis
    for produto in produtos:
        if produto["disponivel"] == True:
            lista_disponiveis.append(produto)
            
    return jsonify(lista_disponiveis)

if __name__ == "__main__":
    app.run(debug=True)