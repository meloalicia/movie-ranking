from flask import Blueprint, jsonify, render_template, request
from flask_cors import CORS
from services.avaliacao_service import listar_avaliacoes, criar_avaliacao, atualizar_avaliacao, buscar_avaliacao, deletar_avaliacao 

avaliacao_routes = Blueprint("avaliacao_routes", __name__)

#Listar todas as avaliações de um filme
@avaliacao_routes.route("/avaliacao/<int:idfilme>", methods=["GET"])
def listar_todas_avaliacoes(idfilme):
    avaliacoes = listar_avaliacoes(idfilme)
    return jsonify(avaliacoes)

#Trazer os dados de UMA avaliação
@avaliacao_routes.route("/avaliacao/avaliacao/<int:id>", methods=["GET"])
def trazer_dados_avaliacao(id):
    avaliacao = buscar_avaliacao(id)
    return jsonify(avaliacao)

#Salvar nova avaliação
@avaliacao_routes.route("/avaliacao/avaliacao", methods=["POST"])
def salvar_avaliacao():
    dados = request.get_json()
    idfilme = dados.get("idfilme")
    usuario = dados.get("usuario")
    nota = dados.get("nota")
    comentario = dados.get("comentario")
    
    criar_avaliacao(idfilme, usuario, nota, comentario)
    return jsonify({"mensagem": "Avaliação criada com sucesso!"})

# 4. Alterar uma avaliação
@avaliacao_routes.route("/avaliacao/avaliacao", methods=["PUT"])
def alterar_avaliacao():
    dados = request.get_json()
    id = dados.get("id")
    nota = dados.get("nota")
    comentario = dados.get("comentario")
    
    atualizar_avaliacao(id, nota, comentario)
    return jsonify({"mensagem": "Avaliação alterada com sucesso!"})

#Excluir uma avaliação
@avaliacao_routes.route("/avaliacao/avaliacao/<int:id>", methods=["DELETE"])
def remover_avaliacao(id):
    deletar_avaliacao(id)
    return jsonify({"mensagem": "Avaliação removida com sucesso!"})
