usuarios = {}
usuario_logado = None

def criar_usuario():
    global usuario_logado
    nome_usuario = input("Nome de usuário: ")
    if nome_usuario in usuarios:
        print("Esse Usuário já existe.")
        return
    senha = input("Senha: ")
    usuarios[nome_usuario] = {
        "senha": senha,
        "tarefas": []
    }
    usuario_logado = nome_usuario 
    print("Usuário criado com sucesso e login realizado!")

def login_usuario():
    global usuario_logado
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    if nome_usuario in usuarios and usuarios[nome_usuario]["senha"] == senha:
        usuario_logado = nome_usuario
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")

def logout_usuario():
    global usuario_logado
    usuario_logado = None
    print("Logout realizado com sucesso!")

def verificar_login():
    return usuario_logado
