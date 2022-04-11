import sqlite3 as conector

conexao = conector.connect("meu_banco.db")
cursor = conexao.cursor()

try:
    comando = ''' INSERT INTO Marca(nome, sigla) VALUES(:nome, :sigla)'''
    cursor.execute(comando, {"nome": "Hyundai", "sigla": "HYU"})
    conexao.commit()
except ConnectionError as e:
    print("Erro de banco de dados", e)

finally:
    cursor.close()
    conexao.close()