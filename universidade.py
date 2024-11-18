class Universidade:
    def __init__(self, nome, endereco, id):
        self.nome = nome
        self.endereco = endereco
        self.id = id
        self.departamentos = []

    def criarDepartamento(self, nome, id, faculdadeId):
        from departamento import Departamento
        dept = Departamento(nome, id, faculdadeId)
        self.departamentos.append(dept)
        return dept

    def removerDepartamento(self, id):
        for dept in self.departamentos:
            if dept.id == id:
                # Primeiro removemos todas as disciplinas dos professores
                for prof in dept.professores:
                    prof.disciplinas.clear()
                # Depois removemos os professores
                dept.professores.clear()
                # Finalmente removemos o departamento
                self.departamentos.remove(dept)
                return True
        return False

    def listarDepartamentos(self):
        return self.departamentos


class Departamento:
    def __init__(self, nomeDepartamento, id, faculdadeId):
        self.nomeDepartamento = nomeDepartamento
        self.id = id
        self.faculdadeId = faculdadeId
        self.professores = []

    def adicionarProfessor(self, nome, idProfessor):
        from professor import Professor
        # Verificar se o professor já existe
        if any(p.idProfessor == idProfessor for p in self.professores):
            return None
        prof = Professor(nome, idProfessor, self.id)
        self.professores.append(prof)
        return prof

    def deletarProfessor(self, idProfessor):
        for prof in self.professores:
            if prof.idProfessor == idProfessor:
                # Primeiro removemos todas as disciplinas do professor
                prof.disciplinas.clear()
                # Depois removemos o professor
                self.professores.remove(prof)
                return True
        return False

    def listarProfessores(self):
        return self.professores