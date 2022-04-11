import sqlite3

#Abertura da conexão
conexao = sqlite3.connect("URL SQLITE")

#Aquisição de um cursor
cursor = conexao.cursor()

#Execução de Comandos

cursor.execute("...")
cursor.fetchall()

#Efetivação do comando
conexao.commit()

#Fechando conexao
cursor.close()
conexao.close()






'''
#Abertura da conexão
conexao = sqlite3.connect("URL SQLITE")

#Aquisição de um cursor
cursor = conexao.cursor()

#Execução de Comandos

try:
    cursor.execute("...")
    cursor.fetchall()
except sqlite3.OperationalError as erro:
    print("Erro de execucao de comando")

#Efetivação do comando
conexao.commit()

#Fechando conexao
cursor.close()
conexao.close()
'''