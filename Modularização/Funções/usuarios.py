def cadastrar_usuario(nome, senha):
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                usuario = linha.strip().split(", ")[0].lower()
                if usuario.lower() == nome.lower():
                    print("Nome de usuário já existe. Tente outro.")
                    return
                
    except FileNotFoundError:
        pass 

    while True:
        if len(senha) < 8:
            print("Senha deve ter pelo menos 8 caracteres.")
        elif not any(letra.isupper() for letra in senha):
            print("Senha deve ter pelo menos uma letra maiúscula.")
        elif not any(letra.isdigit() for letra in senha):
            print("Senha deve ter pelo menos um número.")
        else:
            break
        
        senha = input("Digite a senha novamente: ")
        

    with open('usuarios.txt', 'a') as arquivo:
        arquivo.write(f"{nome}, {senha}\n")
    print("Usuário cadastrado com sucesso!")

def login_usuario(nome, senha):
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                usuario, senha_salva = linha.strip().split(", ")
                if usuario.lower() == nome.lower() and senha_salva == senha:
                    print("Login realizado com sucesso!")
                    return True
        
        print("Nome de usuario ou senha incorretos.")
        return False
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.")
        return False
    
