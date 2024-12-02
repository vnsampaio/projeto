from conexao import conectar

def criar_tabela_grupo_pessoas():
    """Cria a tabela 'grupo_pessoas'."""
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projeto.grupo_pessoas (
                    id_grupo_pessoa SERIAL PRIMARY KEY,
                    id_grupo INT NOT NULL,
                    id_pessoa INT NOT NULL,
                    FOREIGN KEY (id_grupo) REFERENCES grupos (id_grupo),
                    FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa)
                );
            """)
            conn.commit()  # Efetiva as alterações
            print("Tabela 'grupo_pessoas' criada com sucesso.")
        except Exception as e:
            print("Erro ao criar a tabela 'grupo_pessoas':", e)
        finally:
            conn.close()

if __name__ == "__main__":
    criar_tabela_grupo_pessoas()
