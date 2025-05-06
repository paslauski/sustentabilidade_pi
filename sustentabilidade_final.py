import mysql.connector

programaAtivo = True

conexao = mysql.connector.connect(
host="", 
user="", 
password="", 
database=""
)
cursor = conexao.cursor()
print("Conectado com sucesso!")

soma_ca = 0
soma_ce = 0
soma_nrp = 0
soma_nrq = 0
num_registro = 0

while programaAtivo:
    menu = int(input(f'''
        1 ->  INSERIR REGISTO\n
        2 ->  DELETAR ALGUM DADO POR ID\n
        3 ->  ALTERAR DADO INSERIDO\n
        4 ->  LISTA TABELA POR ID\n
        5 ->  LISTAR MÉDIA\n
        6 ->   SAIR \n'''))
    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5 and menu != 6:
        menu = int(input(f'''Função fora do escopo! Digite uma função válida:\n
        1 ->  INSERIR REGISTO\n
        2 ->  DELETAR ALGUM DADO POR ID\n
        3 ->  ALTERAR DADO INSERIDO\n
        4 ->  LISTA TABELA POR ID\n
        5 ->  LISTAR MÉDIA\n
        6 ->   SAIR \n'''))
    # Coletando os dados do usuário
    match menu:
        case 1: #inserir
            DATA_ = input("Qual é a data (AAAA-MM-DD)? ")
            CA_GASTO = float(input("Quantos litros de água você consumiu hoje? "))
            CE_GASTO = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
            NR_QUANTIDADE =float(input("Quantos KG de resíduos não reciclaveis você gerou hoje? "))
            NR_PORCENTAGEM = float(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))

            #Entrada de múltiplos meios de transporte atualizada
            print(f"\nEscolha os meios de transporte utilizados hoje: Responda apenas com S ou N.")
            UT_CARRO = input(f"\t1. Carro (combustível fósseis) ").upper()
            while UT_CARRO != 'S' and UT_CARRO != 'N':
                UT_CARRO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CARONA_COMPARTILHADA = input(f"\t2. Carona compartilhada ").upper()
            while UT_CARONA_COMPARTILHADA != 'S' and UT_CARONA_COMPARTILHADA != 'N':
                UT_CARONA_COMPARTILHADA = input(f"\tDigite apenas S ou N. ").upper()
            UT_BICICLETA = input(f"\t3. Bicicleta ").upper()
            while UT_BICICLETA != 'S' and UT_BICICLETA != 'N':
                UT_BICICLETA = input(f"\tDigite apenas S ou N. ").upper()
            UT_TRANSPORTE_PUBLICO = input(f"\t4. Transporte público (ônibus, metrô, trem) ").upper()
            while UT_TRANSPORTE_PUBLICO != 'S' and UT_TRANSPORTE_PUBLICO != 'N': # not in ['S', 'N']:
                UT_TRANSPORTE_PUBLICO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CARRO_ELETRICO = input(f"\t5. Carro elétrico ").upper()
            while UT_CARRO_ELETRICO != 'S' and UT_CARRO_ELETRICO != 'N':
                UT_CARRO_ELETRICO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CAMINHADA = input(f"\t6. Caminhada ").upper()
            while  UT_CAMINHADA != 'S' and  UT_CAMINHADA != 'N':
                UT_CAMINHADA = input(f"\tDigite apenas S ou N. ").upper()

            # Classificação de consumo de agua
            if CA_GASTO < 150:
                CA_RESULTADO = "Alta Sustentabilidade"
            elif 150 <= CA_GASTO <= 200:
                CA_RESULTADO = "Moderada Sustentabilidade"
            else:
                CA_RESULTADO = "Baixa Sustentabilidade"

            # Classificação de consumo de energia
            if CE_GASTO < 5:
                CE_RESULTADO = "Alta Sustentabilidade"
            elif 5 <= CE_GASTO <= 10:
                CE_RESULTADO = "Moderada Sustentabilidade"
            else:
                CE_RESULTADO = "Baixa Sustentabilidade"

            # Classificação de resíduos recicláveis
            if NR_PORCENTAGEM > 50:
                NIVEL_NR_PORCENTAGEM = "Alta Sustentabilidade"
            elif 20 <= NR_PORCENTAGEM <= 50:
                NIVEL_NR_PORCENTAGEM = "Moderada Sustentabilidade"
            else:
                NIVEL_NR_PORCENTAGEM = "Baixa Sustentabilidade"

            # Classificação do transporte
            NIVEL_TRANSPORTE = "Baixa Sustentabilidade"
            if UT_CARRO == 'S' or UT_CARONA_COMPARTILHADA == 'S':
                if UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S' or UT_CAMINHADA == 'S':
                    NIVEL_TRANSPORTE = "Moderada Sustentabilidade"
                else:
                    NIVEL_TRANSPORTE = "Baixa Sustentabilidade"
            elif UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S'or UT_CAMINHADA == 'S':
                NIVEL_TRANSPORTE = "Alta Sustentabilidade"
            
            #inserir dados na tabela SUSTENTABILIDADE
            cursor.execute(("""INSERT INTO sustentabilidade 
            (DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO,
            UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA, UT_TRANSPORTE_PUBLICO, UT_CARRO_ELETRICO, 
            UT_CAMINHADA)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """), 
            (DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO, UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA,
            UT_TRANSPORTE_PUBLICO, UT_CARRO_ELETRICO, UT_CAMINHADA))
            cursor.execute(("""INSERT INTO  resultados
                            (DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO)
                            VALUES(%s, %s, %s, %s, %s)"""),
            (DATA_, CA_RESULTADO, NIVEL_NR_PORCENTAGEM, CE_RESULTADO, NIVEL_TRANSPORTE))
            conexao.commit()
            print('Dados inseridos com sucesso!')
        case 2:#DELETAR ALGUM DADO POR ID

            deletar=True
            while deletar:
                id_excluir = int(input("digite o ID que deseja excluir: "))
                cursor.execute("SELECT *  FROM sustentabilidade WHERE ID = %s", (id_excluir,))
                existe= cursor.fetchone()

                if existe:
                    cursor.execute("DELETE FROM sustentabilidade WHERE ID = %s", (id_excluir,))
                    conexao.commit()
                    print(f"\no registro com ID {id_excluir} foi excluido com sucesso!")

                else:
                    print(f"\no registro com ID {id_excluir} não existe na tabela!")
                
                #mostra tudo dnv
                deletar = input('\nDeseja apagar algum outro dado? \n tecle = S para >>>SIM<<   \t tecle = N para >>> NÃO<<:').upper()
                if deletar != 'S' and deletar != 'N':
                    print('Você saiu da função de deletar dado!')
                    deletar=False
                break

        case 3:#ALTERAR DADO INSERIDO\n
            pass
        case 4:#LISTA TABELA POR ID
            aux = int(input('Digite o ID que você deseja pesquisar: '))
            print("\nTABELA SUSTENTABILIDADE:")
            #tabela sustentabilidade
            cursor.execute("SELECT * FROM sustentabilidade WHERE ID = %s",(aux,))
            resultado = cursor.fetchall()
            num_registro = len(resultado)

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
                if linha[6] == 'S' or linha[7] == 'S': 
                    if linha[8] == 'S' or linha[9] == 'S' or linha[10] == 'S' or linha[11] == 'S':
                        media_transporte = "Moderada Sustentabilidade"
                    else:
                        media_transporte = "Baixa Sustentabilidade"
                elif linha[8] == 'S' or linha[9] == 'S' or linha[10] == 'S' or linha[11] == 'S':
                    media_transporte = "Alta Sustentabilidade" 

        case 5: #LISTAR MÉDIA\n
            cursor.execute("SELECT * FROM sustentabilidade")
            sustentabilidade = cursor.fetchall()
            for linha in sustentabilidade:
                soma_ca += linha[2]
                soma_ce += linha[5]
                soma_nrp += linha[4]
                soma_nrq += linha[3]
                num_registro += 1
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
            print(f"\nMÉDIAS DE REGISTROS:\nCA_RESULTADO: {soma_ca / num_registro : .1f}\nNR_QUANTIDADE: {soma_nrq / num_registro : .1f}\nNR_PORCENTAGEM: {soma_nrp / num_registro : .1f}\nCE_GASTO: {soma_ce / num_registro : .1f}")
        case 6:
            programaAtivo = False
            cursor.close()
            conexao.close()
            print (f'''conexão encerrada! \nObrigada por atualizar a tabela!''')
            break

'''# Exibir relatório
print("\n--- Relatório de Sustentabilidade ---")
print(f"Data: {DATA_}")
print(f"Consumo de água: {CA_RESULTADO}")
print(f"Consumo de energia: {CE_RESULTADO}")
print(f"Geração de resíduos: {NIVEL_NR_PORCENTAGEM}")
print(f"Uso de transporte: {NIVEL_TRANSPORTE}")
print("------------------------------------")
'''