import sqlite3

# Função para adicionar uma nova tarefa
def adicionar_tarefa(titulo):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    conn.close()
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

# Função para listar tarefas pendentes
def listar_tarefas():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo FROM tarefas WHERE concluida = 0")
    tarefas = cursor.fetchall()
    conn.close()

    print("\n📌 Tarefas Pendentes:")
    for tarefa in tarefas:
        print(f"[{tarefa[0]}] {tarefa[1]}")
    
# Função para marcar uma tarefa como concluída
def concluir_tarefa(id_tarefa):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    print(f"Tarefa {id_tarefa} marcada como concluída!")

# Função para remover uma tarefa
def remover_tarefa(id_tarefa):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    print(f"Tarefa {id_tarefa} removida com sucesso!")


while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite a tarefa: ")
        adicionar_tarefa(titulo)

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        id_tarefa = int(input("Digite o ID da tarefa concluída: "))
        concluir_tarefa(id_tarefa)

    elif opcao == "4":
        id_tarefa = int(input("Digite o ID da tarefa a remover: "))
        remover_tarefa(id_tarefa)

    elif opcao == "5":
        print("Saindo... Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
