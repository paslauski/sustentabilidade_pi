# pip install mysql-connector
# pip install mysql-connector-python
#cmd ^

import mysql.connector


conexao = mysql.connector.connect(
host="", # IP ou hostname do servidor MySQL puc-> BD-ACD
user="", # "login"
password="", # senha
database="" # nome do banco (tem que existir) #BD170225416(isa)
)
cursor = conexao.cursor()
print('conectado com sucesso!')


#tabela consumo de energia -> como ela esta no mysql (com ou sem dados adc)
cursor.execute("SELECT * FROM Consumo_Energia")
resultado = cursor.fetchall()

print("\nConsumo de enegia:")
for linha in resultado:
    print(f"CE_ID: {linha[0]}, CE_NOME: {linha[1]}, CE_DATA: {linha[2]}, CE_GASTO: {linha[3]}")


#CRIAR TABELA DENTRO DO PYTHON NO BD
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Consumo_Energia (
# CE_ID int auto_increment primary key,
# CE_NOME varchar (35) not null,
# CE_DATA date,
# CE_GASTO decimal (3,1) #(99.9) ou decimal(6,2)  pra aumentar bem..  até 9999.99
# )
# """)


#INSERIR DADOS

CE_NOME = input("Digite o nome: ")
CE_DATA = int(input("Digite a data (AAAA-MM-DD): ")) #tem q ser int no mysql mas como q põe data com "-"? 
#CE_DATA = input("Digite a data (AAAA-MM-DD): ") para ser str
CE_GASTO = float(input('digite o gasto(até 99.9): '))

sql = "INSERT INTO Consumo_Energia (CE_NOME, CE_DATA, CE_GASTO) VALUES (%s, %s, %s)"
valores = (CE_NOME, CE_DATA, CE_GASTO)
cursor.execute(sql, valores)
conexao.commit()
print("Dados inseridos com sucesso!")

#mostra tudo
tecla = input('>>>tecle qualquer tecla para mostrar tudo<<<')

cursor.execute("SELECT * FROM Consumo_Energia")
resultado = cursor.fetchall()
print("\nConsumo de Energia:")
for linha in resultado:
    print(f"CE_ID: {linha[0]}, Nome: {linha[1]}, Data: {linha[2]}, Gasto: {linha[3]}")


#excluir dado: ~~ ver como muda o ID quando é excluido 
tecle = int(input('deseja apagar algum dado? tecle 1 p sim e 0 p não:'))
if tecle == 1:
    id_excluir = int(input("digite o ID que deseja excluir: "))

    sql_delete = "DELETE FROM Consumo_Energia WHERE CE_ID = %s"
    cursor.execute(sql_delete, (id_excluir,))
    conexao.commit()

    print(f"o registro com ID {id_excluir} foi excluido com sucesso!")


#mostra tudo dnv
tecla = input('>>>tecle qualquer tecla para mostrar tudo dnv<<<')

cursor.execute("SELECT * FROM Consumo_Energia")
resultado = cursor.fetchall()
print("\nConsumo de Energia:")
for linha in resultado:
    print(f"CE_ID: {linha[0]}, Nome: {linha[1]}, Data: {linha[2]}, Gasto: {linha[3]}")

cursor.close()
conexao.close()
print ('conexão encerrada!')


