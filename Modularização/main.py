from Funções.usuarios import cadastrar_usuario, login_usuario

def menu():
    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            cadastrar_usuario(nome, senha)

        elif opcao == "2":
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            login_usuario(nome, senha)

        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
