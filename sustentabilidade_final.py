import mysql.connector
programaAtivo = True
conexao = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Iqpqy2",
    database="PI"
)
cursor = conexao.cursor()
print("Conectado com sucesso!")
while programaAtivo:
    menu = int(input(f"""\n
    1. Inserir
                     """))
    # Coletando os dados do usuário
    match menu:
        case 1:
            DATA_ = input("Qual é a data (DD/MM/AAAA)? ")
            CA_GASTO = float(input("Quantos litros de água você consumiu hoje? "))
            CE_GASTO = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
            NR_QUANTIDADE =float(input("Quantos KG de resíduos não reciclaveis você gerou hoje? "))
            NR_PORCENTAGEM = float(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))

            #Entrada de múltiplos meios de transporte atualizada
            print(f"\nEscolha os meios de transporte utilizados hoje: Responda apenas com S ou N.")
            UT_TRANSPORTE_PUBLICO = input(f"\t1. Transporte público (ônibus, metrô, trem) ")
            while UT_TRANSPORTE_PUBLICO != 'S' and UT_TRANSPORTE_PUBLICO != 'N':
                UT_TRANSPORTE_PUBLICO = input(f"\tDigite apenas S ou N. ")
            UT_BICICLETA = input(f"\t2. Bicicleta ")
            while UT_BICICLETA != 'S' and UT_BICICLETA != 'N':
                UT_BICICLETA = input(f"\tDigite apenas S ou N. ")
            UT_CAMINHADA = input(f"\t3. UT_CAMINHADA ")
            while UT_CAMINHADA != 'S' and UT_CAMINHADA != 'N':
                UT_CAMINHADA = input(f"\tDigite apenas S ou N. ")
            UT_CARRO = input(f"\t4. UT_CARRO (combustível fósseis) ")
            while UT_CARRO != 'S' and UT_CARRO != 'N':
                UT_CARRO = input(f"\tDigite apenas S ou N. ")
            UT_CARRO_ELETRICO = input(f"\t5. UT_CARRO elétrico ")
            while UT_CARRO_ELETRICO != 'S' and UT_CARRO_ELETRICO != 'N':
                UT_CARRO_ELETRICO = input(f"\tDigite apenas S ou N. ")
            UT_CARONA_COMPARTILHADA = input(f"\t6. Carona compartilhada ")
            while UT_CARONA_COMPARTILHADA != 'S' and UT_CARONA_COMPARTILHADA != 'N':
                UT_CARONA_COMPARTILHADA = input(f"\tDigite apenas S ou N. ")
            if agua < 150:
                CA_RESULTADO = "Alta Sustentabilidade"
            elif 150 <= agua <= 200:
                CA_RESULTADO = "Moderada Sustentabilidade"
            else:
                CA_RESULTADO = "Baixa Sustentabilidade"

            # Classificação de consumo de energia
            if energia < 5:
                class_energia = "Alta Sustentabilidade"
            elif 5 <= energia <= 10:
                class_energia = "Moderada Sustentabilidade"
            else:
                class_energia = "Baixa Sustentabilidade"


            # Classificação de resíduos recicláveis
            if percentual_reciclado > 50:
                class_residuos = "Alta Sustentabilidade"
            elif 20 <= percentual_reciclado <= 50:
                class_residuos = "Moderada Sustentabilidade"
            else:
                class_residuos = "Baixa Sustentabilidade"

            # Classificação do transporte atualizada
            if carro == 'S' or carona_compartilhada == 'S':
                if bicleta == 'S' or transporte_publico == 'S' or carro_eletrico == 'S' or caminhada == 'S':
                    class_transporte = "Moderada Sustentabilidade"
                else:
                    class_transporte = "Baixa Sustentabilidade"
            elif bicleta == 'S' or transporte_publico == 'S' or carro_eletrico == 'S'or caminhada == 'S':
                class_transporte = "Alta Sustentabilidade"
            cursor.execute("""INSERT INTO sustentabilidade(DATA_,
                            \nCA_GASTO,
                            \nNR_QUANTIDADE,
                            \nNR_PORCENTAGEM,
                            \nCE_GASTO,
                            \nUT_CARRO,
                            \nUT_CARONA_COMPARTILHADA,
                            \nUT_BICICLETA,
                            \nUT_TRANSPORTE_PUBLICO,
                            \nUT_CARRO_ELETRICO,
                            \nUT_CAMINHADA) 
                            \nVALUES(%s
                            \n%s
                            \n%s
                            \n%s
                            \n%s
                            \n%s
                            \n%s
                            \n%s
                            \n%s
                            \n%s
                           )
""",(DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO, UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA, UT_TRANSPORTE_PUBLICO,UT_CARRO_ELETRICO, UT_CAMINHADA))
        case 4:
            print("\nTABELA SUSTENTABILIDADE:")
            #tabela sustentabilidade
            cursor.execute("SELECT * FROM sustentabilidade")
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
        case 5:
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
        
# Classificação de consumo de água



# Exibir relatório
print("\n--- Relatório de Sustentabilidade ---")
print(f"Data: {data}")
print(f"Consumo de água: {CA_RESULTADO}")
print(f"Consumo de energia: {class_energia}")
print(f"Geração de resíduos: {class_residuos}")
print(f"Uso de transporte: {class_transporte}")
print("------------------------------------")
