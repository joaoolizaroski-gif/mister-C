from flask import Flask

app = Flask(__name__)

@app.route("/")
def bem_vindo():
    return "seja bem vindo(a)"

@app.route("/curso")
def curso():
    return "TÉCNICO EM DESEN. SISTEMAS"

@app.route("/escola")
def escola():
    return "CEEP PEDRO BOARETTO NETO - ensino médio integrado"

if __name__ == "__main__":
    app.run(debug=True)