# pip install mysql-connector
# pip install mysql-connector-python
#cmd ^

import mysql.connector


conexao = mysql.connector.connect(
host="localhost", # IP ou hostname do servidor MySQL puc-> BD-ACD   localhost
user="root", # "login" root
password="@Isamysql", # senha
database="sustentabilidade" # nome do banco (tem que existir) #BD170225416(isa)
)
cursor = conexao.cursor()
print('conectado com sucesso!')

programa = 1
while programa == 1:
    #boas vinda.. seleciona oque quer
    print(f'''Bem vindo ao banco de dados de sustentabilidade\nsiga as instruções e tecle a respectiva tecla com o numero da instrução:''')
    funcao= int(input(f'''
        0 -> PARA RODAR O PROGARAM INTEIRO = basta clicar qualquer outra tecla
        1. DELETAR ALGUM DADO por id\n
        2. IR PARA ALGUM TABELA ESPECIFICA\n
        3.    \n
        \n'''))
    # variaveis pra não repetir e reutilizalas sem usar def 
    controle_energia = 0
    # 0 RODA TUDO

    if funcao != 1 and funcao !=2 and funcao != 3:

        #CONSUMO DE ÁGUA

        cursor.execute("SELECT * FROM Consumo_Agua")
        resultado = cursor.fetchall()

        print("\nConsumo de água:")
        for linha in resultado:
            print(f"A tabela atual: \n CA_ID: {linha[0]}  \t CA_NOME: {linha[1]}\t  CA_DATA: {linha[2]}\t  CA_GASTO: {linha[3]}")

        #INSERIR DADOS
        in_consumoagua = int(input(f'''Você deseja inserir algum dado na tabela CONSUM DE ÁGUA?\n
        tecle = 1 para >>>SIM<<   \t tecle = 0 para >>> NÃO<<'''))
        if in_consumoagua == 1:
            CA_NOME = input("Digite o nome: ")
            CA_DATA = int(input("Digite a data (AAAA-MM-DD): ")) #tem q ser int no mysql mas como q põe data com "-"? 
            CA_GASTO = float(input('digite o gasto(até 99.9): '))

            sql = "INSERT INTO Consumo_Agua (CA_NOME, CA_DATA, CA_GASTO) VALUES (%s, %s, %s)"
            valores = (CA_NOME, CA_DATA, CA_GASTO)
            cursor.execute(sql, valores)
            conexao.commit()
            print("Dados inseridos com sucesso!")

            #mostra tudo
            tecle = input('>>>tecle qualquer tecla para mostrar tudo<<<')
            cursor.execute("SELECT * FROM Consumo_Agua")
            resultado = cursor.fetchall()
            print("\nConsumo de Água:")
            for linha in resultado:
                print(f"CA_ID: {linha[0]}, Nome: {linha[1]}, Data: {linha[2]}, Gasto: {linha[3]}")

        
    #1 DELETAR DADO por ID

    if funcao == 1:
        tecle = int(input(f'''Você deseja apagar algum dado? \ntecle = 1 para >>>SIM<<   \t tecle = 0 para >>> NÃO<<'''))
        if tecle == 1:
            while tecle ==1:
                id_excluir = int(input("digite o ID que deseja excluir: "))

                #delte consumo enrgia
                sql_delete = "DELETE FROM Consumo_Energia WHERE CE_ID = %s"
                cursor.execute(sql_delete, (id_excluir,))
                conexao.commit()

                #delete consumo agua
                sql_delete = "DELETE FROM Consumo_Agua WHERE CA_ID = %s"
                cursor.execute(sql_delete, (id_excluir,))
                conexao.commit()
                print(f"o registro com ID {id_excluir} foi excluido com sucesso!")
                #mostra tudo dnv
                tecle = int(input('Deseja apagar algum outro dado? \n tecle = 1 para >>>SIM<<   \t tecle = 0 para >>> NÃO<<:'))
                #printar tabelas


    # 2 IR DIRETO PARA UMA TABELA ESPECIFICA (ver)
    if funcao == 2:
        tecle = int(input(f'''Qual tabela você deseja ver? 
                         \n 1. TABELA DE CONSUMO DE ENERGIA \t 2. TABELA CONSUMO DE ÁGUA \n 3. TABELA CONSUMO DE NÃO RECICLAVEIS \n TABELA DE TRANSPORTES'''))
        select_ce= 1
        select_ca= 2
        select_nr= 3
        select_t= 4
        #ver tabela energia
        if tecle == 1:
            cursor.execute("SELECT * FROM Consumo_Energia")
            resultado = cursor.fetchall()

            # print("\nConsumo de enegia:")
            # for linha in resultado:
            #     print(f"A tabela atual: \n CE_ID: {linha[0]}  \t CE_NOME: {linha[1]}\t  CE_DATA: {linha[2]}\t  CE_GASTO: {linha[3]}")
            #inserir dado na tabela pela função 2
            TECLA_I=int(input(f'''Você deseja inserir algum dado na tabela CONSUM DE ENERGIA?\n
        tecle = 1 para >>>SIM<<   \t tecle = 0 para >>> NÃO<<'''))
            if TECLA_I == 1:
                controle_energia = 1
                #CONSUMO DE ENERGIA
        #tabela consumo de energia -> como ela esta no mysql (com ou sem dados adc)

        cursor.execute("SELECT * FROM Consumo_Energia")
        resultado = cursor.fetchall()

        print("\nConsumo de enegia:")
        for linha in resultado:
            print(f"A tabela atual: \n CE_ID: {linha[0]}  \t CE_NOME: {linha[1]}\t  CE_DATA: {linha[2]}\t  CE_GASTO: {linha[3]}")

        #INSERIR DADOS
        in_consumoenergia = int(input(f'''Você deseja inserir algum dado na tabela CONSUM DE ENERGIA?\n
        tecle = 1 para >>>SIM<<   \t tecle = 0 para >>> NÃO<<'''))
        if in_consumoenergia == 1:
            controle__energia = 1
            if controle_energia == 1:
                CE_NOME = input("Digite o nome: ")
                CE_DATA = int(input("Digite a data (AAAAMMDD): ")) #tem q ser int no mysql mas como q põe data com "-"? 
                CE_GASTO = float(input('digite o gasto(até 99.9): '))

                sql = "INSERT INTO Consumo_Energia (CE_NOME, CE_DATA, CE_GASTO) VALUES (%s, %s, %s)"
                valores = (CE_NOME, CE_DATA, CE_GASTO)
                cursor.execute(sql, valores)
                conexao.commit()
                print("Dados inseridos com sucesso!")

            #mostra tudo
                tecle = input('>>>tecle qualquer tecla para mostrar tudo<<<')
                cursor.execute("SELECT * FROM Consumo_Energia")
                resultado = cursor.fetchall()
                print("\nConsumo de Energia:")
                for linha in resultado:
                    print(f"CE_ID: {linha[0]}, Nome: {linha[1]}, Data: {linha[2]}, Gasto: {linha[3]}")







    #final
    resposta = input("Deseja continuar? (s/n): ").strip().lower()
    if resposta == "s" :
        programa =1
    else:
         programa=0
#break do while
cursor.close() #fora do while 
conexao.close()
print (f'''conexão encerrada! \nObrigada por atualizar a tabela!''')