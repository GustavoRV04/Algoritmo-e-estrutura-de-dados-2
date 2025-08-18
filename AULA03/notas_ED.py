class Turma:
    def __init__(self):
        self.alunos = []

    def inserir_aluno(self, nome, matricula, nota):
        novo_aluno = {"matricula": matricula, "nome": nome, "nota": nota}
        self.alunos.append(novo_aluno)
        print(f"Aluno {nome} inserido com sucesso!\n")

    def ordenar_por_matricula(self):
        self.alunos.sort(key=lambda x: x["matricula"])

    def ordenar_por_nota(self):
        self.alunos.sort(key=lambda x: x["nota"], reverse=True)

    def busca_binaria_matricula(self, matricula):
        self.ordenar_por_matricula()
        inicio = 0
        fim = len(self.alunos) - 1
        comparacoes = 0

        while inicio <= fim:
            meio = (inicio + fim) // 2
            comparacoes += 1
            if self.alunos[meio]["matricula"] == matricula:
                return self.alunos[meio], comparacoes
            elif self.alunos[meio]["matricula"] < matricula:
                inicio = meio + 1
            else:
                fim = meio - 1

        return None, comparacoes

    def busca_sequencial_nome(self, nome_busca):
        encontrados = []
        comparacoes = 0

        for aluno in self.alunos:
            comparacoes += 1
            if aluno["nome"].lower() == nome_busca.lower():
                encontrados.append(aluno)

        return encontrados, comparacoes


def status_aluno(nota):
    return "Aprovado" if nota >= 6 else "Reprovado"


def exibir_resultado(aluno, comparacoes):
    if aluno:
        print(f"\nAluno encontrado após {comparacoes} comparações:")
        print(f"Nome: {aluno['nome']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nota: {aluno['nota']}")
        print(f"Status: {status_aluno(aluno['nota'])}")
    else:
        print(f"\nAluno não encontrado após {comparacoes} comparações.")


def exibir_resultado_nome(encontrados, comparacoes):
    if encontrados:
        print(f"\n{len(encontrados)} aluno(s) encontrado(s) após {comparacoes} comparações:")
        for aluno in encontrados:
            print(f"Nome: {aluno['nome']}")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nota: {aluno['nota']}")
            print(f"Status: {status_aluno(aluno['nota'])}")
            print("---")
    else:
        print(f"\nNenhum aluno encontrado após {comparacoes} comparações.")


def main():
    turma = Turma()

    # Alunos iniciais
    turma.inserir_aluno("Ana", 1001, 8.5)
    turma.inserir_aluno("Bruno", 1002, 5.0)
    turma.inserir_aluno("Carla", 1003, 6.7)
    turma.inserir_aluno("Daniel", 1004, 9.2)
    turma.inserir_aluno("Eduarda", 1005, 4.8)

    while True:
        print("\n--- MENU ---")
        print("1. Buscar aluno por matrícula")
        print("2. Inserir novo aluno")
        print("3. Ordenar alunos por nota")
        print("4. Buscar aluno por nome")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            matricula_busca = int(input("Digite a matrícula: "))
            aluno, comparacoes = turma.busca_binaria_matricula(matricula_busca)
            exibir_resultado(aluno, comparacoes)

        elif opcao == "2":
            nome = input("Nome do aluno: ")
            matricula = int(input("Matrícula: "))
            nota = float(input("Nota: "))
            turma.inserir_aluno(nome, matricula, nota)

        elif opcao == "3":
            turma.ordenar_por_nota()
            print("\nAlunos ordenados por nota (maior para menor):")
            for aluno in turma.alunos:
                print(f"{aluno['nome']} - Nota: {aluno['nota']}")

        elif opcao == "4":
            nome_busca = input("Digite o nome do aluno: ")
            encontrados, comparacoes = turma.busca_sequencial_nome(nome_busca)
            exibir_resultado_nome(encontrados, comparacoes)

        elif opcao == "5":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
