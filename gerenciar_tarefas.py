from usuarios.gerenciar_usuario import usuarios, verificar_login

def criar_tarefa():
    usuario_logado = verificar_login()
    if not usuario_logado:
        print("Você precisa estar logado para criar uma tarefa.")
        return
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "status": "Não concluída"
    }
    usuarios[usuario_logado]["tarefas"].append(tarefa)
    print("Tarefa criada com sucesso!")

def visualizar_tarefas():
    usuario_logado = verificar_login()
    if not usuario_logado:
        print("Você precisa estar logado para ver suas tarefas.")
        return
    tarefas = usuarios[usuario_logado]["tarefas"]
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['nome']} - {tarefa['descricao']} - Status: {tarefa['status']}")

def atualizar_tarefa():
    usuario_logado = verificar_login()
    if not usuario_logado:
        print("Você precisa estar logado para atualizar uma tarefa.")
        return
    visualizar_tarefas()
    try:
        indice = int(input("Número da tarefa a atualizar: ")) - 1
        tarefas = usuarios[usuario_logado]["tarefas"]
        if 0 <= indice < len(tarefas):
            tarefa = tarefas[indice]
            tarefa["nome"] = input("Novo nome da tarefa: ")
            tarefa["descricao"] = input("Nova descrição da tarefa: ")
            tarefa["status"] = input("Novo status da tarefa (Concluída ou Não concluída): ")
            print("Tarefa atualizada com sucesso!")
        else:
            print("Tarefa não encontrada.")
    except ValueError:
        print("Número inválido.")

def deletar_tarefa():
    usuario_logado = verificar_login()
    if not usuario_logado:
        print("Você precisa estar logado para deletar uma tarefa.")
        return
    visualizar_tarefas()
    try:
        indice = int(input("Número da tarefa a deletar: ")) - 1
        tarefas = usuarios[usuario_logado]["tarefas"]
        if 0 <= indice < len(tarefas):
            del tarefas[indice]
            print("Tarefa deletada com sucesso!")
        else:
            print("Tarefa não encontrada.")
    except ValueError:
        print("Número inválido.")
