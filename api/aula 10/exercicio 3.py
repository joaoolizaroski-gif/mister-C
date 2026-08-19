from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova_tarefa = request.get_json()
    
    if "titulo" not in nova_tarefa or nova_tarefa["titulo"] == "":
        return jsonify({"erro": "O titulo nao pode ser vazio"}), 400
        
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

if __name__ == "__main__":
    app.run(debug=True)