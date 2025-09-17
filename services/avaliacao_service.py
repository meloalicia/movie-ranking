from models.avaliacao import Avaliacao

base_avaliacao = [
    Avaliacao(1, 101, "João", 5, "Filme excelente!").to_dict(),
    Avaliacao(2, 101, "Maria", 4, "Gostei bastante, mas o final foi corrido.").to_dict(),
    Avaliacao(3, 102, "Ana", 3, "Mediano, esperava mais.").to_dict()
]

#Listar todas as avaliações
def listar_avaliacoes():
    return [avaliacao for avaliacao in base_avaliacao if int(avaliacao["idfilme"])]
    
#Buscar dados de uma avaliação específica
def buscar_avaliacao(id):
   return [avaliacao for avaliacao in base_avaliacao if int(avaliacao["id"]) == int(id)] 

#Criar uma avaliação
def criar_avaliacao(idfilme, usuario, nota, comentario):
    lista_ids = [avaliacao["id"] for avaliacao in base_avaliacao]
    ultimo_id = max(lista_ids) if lista_ids else 0
    
#atualizar avaliação
def atualizar_avaliacao(id, nota, comentario):
    for avaliacao in base_avaliacao:
        if int(avaliacao['id']) == int(id):
         avaliacao['nome'] = nota
         avaliacao['email'] = comentario

def deletar_avaliacao(id):
    for indice, avaliacao in enumerate(base_avaliacao):
        if int(avaliacao['id']) == int(id):
            del base_avaliacao[indice]
            break  