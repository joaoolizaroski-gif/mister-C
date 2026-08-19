from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    # Substitua "Seu Nome Completo" pelo seu nome verdadeiro
    return "Seu Nome Completo"

if __name__ == "__main__":
    app.run(debug=True)