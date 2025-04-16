# pip install mysql-connector
# pip install mysql-connector-python
#cmd ^

import mysql.connector


conexao = mysql.connector.connect(
host="BD-ACD", # IP ou hostname do servidor MySQL puc-> BD-ACD
user="BD170225416", # "login"
password="Yyqdk4", # senha
database="BD170225416" # nome do banco (tem que existir) #BD170225416(isa)
)
cursor = conexao.cursor()
print('banco de dados conectado com sucesso!')

cursor.execute("SELECT * FROM Consumo_Energia")
resultado = cursor.fetchall()
print(f"{resultado}") #exbir por coluna como tabela

#TIRAR DATAS NO BD PQ TODAS ASTABELAS TEM E NOMES TBM
#media de sustentabilidade mostrar relatorio - mostrar registro 
#mostrar como tabel no py
conexao = mysql.connector.connect(
host="", # IP ou hostname do servidor MySQL puc-> BD-ACD
user="", # "login"
password="", # senha
database="" # nome do banco (tem que existir) #BD170225416(isa)
)


#excluir dado: ~~ ver como muda o ID quando é excluido 
    tecle = int(input('deseja apagar algum dado? tecle 1 p sim e 0 p não:'))
    if tecle == 1:
        id_excluir = int(input("digite o ID que deseja excluir: "))

        sql_delete = "DELETE FROM Consumo_Agua WHERE CA _ID = %s"
        cursor.execute(sql_delete, (id_excluir,))
        conexao.commit()

        print(f"o registro com ID {id_excluir} foi excluido com sucesso!")

    #CRIAR TABELA DENTRO DO PYTHON NO BD
    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS Consumo_Energia (
    # CE_ID int auto_increment primary key,
    # CE_NOME varchar (35) not null,
    # CE_DATA date,
    # CE_GASTO decimal (3,1) #(99.9) ou decimal(6,2)  pra aumentar bem..  até 9999.99
    # )
    # """)