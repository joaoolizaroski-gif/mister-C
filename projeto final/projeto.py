from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Autor(db.Model):
    __tablename__ = "autores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nacionalidade = db.Column(db.String(50), nullable=True)

    livros = db.relationship("Livro", backref="autor", cascade="all, delete-orphan", passive_deletes=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nacionalidade": self.nacionalidade,
        }

class Livro(db.Model):
    __tablename__ = "livros"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    ano_publicacao = db.Column(db.Integer, nullable=True)
    
    autor_id = db.Column(db.Integer, db.ForeignKey("autores.id", ondelete="CASCADE"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "ano_publicacao": self.ano_publicacao,
            "autor_id": self.autor_id,
        }

with app.app_context():
    db.create_all()

@app.route("/autores", methods=["POST"])
def criar_autor():
    dados = request.get_json()
    if not dados or "nome" not in dados:
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

    novo_autor = Autor(
        nome=dados["nome"],
        nacionalidade=dados.get("nacionalidade")
    )
    db.session.add(novo_autor)
    db.session.commit()

    return jsonify(novo_autor.to_dict()), 201

@app.route("/autores", methods=["GET"])
def listar_autores():
    autores = Autor.query.all()
    return jsonify([a.to_dict() for a in autores]), 200

@app.route("/autores/<int:id>", methods=["GET"])
def obter_autor(id):
    autor = db.session.get(Autor, id)
    if not autor:
        return jsonify({"erro": "Autor não encontrado"}), 404
    return jsonify(autor.to_dict()), 200

@app.route("/autores/<int:id>", methods=["PUT"])
def atualizar_autor(id):
    autor = db.session.get(Autor, id)
    if not autor:
        return jsonify({"erro": "Autor não encontrado"}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados para atualização inválidos"}), 400

    autor.nome = dados.get("nome", autor.nome)
    autor.nacionalidade = dados.get("nacionalidade", autor.nacionalidade)

    db.session.commit()
    return jsonify(autor.to_dict()), 200

@app.route("/autores/<int:id>", methods=["DELETE"])
def deletar_autor(id):
    autor = db.session.get(Autor, id)
    if not autor:
        return jsonify({"erro": "Autor não encontrado"}), 404

    db.session.delete(autor)
    db.session.commit()
    return jsonify({"mensagem": "Autor excluído com sucesso"}), 200

@app.route("/livros", methods=["POST"])
def criar_livro():
    dados = request.get_json()
    if not dados or "titulo" not in dados or "autor_id" not in dados:
        return jsonify({"erro": "Campos 'titulo' e 'autor_id' são obrigatórios"}), 400

    autor = db.session.get(Autor, dados["autor_id"])
    if not autor:
        return jsonify({"erro": "Autor não encontrado"}), 404

    novo_livro = Livro(
        titulo=dados["titulo"],
        ano_publicacao=dados.get("ano_publicacao"),
        autor_id=dados["autor_id"]
    )
    db.session.add(novo_livro)
    db.session.commit()

    return jsonify(novo_livro.to_dict()), 201

@app.route("/livros", methods=["GET"])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([l.to_dict() for l in livros]), 200

@app.route("/livros/<int:id>", methods=["GET"])
def obter_livro(id):
    livro = db.session.get(Livro, id)
    if not livro:
        return jsonify({"erro": "Livro não achado"}), 404
    return jsonify(livro.to_dict()), 200

@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    livro = db.session.get(Livro, id)
    if not livro:
        return jsonify({"erro": "Livro não foi achado"}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dadoss inválidos"}), 400

    if "autor_id" in dados:
        autor = db.session.get(Autor, dados["autor_id"])
        if not autor:
            return jsonify({"erro": "Novo autor fornecido não existe"}), 404
        livro.autor_id = dados["autor_id"]

    livro.titulo = dados.get("titulo", livro.titulo)
    livro.ano_publicacao = dados.get("ano_publicacao", livro.ano_publicacao)

    db.session.commit()
    return jsonify(livro.to_dict()), 200

@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    livro = db.session.get(Livro, id)
    if not livro:
        return jsonify({"erro": "Livro não foi achado"}), 404

    db.session.delete(livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro excluído com suesso"}), 200

@app.route("/livros/detalhes", methods=["GET"])
def listar_livros_com_autor():
    resultados = db.session.query(Livro, Autor.nome).join(Autor, Livro.autor_id == Autor.id, isouter=True).all()
    
    resposta = []
    for livro, nome_autor in resultados:
        resposta.append({
            "id": livro.id,
            "titulo": livro.titulo,
            "ano_publicacao": livro.ano_publicacao,
            "autor_id": livro.autor_id,
            "nome_autor": nome_autor
        })
    
    return jsonify(resposta), 200

@app.route("/autores/<int:autor_id>/livros", methods=["GET"])
def listar_livros_por_autor(autor_id):
    autor = db.session.get(Autor, autor_id)
    if not autor:
        return jsonify({"erro": "Autor não encontrado"}), 404

    livros = Livro.query.filter_by(autor_id=autor_id).all()
    return jsonify([l.to_dict() for l in livros]), 200

@app.route("/livros/busca", methods=["GET"])
def buscar_livros():
    termo_titulo = request.args.get("titulo")
    termo_ano = request.args.get("ano")

    consulta = Livro.query

    if termo_titulo:
        consulta = consulta.filter(Livro.titulo.ilike(f"%{termo_titulo}%"))
    if termo_ano:
        consulta = consulta.filter(Livro.ano_publicacao == termo_ano)

    livros = consulta.all()
    return jsonify([l.to_dict() for l in livros]), 200

if __name__ == "__main__":
    app.run(debug=True)