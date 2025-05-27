import mysql.connector

<<<<<<< Updated upstream
programaAtivo = True

conexao = mysql.connector.connect(
    host="127.0.0.1",  # IP ou hostname do servidor MySQL puc-> BD-ACD
    user="root",  # "login"
    password="Miguel49*",  # senha
    database="PI"  # nome do banco (tem que existir) #BD170225416(isa)
=======
# --- Configuração da Cifra de Hill ---
MATRIZ_CHAVE = [[3, 5], [1, 2]]
DIMENSAO_MATRIZ = len(MATRIZ_CHAVE)
MODULO_ALFABETO = 26
MATRIZ_CHAVE_INVERSA = [[2, 21], [25, 3]]


def caractere_para_numero(valor_char):
    valor_char_upper = str(valor_char).upper()
    if 'A' <= valor_char_upper <= 'Y':
        return ord(valor_char_upper) - ord('A') + 1
    elif valor_char_upper == 'Z':
        return 0
    else:
        # Mapeia caracteres inesperados para 0 (como 'Z') silenciosamente
        # Isso é para evitar erros se dados não A-Z chegarem aqui,
        # especialmente durante a descriptografia de dados potencialmente corrompidos.
        return 0


def numero_para_caractere(valor_num):
    valor_num_mod = valor_num % MODULO_ALFABETO
    if 1 <= valor_num_mod <= 25:
        return chr(valor_num_mod - 1 + ord('A'))
    elif valor_num_mod == 0:
        return 'Z'
    return ''  # Retorna string vazia se algo muito errado acontecer


def preparar_texto_para_hill(texto, tamanho_bloco):
    texto_limpo = "".join(
        [char for char in str(texto).upper() if 'A' <= char <= 'Z'])

    resto = len(texto_limpo) % tamanho_bloco
    if resto != 0:
        preenchimento_necessario = tamanho_bloco - resto
        texto_limpo += 'X' * preenchimento_necessario
    return texto_limpo


def criptografar_texto_hill(texto_plano, matriz_chave_usada, dimensao_matriz_usada, modulo_usado):
    if not texto_plano:
        return ""

    texto_processado = preparar_texto_para_hill(
        texto_plano, dimensao_matriz_usada)
    if not texto_processado:
        return ""

    texto_numerico = [caractere_para_numero(c) for c in texto_processado]

    numeros_criptografados = []
    for i in range(0, len(texto_numerico), dimensao_matriz_usada):
        bloco = texto_numerico[i:i+dimensao_matriz_usada]
        segmento_bloco_criptografado = [0] * dimensao_matriz_usada
        for j_coluna in range(dimensao_matriz_usada):
            valor_soma = 0
            for k_elemento in range(dimensao_matriz_usada):
                valor_soma += bloco[k_elemento] * \
                    matriz_chave_usada[k_elemento][j_coluna]
            segmento_bloco_criptografado[j_coluna] = valor_soma % modulo_usado
        numeros_criptografados.extend(segmento_bloco_criptografado)

    return "".join([numero_para_caractere(n) for n in numeros_criptografados])


def descriptografar_texto_hill(texto_cifrado, matriz_chave_inversa_usada, dimensao_matriz_usada, modulo_usado):
    if not texto_cifrado:
        return ""

    texto_cifrado_str = str(texto_cifrado)  # Garante que é uma string
    cifra_numerica = [caractere_para_numero(c) for c in texto_cifrado_str]

    if len(cifra_numerica) % dimensao_matriz_usada != 0:
        # Se o comprimento do texto cifrado não for múltiplo da dimensão da matriz,
        # indica dados corrompidos ou erro no processo. Retorna o texto cifrado original.
        return texto_cifrado_str

    numeros_descriptografados = []
    for i in range(0, len(cifra_numerica), dimensao_matriz_usada):
        bloco = cifra_numerica[i:i+dimensao_matriz_usada]
        segmento_bloco_descriptografado = [0] * dimensao_matriz_usada
        for j_coluna in range(dimensao_matriz_usada):
            valor_soma = 0
            for k_elemento in range(dimensao_matriz_usada):
                valor_soma += bloco[k_elemento] * \
                    matriz_chave_inversa_usada[k_elemento][j_coluna]
            segmento_bloco_descriptografado[j_coluna] = valor_soma % modulo_usado
        numeros_descriptografados.extend(segmento_bloco_descriptografado)

    texto_descriptografado = "".join(
        [numero_para_caractere(n) for n in numeros_descriptografados])
    return texto_descriptografado

# --- Fim da Configuração da Cifra de Hill ---


programaAtivo = True

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Miguel49*",
    database="PI"
>>>>>>> Stashed changes
)
cursor = conexao.cursor()
print("Conectado com sucesso!")

