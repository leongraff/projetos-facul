# A. Print de boas-vindas com o seu nome
print("Bem-vindo ao sistema de cadastro de colaboradores do Leon Graff!")

# criando id global e a lista
lista_colaboradores = []
id_global = 0


# definindo função de cadastro
def cadastrar_colaborador(id):
    global id_global  # Use the global id_global variable
    id_global = id
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))

    colaborador = {"id": id, "nome": nome, "setor": setor, "salário": salario}

    # adicionando dicionario a lista
    lista_colaboradores.append(colaborador)


# definindo função de consulta de colaborador
def consultar_colaborador():
    opcao = int(
        input(
            "Digite a opção desejada:\n1. Consultar Todos os colaboradores\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\n"
        )
    )

    if opcao == 1:
        # consulta todos
        print("------------ MENU CONSULTAR COLABORADOR ------------")
        for colaborador in lista_colaboradores:
            for key, value in colaborador.items():
                print("{}: {}".format(key, value))
            print()
    elif opcao == 2:
        # consulta por id
        id_consulta = int(input("Digite o id do colaborador a ser consultado: "))
        for colaborador in lista_colaboradores:
            if colaborador["id"] == id_consulta:
                print("----- Colaborador encontrado -----")
                for key, value in colaborador.items():
                    print("{}: {}".format(key, value))
                print()
                break
        else:
            print("Colaborador não encontrado.")
    elif opcao == 3:
        # por setor
        setor_consulta = input("Digite o setor dos colaboradores a serem consultados: ")
        print("----- Colaboradores do Setor {} -----".format(setor_consulta))
        for colaborador in lista_colaboradores:
            if colaborador["setor"].lower() == setor_consulta.lower():
                for key, value in colaborador.items():
                    print("{}: {}".format(key, value))
                print()
    elif opcao == 4:
        return
    else:
        print("Opção inválida.")


# definindo função para remover colaborador
def remover_colaborador():
    id_remocao = int(input("Digite o id do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_remocao:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            break
    else:
        print("Colaborador não encontrado.")


# função main
def main():
    global id_global
    while True:
        print("\n-------------- MENU PRINCIPAL --------------")
        print("1. Cadastrar Colaborador")
        print("2. Consultar Colaborador(es)")
        print("3. Remover Colaborador")
        print("4. Sair")
        opcao_menu = int(input("Escolha uma opção: "))

        if opcao_menu == 1:
            id_global += 1
            cadastrar_colaborador(id_global)
        elif opcao_menu == 2:
            consultar_colaborador()
        elif opcao_menu == 3:
            remover_colaborador()
        elif opcao_menu == 4:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


main()
