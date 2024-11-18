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
                # remover departament's professors at first
                dept.professores.clear()
                self.departamentos.remove(dept)
                return True
        return False
    
    def listarDepartamentos(self):
        return self.departamentos