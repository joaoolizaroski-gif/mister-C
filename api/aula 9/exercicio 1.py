from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produto")
def produto():
    dados_produto = {
        "id": 1,
        "nome": "Caderno Esperto",
        "preco": 45.90,
        "disponivel": True
    }
    return jsonify(dados_produto)

if __name__ == "__main__":
    app.run(debug=True)