import mysql.connector

conexao = mysql.connector.connect(
host="BD-ACD", # IP ou hostname do servidor MySQL puc-> BD-ACD
user="BD170225416", # "login"
password="Yyqdk4", # senha
database="BD170225416" # nome do banco (tem que existir) #BD170225416(isa)
)
cursor = conexao.cursor()
print('conectado com sucesso!')

#tabela sustentabilidade
cursor.execute("SELECT * FROM sustentabilidade")
resultado = cursor.fetchall()

print("TABELA SUSTENTABILIDADE:")
for linha in resultado:
    print(f"""\n 
ID:{linha[0]}
\t DATA_:{linha[1]}
\t CA_DATA: {linha[2]}
\t CA_GASTO: {linha[3]}
\t NR_QUANTIDADE:{linha[4]}
\t NR_PORCENTAGEM:{linha[5]}
\t CE_GASTO decimal:{linha[6]}
\t UT_CARRO:{linha[7]}
\t UT_CARONA_COMPARTILHADA :{linha[8]}
\t UT_BICICLETA :{linha[9]}
\t UT_TRANSPORTE_PUBLICO :{linha[10]}
\t UT_CARRO_ELETRICO:{linha[11]}
\t UT_CAMINHADA :{linha[12]}""")


#tabela resultados

id = int(input('Digite o ID que você deseja consultar: '))
cursor.execute("SELECT * FROM resultados WHERE ID = %s", (id,))
resultado = cursor.fetchall()

print("TABELA SUSTENTABILIDADE:")
for linha in resultado:
    print(f"""\n 
ID:{linha[0]}
\t DATA_:{linha[1]}
\t CA_RESULTADO: {linha[2]}
\t NR_RESULTADO: {linha[3]}
\t CE_RESULTADO:{linha[4]}
\t UT_RESULTADO:{linha[5]}""")        

