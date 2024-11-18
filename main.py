from universidade import Universidade

def exibir_menu():
    print("\nGerenciar Universidade")
    print("1. Criar departamento")
    print("2. Remover departamento")
    print("3. Listar departamentos")
    print("4. Adicionar professor")
    print("5. Remover professor")
    print("6. Listar professores")
    print("7. Adicionar disciplina")
    print("8. Remover disciplina")
    print("9. Listar disciplinas")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    # initialize university
    univ = Universidade("Universidade Exemplo", "Rua Principal, 123", "UNIV001")
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            nome = input("Nome do departamento: ")
            id = int(input("ID do departamento: "))
            faculdadeId = int(input("ID da faculdade: "))
            univ.criarDepartamento(nome, id, faculdadeId)
            print("Departamento criado com sucesso!")
            
        elif opcao == "2":
            id = int(input("ID do departamento a remover: "))
            if univ.removerDepartamento(id):
                print("Departamento removido com sucesso!")
            else:
                print("Departamento não encontrado!")
                
        elif opcao == "3":
            deps = univ.listarDepartamentos()
            if deps:
                print("\nDepartamentos:")
                for dep in deps:
                    print(f"Nome: {dep.nomeDepartamento}, ID: {dep.id}")
            else:
                print("Nenhum departamento cadastrado!")
                
        elif opcao == "4":
            if not univ.departamentos:
                print("Crie um departamento primeiro!")
                continue
                
            dept_id = int(input("ID do departamento: "))
            dept = None
            for d in univ.departamentos:
                if d.id == dept_id:
                    dept = d
                    break
                    
            if dept:
                nome = input("Nome do professor: ")
                id_prof = int(input("ID do professor: "))
                dept.adicionarProfessor(nome, id_prof)
                print("Professor adicionado com sucesso!")
            else:
                print("Departamento não encontrado!")
                
        elif opcao == "5":
            if not univ.departamentos:
                print("Nenhum departamento cadastrado!")
                continue
                
            dept_id = int(input("ID do departamento: "))
            dept = None
            for d in univ.departamentos:
                if d.id == dept_id:
                    dept = d
                    break
                    
            if dept:
                prof_id = int(input("ID do professor a remover: "))
                if dept.deletarProfessor(prof_id):
                    print("Professor removido com sucesso!")
                else:
                    print("Professor não encontrado!")
            else:
                print("Departamento não encontrado!")
                
        elif opcao == "6":
            if not univ.departamentos:
                print("Nenhum departamento cadastrado!")
                continue
                
            dept_id = int(input("ID do departamento: "))
            dept = None
            for d in univ.departamentos:
                if d.id == dept_id:
                    dept = d
                    break
                    
            if dept:
                profs = dept.listarProfessores()
                if profs:
                    print("\nProfessores:")
                    for prof in profs:
                        print(f"Nome: {prof.nome}, ID: {prof.idProfessor}")
                else:
                    print("Nenhum professor cadastrado neste departamento!")
            else:
                print("Departamento não encontrado!")
                
        elif opcao == "7":
            if not univ.departamentos:
                print("Nenhum departamento cadastrado!")
                continue
                
            dept_id = int(input("ID do departamento: "))
            dept = None
            for d in univ.departamentos:
                if d.id == dept_id:
                    dept = d
                    break
                    
            if dept:
                prof_id = int(input("ID do professor: "))
                prof = None
                for p in dept.professores:
                    if p.idProfessor == prof_id:
                        prof = p
                        break
                        
                if prof:
                    nome = input("Nome da disciplina: ")
                    id_disc = int(input("ID da disciplina: "))
                    prof.adicionarDisciplina(nome, id_disc)
                    print("Disciplina adicionada com sucesso!")
                else:
                    print("Professor não encontrado!")
            else:
                print("Departamento não encontrado!")
                
        elif opcao == "8":
            if not univ.departamentos:
                print("Nenhum departamento cadastrado!")
                continue
                
            dept_id = int(input("ID do departamento: "))
            dept = None
            for d in univ.departamentos:
                if d.id == dept_id:
                    dept = d
                    break
                    
            if dept:
                prof_id = int(input("ID do professor: "))
                prof = None
                for p in dept.professores:
                    if p.idProfessor == prof_id:
                        prof = p
                        break
                        
                if prof:
                    disc_id = int(input("ID da disciplina a remover: "))
                    if prof.deletarDisciplina(disc_id):
                        print("Disciplina removida com sucesso!")
                    else:
                        print("Disciplina não encontrada!")
                else:
                    print("Professor não encontrado!")
            else:
                print("Departamento não encontrado!")
                
        elif opcao == "9":
            if not univ.departamentos:
                print("Nenhum departamento cadastrado!")
                continue
                
            dept_id = int(input("ID do departamento: "))
            dept = None
            for d in univ.departamentos:
                if d.id == dept_id:
                    dept = d
                    break
                    
            if dept:
                prof_id = int(input("ID do professor: "))
                prof = None
                for p in dept.professores:
                    if p.idProfessor == prof_id:
                        prof = p
                        break
                        
                if prof:
                    discs = prof.listarDisciplinas()
                    if discs:
                        print("\nDisciplinas:")
                        for disc in discs:
                            print(f"Nome: {disc.nome}, ID: {disc.id}")
                    else:
                        print("Nenhuma disciplina cadastrada para este professor!")
                else:
                    print("Professor não encontrado!")
            else:
                print("Departamento não encontrado!")
                
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()