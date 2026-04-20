def cadastrar():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    try:
        # Lê o arquivo para verificar se o usuário já existe
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(" ; ")

                # Regra: não permitir usuários duplicados
                if usuario == dados[0]:
                    print("Usuário já existe!")
                    return
    except FileNotFoundError:
        # Arquivo ainda não existe (primeiro uso do sistema)
        pass

    # Persiste o novo usuário no formato: usuario ; senha
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(usuario + " ; " + senha + "\n")

    print("Usuário cadastrado com sucesso!")


def login():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    try:
        # Busca o usuário no "banco de dados" (arquivo)
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(" ; ")

                if usuario == dados[0]:
                    # Validação direta de senha (sem criptografia nesta versão)
                    if senha == dados[1]:
                        print("Login realizado com sucesso!")
                        return
                    else:
                        print("Senha incorreta!")
                        return

        # Executado apenas se nenhum usuário correspondente for encontrado
        print("Usuário não encontrado!")

    except FileNotFoundError:
        # Nenhum usuário foi cadastrado ainda
        print("Nenhum usuário cadastrado ainda.")


while True:
    print("\n=== SISTEMA ===")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        login()

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")