<<<<<<< Updated upstream
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
=======
# Variáveis globais para médias, zeradas antes de cada cálculo no caso 5
soma_ca_global = 0
soma_ce_global = 0
soma_nrp_global = 0
soma_nrq_global = 0
num_registro_global = 0  # Esta não parece ser usada de forma global efetiva


def pausar():
    input("\nPressione [Enter] para continuar...")


while programaAtivo:
    print("""
    ╔══════════════════════════════════════════════════╗
    ║                       MENU PRINCIPAL             ║
    ╠══════════════════════════════════════════════════╣
    ║  1 ▸ Inserir registro                            ║
    ║  2 ▸ Deletar dado por ID                         ║
    ║  3 ▸ Alterar dado inserido                       ║
    ║  4 ▸ Listar tabelas                              ║
    ║  5 ▸ Listar média                                ║
    ║  6 ▸ Sair                                        ║
    ╚══════════════════════════════════════════════════╝
    """)
    entrada_menu_str = input("Escolha uma opção (1-6): ")
    if entrada_menu_str.isdigit():
        menu = int(entrada_menu_str)
    else:
        menu = -1  # Opção inválida para entrar no while de validação

    while menu < 1 or menu > 6:  # Ajustado para incluir 1 e 6 como válidos
        entrada_menu_str = input("Escolha uma opção válida! (1-6): ")
        if entrada_menu_str.isdigit():
            menu = int(entrada_menu_str)
        else:
            menu = -1

    match menu:
        case 1:  # inserir
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                    INSERIR REGISTRO              ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
>>>>>>> Stashed changes
            DATA_ = input("Qual é a data (AAAA-MM-DD)? ")
            CA_GASTO = float(
                input("Quantos litros de água você consumiu hoje? "))
            CE_GASTO = float(
                input("Quantos kWh de energia elétrica você consumiu hoje? "))
            NR_QUANTIDADE = float(
                input("Quantos KG de resíduos não reciclaveis você gerou hoje? "))
            NR_PORCENTAGEM = float(
                input("Qual a porcentagem de resíduos reciclados no total (em %)? "))

<<<<<<< Updated upstream
            # Entrada de múltiplos meios de transporte atualizada
=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            # not in ['S', 'N']:
=======
>>>>>>> Stashed changes
            while UT_TRANSPORTE_PUBLICO != 'S' and UT_TRANSPORTE_PUBLICO != 'N':
                UT_TRANSPORTE_PUBLICO = input(
                    f"\tDigite apenas S ou N. ").upper()
            UT_CARRO_ELETRICO = input(f"\t5. Carro elétrico ").upper()
            while UT_CARRO_ELETRICO != 'S' and UT_CARRO_ELETRICO != 'N':
                UT_CARRO_ELETRICO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CAMINHADA = input(f"\t6. Caminhada ").upper()
            while UT_CAMINHADA != 'S' and UT_CAMINHADA != 'N':
                UT_CAMINHADA = input(f"\tDigite apenas S ou N. ").upper()

