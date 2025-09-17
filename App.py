from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from routes.avaliacao_routes import avaliacao_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(avaliacao_routes)

#Base de filmes (mock)
filmes = [
    {"id": 1, "titulo": "Matrix", "genero": "Ficção Científica"},
    {"id": 2, "titulo": "Titanic", "genero": "Romance"},
]

@app.route("/")
def home():
    filmes_completo = [
        {
            "titulo": "Matrix",
            "descricao": "Um hacker descobre a verdade sobre sua realidade...",
            "poster": "https://link-para-o-poster.jpg",
            "avaliacoes": 120
        },
        {
            "titulo": "Titanic",
            "descricao": "Romance épico no navio mais famoso da história...",
            "poster": "https://link-para-o-poster2.jpg",
            "avaliacoes": 95
        }
    ]
    return render_template("filmes.html", filmes=filmes_completo)

#Listar todos os filmes
@app.route("/filmes", methods=["GET"])
def listar_filmes():
    return jsonify(filmes)

#Buscar filme por ID
@app.route("/filmes/<int:id>", methods=["GET"])
def buscar_filme(id):
    for filme in filmes:
        if filme["id"] == id:
            return jsonify(filme)
    return jsonify({"erro": "Filme não encontrado"}), 404

#Criar novo filme
@app.route("/filmes", methods=["POST"])
def criar_filme():
    dados = request.get_json()
    novo_id = max([f["id"] for f in filmes]) + 1 if filmes else 1
    filme = {
        "id": novo_id,
        "titulo": dados.get("titulo"),
        "genero": dados.get("genero"),
    }
    filmes.append(filme)
    return jsonify({"mensagem": "Filme criado com sucesso!", "filme": filme}), 201

#Atualizar filme existente
@app.route("/filmes/<int:id>", methods=["PUT"])
def atualizar_filme(id):
    dados = request.get_json()
    for filme in filmes:
        if filme["id"] == id:
            filme["titulo"] = dados.get("titulo", filme["titulo"])
            filme["genero"] = dados.get("genero", filme["genero"])
            return jsonify({"mensagem": "Filme atualizado com sucesso!", "filme": filme})
    return jsonify({"erro": "Filme não encontrado"}), 404

#Deletar filme
@app.route("/filmes/<int:id>", methods=["DELETE"])
def deletar_filme(id):
    for i, filme in enumerate(filmes):
        if filme["id"] == id:
            del filmes[i]
            return jsonify({"mensagem": "Filme deletado com sucesso!"})
    return jsonify({"erro": "Filme não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
