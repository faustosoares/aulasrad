import sqlite3 as conector

conexao = conector.connect("meu_banco.db")

#Banco em memória
#conexao = sqlite3.connect(':memory:')

cursor = conexao.cursor()

try:
    comando = '''CREATE TABLE Veiculo (
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id)
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