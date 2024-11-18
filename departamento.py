class Departamento:
    def __init__(self, nomeDepartamento, id, faculdadeId):
        self.nomeDepartamento = nomeDepartamento
        self.id = id
        self.faculdadeId = faculdadeId
        self.professores = []
    
    def adicionarProfessor(self, nome, idProfessor):
        from professor import Professor
        prof = Professor(nome, idProfessor, self.id)
        self.professores.append(prof)
        return prof
    
    def deletarProfessor(self, idProfessor):
        for prof in self.professores:
            if prof.idProfessor == idProfessor:
                # remover professor's subjects
                prof.disciplinas.clear()
                self.professores.remove(prof)
                return True
        return False
    
    def listarProfessores(self):
        return self.professores