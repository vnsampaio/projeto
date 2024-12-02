from usuarios.gerenciar_usuario import criar_usuario, login_usuario, logout_usuario, verificar_login
from tarefas.gerenciar_tarefas import criar_tarefa, visualizar_tarefas, atualizar_tarefa, deletar_tarefa

def main():
    while True:
        print("\nMenu:")
        if verificar_login():
            print("1. Criar tarefa")
            print("2. Visualizar tarefas")
            print("3. Atualizar tarefa")
            print("4. Deletar tarefa")
            print("5. Logout")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                criar_tarefa()
            elif opcao == '2':
                visualizar_tarefas()
            elif opcao == '3':
                atualizar_tarefa()
            elif opcao == '4':
                deletar_tarefa()
            elif opcao == '5':
                logout_usuario()
            else:
                print("Opção inválida.")
        else:
            print("1. Criar usuário")
            print("2. Login")
            print("3. Encerrar programa")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                criar_usuario()
            elif opcao == '2':
                login_usuario()
            elif opcao == '3':
                print("Encerrando programa.")
                break
            else:
                print("Opção inválida.")

main()
