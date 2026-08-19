from flask import Flask
from datetime import date

app = Flask(__name__)
@app.route("/saudacao")
def saudacao():
    return "Olá! Seja muito bem-vindo à nossa API."
@app.route("/data")
def data_de_hoje():
    hoje = date.today()
    return f"A data de hoje é: {hoje}"
if __name__ == "__main__":
    app.run(debug=True)