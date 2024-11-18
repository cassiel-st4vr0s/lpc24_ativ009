class Professor:
    def __init__(self, nome, idProfessor, departamentoId):
        self.nome = nome
        self.idProfessor = idProfessor
        self.departamentoId = departamentoId
        self.disciplinas = []
    
    def adicionarDisciplina(self, nome, id):
        from disciplina import Disciplina
        disc = Disciplina(nome, id, self.idProfessor)
        self.disciplinas.append(disc)
        return disc
    
    def deletarDisciplina(self, id):
        for disc in self.disciplinas:
            if disc.id == id:
                self.disciplinas.remove(disc)
                return True
        return False
    
    def listarDisciplinas(self):
        return self.disciplinas
