from conexao import conectar

def criar_tabela_grupos():
    """Cria a tabela 'grupos'."""
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projeto.grupos (
                    id_grupo SERIAL PRIMARY KEY,
                    nome VARCHAR(50) NOT NULL,
                    descricao TEXT
                );
            """)
            conn.commit()  # Efetiva as alterações
            print("Tabela 'grupos' criada com sucesso.")
        except Exception as e:
            print("Erro ao criar a tabela 'grupos':", e)
        finally:
            conn.close()

if __name__ == "__main__":
    criar_tabela_grupos()
