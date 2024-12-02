import pg8000

def conectar():
    
    try:
        return pg8000.connect(
            host="localhost",
            port=5432,
            database="postgres",
            user="postgres",
            password="postgres"
        )
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None
