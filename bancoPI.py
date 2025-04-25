import mysql.connector

conexao = mysql.connector.connect(
host="127.0.0.1", # IP ou hostname do servidor MySQL puc-> BD-ACD
user="root", # "login"
password="lqpqy2", # senha
database="PI" # nome do banco (tem que existir) #BD170225416(isa)
)
cursor = conexao.cursor()
print('conectado com sucesso!')
soma_ca = 0
soma_nrq = 0
soma_nrp = 0
soma_ce = 0
media_transporte = ''
#tabela sustentabilidade
cursor.execute("SELECT * FROM sustentabilidade")
resultado = cursor.fetchall()
num_registro = len(resultado)

print("\nTABELA SUSTENTABILIDADE:")
for linha in resultado:
    print(f"""\n 
ID: {linha[0]}
\t DATA_: {linha[1]}
\t CA_GASTO: {linha[2]}
\t NR_QUANTIDADE: {linha[3]}
\t NR_PORCENTAGEM: {linha[4]}
\t CE_GASTO decimal: {linha[5]}
\t UT_CARRO: {linha[6]}
\t UT_CARONA_COMPARTILHADA: {linha[7]}
\t UT_BICICLETA: {linha[8]}
\t UT_TRANSPORTE_PUBLICO: {linha[9]}
\t UT_CARRO_ELETRICO: {linha[10]}
\t UT_CAMINHADA: {linha[11]}""")
    soma_ca += linha[2]
    soma_nrq += linha[3]
    soma_nrp += linha[4]
    soma_ce += linha[5]
    if linha[6] == 'S' or linha[7] == 'S': 
        if linha[8] == 'S' or linha[9] == 'S' or linha[10] == 'S' or linha[11] == 'S':
            media_transporte = "Moderada Sustentabilidade"
        else:
            media_transporte = "Baixa Sustentabilidade"
    elif linha[8] == 'S' or linha[9] == 'S' or linha[10] == 'S' or linha[11] == 'S':
        media_transporte = "Alta Sustentabilidade"

cursor.execute("SELECT * FROM resultados")
resultado = cursor.fetchall()

print("TABELA RESULTADOS:")
for linha in resultado:
    print(f"""\n 
ID:{linha[0]}
\t DATA_:{linha[1]}
\t CA_RESULTADO: {linha[2]}
\t NR_RESULTADO: {linha[3]}
\t CE_RESULTADO:{linha[4]}
\t UT_RESULTADO:{linha[5]}""")        

print(f"\nMÉDIAS DE REGISTROS:\nCA_RESULTADO: {soma_ca / num_registro : .1f}\nNR_QUANTIDADE: {soma_nrq / num_registro : .1f}\nNR_PORCENTAGEM: {soma_nrp / num_registro : .1f}\nCE_GASTO: {soma_ce / num_registro : .1f}\nUT_RESULTADO: {media_transporte}")