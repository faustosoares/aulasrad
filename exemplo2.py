import sqlite3 as conector

conexao = conector.connect("meu_banco.db")

#Banco em memória
#conexao = sqlite3.connect(':memory:')

cursor = conexao.cursor()

try:
    comando = '''CREATE TABLE Marca (
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id)
                );'''
    cursor.execute(comando)
    conexao.commit()
except conector.DatabaseError as e:
    print("Erro de banco de dados", e)

finally:
    #Fechando conexoes
    if conexao:
        cursor.close()
        conexao.close()