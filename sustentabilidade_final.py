import mysql.connector

programaAtivo = True

conexao = mysql.connector.connect(
    host="127.0.0.1",  # IP ou hostname do servidor MySQL puc-> BD-ACD
    user="root",  # "login"
    password="Miguel49*",  # senha
    database="PI"  # nome do banco (tem que existir) #BD170225416(isa)
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
        6 ->   SAIR \n '''))
    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5 and menu != 6:
        menu = int(input(f'''Função fora do escopo! Digite uma função válida:\n
        1 ->  INSERIR REGISTO\n
        2 ->  DELETAR ALGUM DADO POR ID\n
        3 ->  ALTERAR DADO INSERIDO\n
        4 ->  LISTA TABELA POR ID\n
        5 ->  LISTAR MÉDIA\n
        6 ->   SAIR \n '''))
    # Coletando os dados do usuário
    match menu:
        case 1:  # inserir
            DATA_ = input("Qual é a data (AAAA-MM-DD)? ")
            CA_GASTO = float(
                input("Quantos litros de água você consumiu hoje? "))
            CE_GASTO = float(
                input("Quantos kWh de energia elétrica você consumiu hoje? "))
            NR_QUANTIDADE = float(
                input("Quantos KG de resíduos não reciclaveis você gerou hoje? "))
            NR_PORCENTAGEM = float(
                input("Qual a porcentagem de resíduos reciclados no total (em %)? "))

            # Entrada de múltiplos meios de transporte atualizada
            print(
                f"\nEscolha os meios de transporte utilizados hoje: Responda apenas com S ou N.")
            UT_CARRO = input(f"\t1. Carro (combustível fósseis) ").upper()
            while UT_CARRO != 'S' and UT_CARRO != 'N':
                UT_CARRO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CARONA_COMPARTILHADA = input(
                f"\t2. Carona compartilhada ").upper()
            while UT_CARONA_COMPARTILHADA != 'S' and UT_CARONA_COMPARTILHADA != 'N':
                UT_CARONA_COMPARTILHADA = input(
                    f"\tDigite apenas S ou N. ").upper()
            UT_BICICLETA = input(f"\t3. Bicicleta ").upper()
            while UT_BICICLETA != 'S' and UT_BICICLETA != 'N':
                UT_BICICLETA = input(f"\tDigite apenas S ou N. ").upper()
            UT_TRANSPORTE_PUBLICO = input(
                f"\t4. Transporte público (ônibus, metrô, trem) ").upper()
            # not in ['S', 'N']:
            while UT_TRANSPORTE_PUBLICO != 'S' and UT_TRANSPORTE_PUBLICO != 'N':
                UT_TRANSPORTE_PUBLICO = input(
                    f"\tDigite apenas S ou N. ").upper()
            UT_CARRO_ELETRICO = input(f"\t5. Carro elétrico ").upper()
            while UT_CARRO_ELETRICO != 'S' and UT_CARRO_ELETRICO != 'N':
                UT_CARRO_ELETRICO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CAMINHADA = input(f"\t6. Caminhada ").upper()
            while UT_CAMINHADA != 'S' and UT_CAMINHADA != 'N':
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
            elif UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S' or UT_CAMINHADA == 'S':
                NIVEL_TRANSPORTE = "Alta Sustentabilidade"

            # inserir dados na tabela SUSTENTABILIDADE
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
            print('\nDados inseridos com sucesso!')
            tecle = input('>>ENTER<<')
        case 2:  # DELETAR ALGUM DADO POR ID

            id_excluir = int(input("digite o ID que deseja excluir: "))
            cursor.execute(
                "SELECT *  FROM sustentabilidade WHERE ID = %s", (id_excluir,))
            existe = cursor.fetchone()

            if existe:
                cursor.execute(
                    "DELETE FROM sustentabilidade WHERE ID = %s", (id_excluir,))
                conexao.commit()
                print(
                    f"\no registro com ID {id_excluir} foi excluido com sucesso!")

            else:
                print(
                    f"\no registro com ID {id_excluir} não existe na tabela!")
            tecle = input('>>ENTER<<')

        case 3:  # ALTERAR DADO INSERIDO\n
            print("\nTABELA SUSTENTABILIDADE:")
            cursor.execute('SELECT * FROM sustentabilidade')
            while True:
                try:
                    id = int(input('Digite o ID que você deseja alterar: '))
                    break
                except ValueError:
                    print('ID inválido. Por favor, digite um número inteiro.')

            while True:
                try:
                    menu_alteracao = int(
                        input('O que você deseja alterar? (selecione 1, 2 ou 3)\n'
                              '1. Todas as colunas da linha\n'
                              '2. Apenas uma coluna\n'
                              '3. Mais de uma coluna\n')
                    )
                    if 1 <= menu_alteracao <= 3:
                        break  # Sai do loop se a seleção do menu for válida
                    else:
                        print('Seleção inválida. Por favor, digite 1, 2 ou 3.')
                except ValueError:
                    print('Seleção inválida. Por favor, digite um número inteiro.')
            if menu_alteracao == 1:
                ID_ = int(input('Digite o id a ser alterado: '))
                DATA_ = input("Qual é a data (AAAA-MM-DD)? ")
                CA_GASTO = float(
                    input("Quantos litros de água você consumiu hoje? "))
                CE_GASTO = float(
                    input("Quantos kWh de energia elétrica você consumiu hoje? "))
                NR_QUANTIDADE = float(
                    input("Quantos KG de resíduos não reciclaveis você gerou hoje? "))
                NR_PORCENTAGEM = float(
                    input("Qual a porcentagem de resíduos reciclados no total (em %)? "))
                print(
                    f"\nEscolha os meios de transporte utilizados hoje: Responda apenas com S ou N.")
                UT_CARRO = input(f"\t1. Carro (combustível fósseis) ").upper()
                while UT_CARRO != 'S' and UT_CARRO != 'N':
                    UT_CARRO = input(f"\tDigite apenas S ou N. ").upper()
                UT_CARONA_COMPARTILHADA = input(
                    f"\t2. Carona compartilhada ").upper()
                while UT_CARONA_COMPARTILHADA != 'S' and UT_CARONA_COMPARTILHADA != 'N':
                    UT_CARONA_COMPARTILHADA = input(
                        f"\tDigite apenas S ou N. ").upper()
                UT_BICICLETA = input(f"\t3. Bicicleta ").upper()
                while UT_BICICLETA != 'S' and UT_BICICLETA != 'N':
                    UT_BICICLETA = input(f"\tDigite apenas S ou N. ").upper()
                UT_TRANSPORTE_PUBLICO = input(
                    f"\t4. Transporte público (ônibus, metrô, trem) ").upper()
                # not in ['S', 'N']:
                while UT_TRANSPORTE_PUBLICO != 'S' and UT_TRANSPORTE_PUBLICO != 'N':
                    UT_TRANSPORTE_PUBLICO = input(
                        f"\tDigite apenas S ou N. ").upper()
                UT_CARRO_ELETRICO = input(f"\t5. Carro elétrico ").upper()
                while UT_CARRO_ELETRICO != 'S' and UT_CARRO_ELETRICO != 'N':
                    UT_CARRO_ELETRICO = input(
                        f"\tDigite apenas S ou N. ").upper()
                UT_CAMINHADA = input(f"\t6. Caminhada ").upper()
                while UT_CAMINHADA != 'S' and UT_CAMINHADA != 'N':
                    UT_CAMINHADA = input(f"\tDigite apenas S ou N. ").upper()
                sql = 'UPDATE sustentabiliidade set DATA_ = %s, CA_GASTO = %s, NR_QUANTIDADE = %s, NR_PORCENTAGEM = %s CE_GASTO = %s, UT_CARRO = %s, UT_CARONA_COMPARTILHADA = %s, UT_BICICLETA = %s, UT_TRANSPORTE_PUBLICO = %s, UT_CARRO_ELETRICO = %s, UT_CAMINHADA = %s WHERE ID = %s'
                valores = (DATA_, CA_GASTO, CE_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM,
                           UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA, UT_TRANSPORTE_PUBLICO, UT_CARRO_ELETRICO, UT_CAMINHADA, ID_)
                cursor.execute(sql, valores)
                conexao.commit()
                print("Dados inseridos com sucesso!")
            elif menu_alteracao == 2:
                ID_ = int(input('Digite o ID a ser alterado: '))
                coluna = input('''digite o número da coluna  correspondente que você deseja alterar:
                                  1 - DATA_\n
                                  2 - CA_GASTO\n
                                  3 - CE_GASTO\n
                                  4 - NR_QUANTIDADE\n
                                  5 - NR_PORCENTAGEM\n  
                                  6 - UT_CARRO\n
                                  7 - UT_CARONA_COMPARTILHADA\n
                                  8 - UT_BICICLETA\n
                                  9 -  UT_TRANSPORTE_PUBLICO\n
                                 10 - UT_CARRO_ELETRICO\n
                                 11- UT_CAMINHADA\n
                               ''')
                while true

        case 4:  # LISTA TABELA POR ID
            aux = int(input('Digite o ID que você deseja pesquisar: '))
            print("\nTABELA SUSTENTABILIDADE:")
            # tabela sustentabilidade
            cursor.execute(
                "SELECT * FROM sustentabilidade WHERE ID = %s", (aux,))
            resultado = cursor.fetchall()
            num_registro = len(resultado)

            for linha in resultado:
                print(f"""\n 
            ID: {linha[0]}
            \t DATA: {linha[1]}
            \t Consumo de água: {linha[2]}
            \t Quantidade de resíduos não reciclaveis gerados (em KG): {linha[3]}
            \t Nível de resíduos reciclados no total (em %): {linha[4]}
            \t Consumo de energia: {linha[5]}
            \t Uso do Transporte - CARRO: {linha[6]}
            \t Uso do Transporte - CARONA COMPARTILHADA: {linha[7]}
            \t Uso do Transporte - BICICLETA: {linha[8]}
            \t Uso do Transporte - TRANSPORTE PÚBLICO: {linha[9]}
            \t Uso do Transporte - CARRO ELÉTRICO: {linha[10]}
            \t Uso do Transporte - CAMINHADA: {linha[11]}""")

            tecle = input('>>ENTER<<')

        case 5:  # LISTAR MÉDIA\n

            id = int(
                input('Digite o ID que você deseja consultar sua média de sustentabilidade: '))
            cursor.execute(
                "SELECT * FROM sustentabilidade WHERE ID = %s", (id,))
            resultado = cursor.fetchall()

            for linha in resultado:
                if linha[6] == 'S' or linha[7] == 'S':
                    if linha[8] == 'S' or linha[9] == 'S' or linha[10] == 'S' or linha[11] == 'S':
                        UT_RESULTADO = "Moderada Sustentabilidade"
                    else:
                        UT_RESULTADO = "Baixa Sustentabilidade"
                elif linha[8] == 'S' or linha[9] == 'S' or linha[10] == 'S' or linha[11] == 'S':
                    UT_RESULTADO = "Alta Sustentabilidade"
                else:
                    UT_RESULTADO = "Baixa Sustentabilidade"

                cursor.execute("""INSERT INTO resultados (ID, DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO)
                      VALUES (%s, %s, %s, %s, %s, %s)""",
                               (linha[0], linha[1], linha[2], linha[3], linha[5], UT_RESULTADO))
                # MS_RESULTADO

                conexao.commit()

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
            ID:\t{linha[0]}
            \t DATA:\t{linha[1]}
            \t Consumo de água - nível de média: \t{linha[2]}
            \t Resíduos reciclados - nível de média: \t{linha[3]}
            \t Consumo de energia - nível de média:\t{linha[4]}
            \t Uso de Transporte - nível de média:\t{linha[5]}""")
            print(f"""\n\tMÉDIAS DE REGISTROS:\n
                Consumo de água - nível de sustentabilidade: \t\t{soma_ca / num_registro : .1f}
                Resíduos não reciclados(KG) - nível de sustentabilidade:{soma_nrq / num_registro : .1f}
                Resíduos reciclados - nível de sustentabilidade: \t{soma_nrp / num_registro : .1f}
                Consumo de energia - nível de sustentabilidade: \t{soma_ce / num_registro : .1f}""")
            # FALTA A MÉDIA FINAL DO DIA = MS_RESULTADO

            # delete na tabela p/ quando for fazer a consulta dnv só exibir o id q a gnt quer, mas não sei como vai ficar a média...
            # essa média seria por tipo mês? pq se sim, apaga isso de delete e aparece TODOS os registros da tabela resultados q foi consultado
            # e faz o calculo da media, se não, nem precisa ter, MAS como esse case é pra média, teria q tirar o aux pra puxar todos os IDs
            # da tabela sustentabilidade... não sei
            cursor.execute("delete from resultados")
            conexao.commit()

            tecle = input('>>ENTER<<')

        case 6:
            programaAtivo = False
            cursor.close()
            conexao.close()
            print(f'''conexão encerrada! \nObrigada por atualizar a tabela!''')
            break
