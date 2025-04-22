import mysql.connector


conexao = mysql.connector.connect(
host="BD-ACD", # IP ou hostname do servidor MySQL puc-> BD-ACD
user="BD170225416", # "login"
password="Yyqdk4", # senha
database="BD170225416" # nome do banco (tem que existir) #BD170225416(isa)
)
cursor = conexao.cursor()
print('conectado com sucesso!')

cursor.execute("SELECT * FROM sustentabilidade")
resultado = cursor.fetchall()

print("sustentabilidade tabela:")
for linha in resultado:
    print(f"A tabela atual: \n ID: {linha[0]}  \t DATA_: {linha[1]}\t  CA_DATA: {linha[2]}\t  CA_GASTO: {linha[3]}")