<<<<<<< Updated upstream
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
=======
            if CA_GASTO < 150:
                CA_RESULTADO_ORIGINAL = "Alta Sustentabilidade"
            elif 150 <= CA_GASTO <= 200:
                CA_RESULTADO_ORIGINAL = "Moderada Sustentabilidade"
            else:
                CA_RESULTADO_ORIGINAL = "Baixa Sustentabilidade"

            if CE_GASTO < 5:
                CE_RESULTADO_ORIGINAL = "Alta Sustentabilidade"
            elif 5 <= CE_GASTO <= 10:
                CE_RESULTADO_ORIGINAL = "Moderada Sustentabilidade"
            else:
                CE_RESULTADO_ORIGINAL = "Baixa Sustentabilidade"

            if NR_PORCENTAGEM > 50:
                NIVEL_NR_PORCENTAGEM_ORIGINAL = "Alta Sustentabilidade"
            elif 20 <= NR_PORCENTAGEM <= 50:
                NIVEL_NR_PORCENTAGEM_ORIGINAL = "Moderada Sustentabilidade"
            else:
                NIVEL_NR_PORCENTAGEM_ORIGINAL = "Baixa Sustentabilidade"

            NIVEL_TRANSPORTE_ORIGINAL = "Baixa Sustentabilidade"
            if UT_CARRO == 'S' or UT_CARONA_COMPARTILHADA == 'S':
                if UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S' or UT_CAMINHADA == 'S':
                    NIVEL_TRANSPORTE_ORIGINAL = "Moderada Sustentabilidade"
            elif UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S' or UT_CAMINHADA == 'S':
                NIVEL_TRANSPORTE_ORIGINAL = "Alta Sustentabilidade"

>>>>>>> Stashed changes
            cursor.execute(("""INSERT INTO sustentabilidade 
            (DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO,
            UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA, UT_TRANSPORTE_PUBLICO, UT_CARRO_ELETRICO, 
            UT_CAMINHADA)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """),
                           (DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO, UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA,
                            UT_TRANSPORTE_PUBLICO, UT_CARRO_ELETRICO, UT_CAMINHADA))
<<<<<<< Updated upstream
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

