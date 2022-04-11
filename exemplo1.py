import sqlite3 as conector

conexao = conector.connect("meu_banco.db")

#Banco em memória
#conexao = sqlite3.connect(':memory:')

cursor = conexao.cursor()

try:
    comando = '''CREATE TABLE Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
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