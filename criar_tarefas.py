from conexao import conectar

def criar_tabela_tarefas():
    """Cria a tabela 'tarefas'."""
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projeto.tarefas (
                    id_tarefa SERIAL PRIMARY KEY,
                    titulo VARCHAR(100) NOT NULL,
                    descricao TEXT,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    concluida BOOLEAN DEFAULT FALSE,
                    id_pessoa INT,
                    id_grupo INT,
                    FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa) ON DELETE SET NULL,
                    FOREIGN KEY (id_grupo) REFERENCES grupos (id_grupo) ON DELETE SET NULL
                );
            """)
            conn.commit()  # Efetiva as alterações
            print("Tabela 'tarefas' criada com sucesso.")
        except Exception as e:
            print("Erro ao criar a tabela 'tarefas':", e)
        finally:
            conn.close()

if __name__ == "__main__":
    criar_tabela_tarefas()