=======

            CA_RESULTADO_CRIPT = criptografar_texto_hill(
                CA_RESULTADO_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
            NIVEL_NR_PORCENTAGEM_CRIPT = criptografar_texto_hill(
                NIVEL_NR_PORCENTAGEM_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
            CE_RESULTADO_CRIPT = criptografar_texto_hill(
                CE_RESULTADO_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
            NIVEL_TRANSPORTE_CRIPT = criptografar_texto_hill(
                NIVEL_TRANSPORTE_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)

            cursor.execute(("""INSERT INTO resultados
                                (DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO)
                                VALUES(%s, %s, %s, %s, %s)"""),
                           (DATA_, CA_RESULTADO_CRIPT, NIVEL_NR_PORCENTAGEM_CRIPT, CE_RESULTADO_CRIPT, NIVEL_TRANSPORTE_CRIPT))
            conexao.commit()
            print('Dados inseridos com sucesso!')
            pausar()
        case 2:  # DELETAR ALGUM DADO POR ID
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                   DELETAR DADO POR ID            ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
            deletar = True
            while deletar:
                id_excluir_str = input("Digite o ID que deseja excluir: ")
                if id_excluir_str.isdigit():
                    id_excluir = int(id_excluir_str)
                    cursor.execute(
                        "SELECT * FROM sustentabilidade WHERE ID = %s", (id_excluir,))
                    existe = cursor.fetchone()
                    if existe:
                        cursor.execute(
                            "DELETE FROM resultados WHERE ID = %s", (id_excluir,))
                        cursor.execute(
                            "DELETE FROM sustentabilidade WHERE ID = %s", (id_excluir,))
                        conexao.commit()
                        print(
                            f"\nO registro com ID {id_excluir} foi excluido com sucesso!")
                    else:
                        print(
                            f"\nO registro com ID {id_excluir} não existe na tabela!")
                else:
                    print("ID inválido. Por favor, insira um número.")

                deletarN = input(
                    '\nDeseja apagar algum outro dado? \n tecle = S para >>>SIM<<      tecle = N para >>> NÃO<<:').upper()
                while deletarN != 'S' and deletarN != 'N':
                    deletarN = input(
                        '\nDeseja apagar algum outro dado? \n tecle = S para >>>SIM<<      tecle = N para >>> NÃO<<:').upper()
                if deletarN == 'N':
                    deletar = False
            pausar()
        case 3:  # ALTERAR DADO INSERIDO
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                  ALTERAR DADO INSERIDO           ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
            alterar = True
            while alterar:
                aux_str = input('Digite o ID que você deseja alterar: ')
                if aux_str.isdigit():
                    aux = int(aux_str)
                    cursor.execute(
                        "SELECT * FROM sustentabilidade WHERE ID = %s", (aux,))
                    existe = cursor.fetchone()
                    if existe:
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
                        UT_CARRO = input(
                            f"\t1. Carro (combustível fósseis) ").upper()
                        while UT_CARRO != 'S' and UT_CARRO != 'N':
                            UT_CARRO = input(
                                f"\tDigite apenas S ou N. ").upper()
                        # ... (repetir validação para outros UT_*)

                        if CA_GASTO < 150:
                            CA_RESULTADO_ORIGINAL = "Alta Sustentabilidade"
                        elif 150 <= CA_GASTO <= 200:
                            CA_RESULTADO_ORIGINAL = "Moderada Sustentabilidade"
                        else:
                            CA_RESULTADO_ORIGINAL = "Baixa Sustentabilidade"

                        if CE_GASTO < 5:
                            CE_RESULTADO_ORIGINAL = "Alta Sustentabilidade"
                        elif 5 <= CE_GASTO <= 10:
                            CE_RESULTADO_ORIGINAL = "Moderada Sustentabilidade"
                        else:
                            CE_RESULTADO_ORIGINAL = "Baixa Sustentabilidade"

                        if NR_PORCENTAGEM > 50:
                            NIVEL_NR_PORCENTAGEM_ORIGINAL = "Alta Sustentabilidade"
                        elif 20 <= NR_PORCENTAGEM <= 50:
                            NIVEL_NR_PORCENTAGEM_ORIGINAL = "Moderada Sustentabilidade"
                        else:
                            NIVEL_NR_PORCENTAGEM_ORIGINAL = "Baixa Sustentabilidade"

                        # Lógica de transporte aqui...
                        NIVEL_TRANSPORTE_ORIGINAL = "Baixa Sustentabilidade"
                        if UT_CARRO == 'S' or UT_CARONA_COMPARTILHADA == 'S':
                            if UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S' or UT_CAMINHADA == 'S':
                                NIVEL_TRANSPORTE_ORIGINAL = "Moderada Sustentabilidade"
                        elif UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S' or UT_CAMINHADA == 'S':
                            NIVEL_TRANSPORTE_ORIGINAL = "Alta Sustentabilidade"

                        cursor.execute("UPDATE sustentabilidade SET DATA_ = %s, CA_GASTO = %s, NR_QUANTIDADE = %s, NR_PORCENTAGEM = %s, CE_GASTO = %s,UT_CARRO = %s, UT_CARONA_COMPARTILHADA = %s, UT_BICICLETA = %s, UT_TRANSPORTE_PUBLICO = %s, UT_CARRO_ELETRICO = %s, UT_CAMINHADA = %s WHERE ID = %s",
                                       (DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO, UT_CARRO, "S", "N", "S", "N", "S", aux))  # Exemplo, corrigir os valores de UT_*

                        CA_RESULTADO_CRIPT = criptografar_texto_hill(
                            CA_RESULTADO_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                        NIVEL_NR_PORCENTAGEM_CRIPT = criptografar_texto_hill(
                            NIVEL_NR_PORCENTAGEM_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                        CE_RESULTADO_CRIPT = criptografar_texto_hill(
                            CE_RESULTADO_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                        NIVEL_TRANSPORTE_CRIPT = criptografar_texto_hill(
                            NIVEL_TRANSPORTE_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)

                        cursor.execute(("""UPDATE resultados
                                            SET DATA_ = %s, CA_RESULTADO = %s, NR_RESULTADO = %s, 
                                            CE_RESULTADO = %s, UT_RESULTADO = %s
                                            WHERE ID = %s"""),
                                       (DATA_, CA_RESULTADO_CRIPT, NIVEL_NR_PORCENTAGEM_CRIPT, CE_RESULTADO_CRIPT, NIVEL_TRANSPORTE_CRIPT, aux))
                        conexao.commit()
                        print(f'\nO ID {aux} foi alterado com sucesso!')
                    else:
                        print(f'\nID não encontrado!')
                else:
                    print("ID inválido. Por favor, insira um número.")

                alterarN = input(
                    '\nDeseja alterar algum outro dado? \n tecle = S para >>>SIM<<      tecle = N para >>> NÃO<<:').upper()
                while alterarN != 'S' and alterarN != 'N':
                    alterarN = input(
                        '\nDeseja alterar algum outro dado? \n tecle = S para >>>SIM<<      tecle = N para >>> NÃO<<:').upper()
                if alterarN == 'N':
                    alterar = False
            pausar()
        case 4:  # LISTA TABELA POR ID
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                      LISTAR TABELAS              ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
            print("\nTABELA SUSTENTABILIDADE:")
            cursor.execute("SELECT * FROM sustentabilidade")
            resultado_sust = cursor.fetchall()
            for linha in resultado_sust:
                print(f"""\n 
            ID: {linha[0]}, Data: {linha[1]}, Água (L): {linha[2]}, Res.NãoRec (kg): {linha[3]},
            Res.Rec (%): {linha[4]}, Energia (kW): {linha[5]}, Carro: {linha[6]}, Carona: {linha[7]},
            Bicicleta: {linha[8]}, Transp.Púb: {linha[9]}, CarroElét: {linha[10]}, Caminhada: {linha[11]}""")
            pausar()
            print("\nTABELA RESULTADOS (dados descriptografados): ")
            cursor.execute(
                "SELECT ID, DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO FROM resultados")
            resultado_res = cursor.fetchall()
            for linha_res in resultado_res:
                id_db, data_db, ca_cript, nr_cript, ce_cript, ut_cript = linha_res

                CA_RESULTADO_DESCRIPT = descriptografar_texto_hill(
                    ca_cript, MATRIZ_CHAVE_INVERSA, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                NR_RESULTADO_DESCRIPT = descriptografar_texto_hill(
                    nr_cript, MATRIZ_CHAVE_INVERSA, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                CE_RESULTADO_DESCRIPT = descriptografar_texto_hill(
                    ce_cript, MATRIZ_CHAVE_INVERSA, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                UT_RESULTADO_DESCRIPT = descriptografar_texto_hill(
                    ut_cript, MATRIZ_CHAVE_INVERSA, DIMENSAO_MATRIZ, MODULO_ALFABETO)

                print(f"""\n
            ID: {id_db}, Data: {data_db}
            \t Uso de água: {CA_RESULTADO_DESCRIPT}
            \t Reciclagem de resíduos: {NR_RESULTADO_DESCRIPT}
            \t Uso de eletricidade: {CE_RESULTADO_DESCRIPT}
            \t Uso de transportes: {UT_RESULTADO_DESCRIPT}""")
            pausar()
        case 5:  # LISTAR MÉDIA
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                       LISTAR MÉDIA                      ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
            soma_ca_local = 0  # Usar variáveis locais para o cálculo da média
            soma_ce_local = 0
            soma_nrp_local = 0
            soma_nrq_local = 0
            num_registros_media = 0

            cursor.execute(
                "SELECT CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO FROM sustentabilidade")
            registros_sustentabilidade = cursor.fetchall()

            if not registros_sustentabilidade:
                print("\nNão há registros para calcular a média.")
            else:
                for linha_sust in registros_sustentabilidade:
                    soma_ca_local += float(linha_sust[0])
                    soma_nrq_local += float(linha_sust[1])
                    soma_nrp_local += float(linha_sust[2])
                    soma_ce_local += float(linha_sust[3])
                    num_registros_media += 1

                print(
                    f"\n\tMÉDIAS DE REGISTROS ({num_registros_media} registros):")
                if num_registros_media > 0:
                    print(
                        f"\tÁgua utilizada: (L) {soma_ca_local / num_registros_media : .1f}")
                    print(
                        f"\tResíduos não recicláveis: (kg) {soma_nrq_local / num_registros_media : .1f}")
                    print(
                        f"\tResíduos reciclados: (%) {soma_nrp_local / num_registros_media : .1f}")
                    print(
                        f"\tEnergia consumida: (kW) {soma_ce_local / num_registros_media : .1f}")
            pausar()
>>>>>>> Stashed changes
        case 6:
            programaAtivo = False
            cursor.close()
            conexao.close()
<<<<<<< Updated upstream
            print(f'''conexão encerrada! \nObrigada por atualizar a tabela!''')
=======
            print(f'''Conexão encerrada! \nObrigada por atualizar a tabela!''')
>>>>>>> Stashed changes
            break
