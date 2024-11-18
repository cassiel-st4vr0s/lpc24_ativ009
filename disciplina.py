class Disciplina:
    def __init__(self, nome, id, professorId):
        self.nome = nome
        self.id = id
        self.professorId = professorId
    
    def listarProfessores(self):
        return [self.professorId]