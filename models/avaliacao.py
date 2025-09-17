class Avaliacao: 
    def __init__(self, id, idfilme, usuario, nota, comentario):
        self.id = id
        self.idfilme = idfilme
        self.usuario = usuario
        self.nota = nota
        self.comentario = comentario


    def to_dict(self):
            return {
                "id": self.id,
                "idfilme": self.idfilme,
                "usuario": self.usuario,
                "nota":  self.nota,
                "comenatario": self.comentario
            
            }
