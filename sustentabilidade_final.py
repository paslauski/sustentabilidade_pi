import mysql.connector
#concertar descriptografia palavra impar
#mostrar classificacao da media

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
        return 0

def numero_para_caractere(valor_num):
    valor_num_mod = valor_num % MODULO_ALFABETO
    if 1 <= valor_num_mod <= 25:
        return chr(valor_num_mod - 1 + ord('A'))
    elif valor_num_mod == 0:
        return 'Z'
    return ''

def preparar_texto_para_hill(texto, tamanho_bloco):
    texto_processado = "".join([char for char in str(texto).upper() if 'A' <= char <= 'Z'])

    if not texto_processado:
        return ""

    if len(texto_processado) % 2 != 0:
        texto_processado = texto_processado + 'W'
        texto_processado = texto_processado[:-1]

    if not texto_processado:
        texto_processado = 'X' * tamanho_bloco
    else:
        resto_final = len(texto_processado) % tamanho_bloco
        if resto_final != 0:
            preenchimento_necessario = tamanho_bloco - resto_final
            texto_processado += 'X' * preenchimento_necessario
            
    return texto_processado

def criptografar_texto_hill(texto_plano, matriz_chave_usada, dimensao_matriz_usada, modulo_usado):
    if not texto_plano: 
        return ""
    
    texto_processado = preparar_texto_para_hill(texto_plano, dimensao_matriz_usada)
    if not texto_processado: 
        return ""

    texto_numerico = [caractere_para_numero(c) for c in texto_processado]
    
    numeros_criptografados = []
    for i in range(0, len(texto_numerico), dimensao_matriz_usada):
        bloco = texto_numerico[i:i+dimensao_matriz_usada]
        segmento_bloco_criptografado = [0] * dimensao_matriz_usada
        for j_linha in range(dimensao_matriz_usada):  # Itera nas linhas da matriz chave
            valor_soma = 0
            for k_elemento in range(dimensao_matriz_usada): # Faz o produto escalar
                # --- LINHA CORRIGIDA ---
                valor_soma += matriz_chave_usada[j_linha][k_elemento] * bloco[k_elemento]
            segmento_bloco_criptografado[j_linha] = valor_soma % modulo_usado
        numeros_criptografados.extend(segmento_bloco_criptografado)
            
    return "".join([numero_para_caractere(n) for n in numeros_criptografados])

def descriptografar_texto_hill(texto_cifrado, matriz_chave_inversa_usada, dimensao_matriz_usada, modulo_usado):
    if not texto_cifrado: 
        return ""

    texto_cifrado_str = str(texto_cifrado) 
    cifra_numerica = [caractere_para_numero(c) for c in texto_cifrado_str]
    
    # Adicionada uma verificação para evitar erros com textos que não são múltiplos do bloco
    if len(cifra_numerica) % dimensao_matriz_usada != 0:
        # Tenta preencher se o tamanho for ímpar, um cenário comum
        if len(cifra_numerica) % 2 != 0:
             cifra_numerica.append(caractere_para_numero('X'))
        else:
             return texto_cifrado_str # Retorna o texto original se não for possível corrigir

    numeros_descriptografados = []
    for i in range(0, len(cifra_numerica), dimensao_matriz_usada):
        bloco = cifra_numerica[i:i+dimensao_matriz_usada]
        segmento_bloco_descriptografado = [0] * dimensao_matriz_usada
        for j_linha in range(dimensao_matriz_usada): # Itera nas linhas da matriz chave
            valor_soma = 0
            for k_elemento in range(dimensao_matriz_usada): # Faz o produto escalar
                # --- LINHA CORRIGIDA ---
                valor_soma += matriz_chave_inversa_usada[j_linha][k_elemento] * bloco[k_elemento]
            segmento_bloco_descriptografado[j_linha] = valor_soma % modulo_usado
        numeros_descriptografados.extend(segmento_bloco_descriptografado)

    texto_descriptografado = "".join([numero_para_caractere(n) for n in numeros_descriptografados])

    # Remove o caractere de preenchimento 'X' se ele existir no final
    while texto_descriptografado.endswith("X"):
        texto_descriptografado = texto_descriptografado[:-1]

    return texto_descriptografado

programaAtivo = True

conexao = mysql.connector.connect(
    host="localhost", # IP ou hostname do servidor MySQL puc-> BD-ACD   localhost
    user="root", # "login" root
    password="lqpqy2", # senha
    database="PI" # nome do banco (tem que existir) #BD170225416(isa)
)
cursor = conexao.cursor()
print("Conectado com sucesso!")

soma_ca_global = 0
soma_ce_global = 0
soma_nrp_global = 0
soma_nrq_global = 0
num_registro_global = 0

def pausar():
    input("\nPressione [Enter] para continuar...")

while programaAtivo:
    print("""
    ╔══════════════════════════════════════════════════╗
    ║                      MENU PRINCIPAL                      ║
    ╠══════════════════════════════════════════════════╣
    ║   1 ▸ Inserir registro                             ║
    ║   2 ▸ Deletar dado por ID                          ║
    ║   3 ▸ Alterar dado inserido                        ║
    ║   4 ▸ Listar tabelas                               ║
    ║   5 ▸ Listar média                                 ║
    ║   6 ▸ Sair                                         ║
    ╚══════════════════════════════════════════════════╝
    """)
    entrada_menu_str = input("Escolha uma opção (1-6): ")
    if entrada_menu_str.isdigit():
        menu = int(entrada_menu_str)
    else:
        menu = -1

    while menu < 1 or menu > 6 :
        entrada_menu_str = input("Escolha uma opção válida! (1-6): ")
        if entrada_menu_str.isdigit():
            menu = int(entrada_menu_str)
        else:
            menu = -1
            
    match menu:
        case 1: #inserir
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                     INSERIR REGISTRO                     ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
            DATA_ = input("Qual é a data (AAAA-MM-DD)? ")
            CA_GASTO = float(input("Quantos litros de água você consumiu hoje? "))
            CE_GASTO = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
            NR_QUANTIDADE =float(input("Quantos KG de resíduos não reciclaveis você gerou hoje? "))
            NR_PORCENTAGEM = float(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))

            print(f"\nEscolha os meios de transporte utilizados hoje: Responda apenas com S ou N.")
            UT_CARRO = input(f"\t1. Carro (combustível fósseis) ").upper()
            while UT_CARRO != 'S' and UT_CARRO != 'N': UT_CARRO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CARONA_COMPARTILHADA = input(f"\t2. Carona compartilhada ").upper()
            while UT_CARONA_COMPARTILHADA != 'S' and UT_CARONA_COMPARTILHADA != 'N': UT_CARONA_COMPARTILHADA = input(f"\tDigite apenas S ou N. ").upper()
            UT_BICICLETA = input(f"\t3. Bicicleta ").upper()
            while UT_BICICLETA != 'S' and UT_BICICLETA != 'N': UT_BICICLETA = input(f"\tDigite apenas S ou N. ").upper()
            UT_TRANSPORTE_PUBLICO = input(f"\t4. Transporte público (ônibus, metrô, trem) ").upper()
            while UT_TRANSPORTE_PUBLICO != 'S' and UT_TRANSPORTE_PUBLICO != 'N': UT_TRANSPORTE_PUBLICO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CARRO_ELETRICO = input(f"\t5. Carro elétrico ").upper()
            while UT_CARRO_ELETRICO != 'S' and UT_CARRO_ELETRICO != 'N': UT_CARRO_ELETRICO = input(f"\tDigite apenas S ou N. ").upper()
            UT_CAMINHADA = input(f"\t6. Caminhada ").upper()
            while  UT_CAMINHADA != 'S' and  UT_CAMINHADA != 'N': UT_CAMINHADA = input(f"\tDigite apenas S ou N. ").upper()

            if CA_GASTO < 150: CA_RESULTADO_ORIGINAL = "Alta"
            elif 150 <= CA_GASTO <= 200: CA_RESULTADO_ORIGINAL = "Moderada"
            else: CA_RESULTADO_ORIGINAL = "Baixa"

            if CE_GASTO < 5: CE_RESULTADO_ORIGINAL = "Alta"
            elif 5 <= CE_GASTO <= 10: CE_RESULTADO_ORIGINAL = "Moderada"
            else: CE_RESULTADO_ORIGINAL = "Baixa"

            if NR_PORCENTAGEM > 50: NIVEL_NR_PORCENTAGEM_ORIGINAL = "Alta"
            elif 20 <= NR_PORCENTAGEM <= 50: NIVEL_NR_PORCENTAGEM_ORIGINAL = "Moderada"
            else: NIVEL_NR_PORCENTAGEM_ORIGINAL = "Baixa"

            NIVEL_TRANSPORTE_ORIGINAL = "Baixa"
            if UT_CARRO == 'S' or UT_CARONA_COMPARTILHADA == 'S':
                if UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S' or UT_CAMINHADA == 'S':
                    NIVEL_TRANSPORTE_ORIGINAL = "Moderada"
            elif UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S'or UT_CAMINHADA == 'S':
                NIVEL_TRANSPORTE_ORIGINAL = "Alta"
            
            cursor.execute(("""INSERT INTO sustentabilidade 
            (DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO,
            UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA, UT_TRANSPORTE_PUBLICO, UT_CARRO_ELETRICO, 
            UT_CAMINHADA)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """), 
            (DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO, UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA,
            UT_TRANSPORTE_PUBLICO, UT_CARRO_ELETRICO, UT_CAMINHADA))
            
            CA_RESULTADO_CRIPT = criptografar_texto_hill(CA_RESULTADO_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
            NIVEL_NR_PORCENTAGEM_CRIPT = criptografar_texto_hill(NIVEL_NR_PORCENTAGEM_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
            CE_RESULTADO_CRIPT = criptografar_texto_hill(CE_RESULTADO_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
            NIVEL_TRANSPORTE_CRIPT = criptografar_texto_hill(NIVEL_TRANSPORTE_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)

            cursor.execute(("""INSERT INTO resultados
                                (DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO)
                                VALUES(%s, %s, %s, %s, %s)"""),
            (DATA_, CA_RESULTADO_CRIPT, NIVEL_NR_PORCENTAGEM_CRIPT, CE_RESULTADO_CRIPT, NIVEL_TRANSPORTE_CRIPT))
            conexao.commit()
            print('Dados inseridos com sucesso!')
            pausar() 
        case 2:#DELETAR ALGUM DADO POR ID
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                   DELETAR DADO POR ID                    ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
            deletar=True
            while deletar:
                id_excluir_str = input("Digite o ID que deseja excluir: ")
                if id_excluir_str.isdigit():
                    id_excluir = int(id_excluir_str)
                    cursor.execute("SELECT * FROM sustentabilidade WHERE ID = %s", (id_excluir,))
                    existe= cursor.fetchone()
                    if existe:
                        cursor.execute("DELETE FROM resultados WHERE ID = %s", (id_excluir,))
                        cursor.execute("DELETE FROM sustentabilidade WHERE ID = %s", (id_excluir,))
                        conexao.commit()
                        print(f"\nO registro com ID {id_excluir} foi excluido com sucesso!")
                    else:
                        print(f"\nO registro com ID {id_excluir} não existe na tabela!")
                else:
                    print("ID inválido. Por favor, insira um número.")
                
                deletarN = input('\nDeseja apagar algum outro dado? \n tecle = S para >>>SIM<<       tecle = N para >>> NÃO<<:').upper()
                while deletarN != 'S' and deletarN != 'N':
                    deletarN = input('\nDeseja apagar algum outro dado? \n tecle = S para >>>SIM<<       tecle = N para >>> NÃO<<:').upper()
                if deletarN == 'N':
                    deletar = False
            pausar() 
        case 3:#ALTERAR DADO INSERIDO
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                  ALTERAR DADO INSERIDO                   ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
            alterar = True
            while alterar:
                aux_str = input('Digite o ID que você deseja alterar: ')
                if aux_str.isdigit():
                    aux = int(aux_str)
                    cursor.execute("SELECT * FROM sustentabilidade WHERE ID = %s", (aux,))
                    existe = cursor.fetchone()
                    if existe:
                        DATA_ = input("Qual é a data (AAAA-MM-DD)? ")
                        CA_GASTO = float(input("Quantos litros de água você consumiu hoje? "))
                        CE_GASTO = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
                        NR_QUANTIDADE =float(input("Quantos KG de resíduos não reciclaveis você gerou hoje? "))
                        NR_PORCENTAGEM = float(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))

                        print(f"\nEscolha os meios de transporte utilizados hoje: Responda apenas com S ou N.")
                        UT_CARRO = input(f"\t1. Carro (combustível fósseis) ").upper()
                        while UT_CARRO != 'S' and UT_CARRO != 'N': UT_CARRO = input(f"\tDigite apenas S ou N. ").upper()
                        UT_CARONA_COMPARTILHADA = input(f"\t2. Carona compartilhada ").upper()
                        while UT_CARONA_COMPARTILHADA != 'S' and UT_CARONA_COMPARTILHADA != 'N': UT_CARONA_COMPARTILHADA = input(f"\tDigite apenas S ou N. ").upper()
                        UT_BICICLETA = input(f"\t3. Bicicleta ").upper()
                        while UT_BICICLETA != 'S' and UT_BICICLETA != 'N': UT_BICICLETA = input(f"\tDigite apenas S ou N. ").upper()
                        UT_TRANSPORTE_PUBLICO = input(f"\t4. Transporte público (ônibus, metrô, trem) ").upper()
                        while UT_TRANSPORTE_PUBLICO != 'S' and UT_TRANSPORTE_PUBLICO != 'N': UT_TRANSPORTE_PUBLICO = input(f"\tDigite apenas S ou N. ").upper()
                        UT_CARRO_ELETRICO = input(f"\t5. Carro elétrico ").upper()
                        while UT_CARRO_ELETRICO != 'S' and UT_CARRO_ELETRICO != 'N': UT_CARRO_ELETRICO = input(f"\tDigite apenas S ou N. ").upper()
                        UT_CAMINHADA = input(f"\t6. Caminhada ").upper()
                        while  UT_CAMINHADA != 'S' and  UT_CAMINHADA != 'N': UT_CAMINHADA = input(f"\tDigite apenas S ou N. ").upper()
                        if CA_GASTO < 150: CA_RESULTADO_ORIGINAL = "Alta"
                        elif 150 <= CA_GASTO <= 200: CA_RESULTADO_ORIGINAL = "Moderada"
                        else: CA_RESULTADO_ORIGINAL = "Baixa"

                        if CE_GASTO < 5: CE_RESULTADO_ORIGINAL = "Alta"
                        elif 5 <= CE_GASTO <= 10: CE_RESULTADO_ORIGINAL = "Moderada"
                        else: CE_RESULTADO_ORIGINAL = "Baixa "

                        if NR_PORCENTAGEM > 50: NIVEL_NR_PORCENTAGEM_ORIGINAL = "Alta"
                        elif 20 <= NR_PORCENTAGEM <= 50: NIVEL_NR_PORCENTAGEM_ORIGINAL = "Moderada"
                        else: NIVEL_NR_PORCENTAGEM_ORIGINAL = "Baixa"
                        
                        NIVEL_TRANSPORTE_ORIGINAL = "Baixa" 
                        if UT_CARRO == 'S' or UT_CARONA_COMPARTILHADA == 'S':
                            if UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S' or UT_CAMINHADA == 'S':
                                NIVEL_TRANSPORTE_ORIGINAL = "Moderada"
                        elif UT_BICICLETA == 'S' or UT_TRANSPORTE_PUBLICO == 'S' or UT_CARRO_ELETRICO == 'S'or UT_CAMINHADA == 'S':
                            NIVEL_TRANSPORTE_ORIGINAL = "Alta"

                        cursor.execute("UPDATE sustentabilidade SET DATA_ = %s, CA_GASTO = %s, NR_QUANTIDADE = %s, NR_PORCENTAGEM = %s, CE_GASTO = %s, UT_CARRO = %s, UT_CARONA_COMPARTILHADA = %s, UT_BICICLETA = %s, UT_TRANSPORTE_PUBLICO = %s, UT_CARRO_ELETRICO = %s, UT_CAMINHADA = %s WHERE ID = %s",
                                        (DATA_, CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO, UT_CARRO, UT_CARONA_COMPARTILHADA, UT_BICICLETA, UT_TRANSPORTE_PUBLICO, UT_CARRO_ELETRICO, UT_CAMINHADA, aux))
                        
                        CA_RESULTADO_CRIPT = criptografar_texto_hill(CA_RESULTADO_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                        NIVEL_NR_PORCENTAGEM_CRIPT = criptografar_texto_hill(NIVEL_NR_PORCENTAGEM_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                        CE_RESULTADO_CRIPT = criptografar_texto_hill(CE_RESULTADO_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                        NIVEL_TRANSPORTE_CRIPT = criptografar_texto_hill(NIVEL_TRANSPORTE_ORIGINAL, MATRIZ_CHAVE, DIMENSAO_MATRIZ, MODULO_ALFABETO)

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

                alterarN = input('\nDeseja alterar algum outro dado? \n tecle = S para >>>SIM<<       tecle = N para >>> NÃO<<:').upper()
                while alterarN != 'S' and alterarN != 'N':
                    alterarN = input('\nDeseja alterar algum outro dado? \n tecle = S para >>>SIM<<       tecle = N para >>> NÃO<<:').upper()
                if alterarN == 'N':
                    alterar = False
            pausar() 
        case 4:#LISTA TABELA POR ID
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                     LISTAR TABELAS                     ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar()
            print("\nTABELA SUSTENTABILIDADE:")
            cursor.execute("SELECT * FROM sustentabilidade")
            resultado_sust = cursor.fetchall()
            for linha in resultado_sust:
                print(f"""\n 
            ID: {linha[0]}, Data: {linha[1]} 
            \tÁgua (L): {linha[2]} 
            \tRes.NãoRec (kg): {linha[3]}
            \tRes.Rec (%): {linha[4]} 
            \tEnergia (kW): {linha[5]} 
            \tCarro: {linha[6]} 
            \tCarona: {linha[7]}
            \tBicicleta: {linha[8]} 
            \tTransp.Púb: {linha[9]} 
            \tCarroElét: {linha[10]} 
            \tCaminhada: {linha[11]}""") 
            pausar() 
            print("\nTABELA RESULTADOS (dados descriptografados): ")
            cursor.execute("SELECT ID, DATA_, CA_RESULTADO, NR_RESULTADO, CE_RESULTADO, UT_RESULTADO FROM resultados")
            resultado_res = cursor.fetchall()
            for linha_res in resultado_res:
                id_db, data_db, ca_cript, nr_cript, ce_cript, ut_cript = linha_res
                
                CA_RESULTADO_DESCRIPT = descriptografar_texto_hill(ca_cript, MATRIZ_CHAVE_INVERSA, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                NR_RESULTADO_DESCRIPT = descriptografar_texto_hill(nr_cript, MATRIZ_CHAVE_INVERSA, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                CE_RESULTADO_DESCRIPT = descriptografar_texto_hill(ce_cript, MATRIZ_CHAVE_INVERSA, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                UT_RESULTADO_DESCRIPT = descriptografar_texto_hill(ut_cript, MATRIZ_CHAVE_INVERSA, DIMENSAO_MATRIZ, MODULO_ALFABETO)
                
                print(f"""\n
            ID: {id_db}, Data: {data_db}
            \t Uso de água: {CA_RESULTADO_DESCRIPT}
            \t Reciclagem de resíduos: {NR_RESULTADO_DESCRIPT}
            \t Uso de eletricidade: {CE_RESULTADO_DESCRIPT}
            \t Uso de transportes: {UT_RESULTADO_DESCRIPT}""")
            pausar() 
        case 5: #LISTAR MÉDIA
            print("""
    ╔══════════════════════════════════════════════════╗
    ║                      LISTAR MÉDIA                      ║
    ╚══════════════════════════════════════════════════╝ """)
            pausar() 
            soma_ca_local = 0 
            soma_ce_local = 0
            soma_nrp_local = 0
            soma_nrq_local = 0
            num_registros_media = 0
            
            cursor.execute("SELECT CA_GASTO, NR_QUANTIDADE, NR_PORCENTAGEM, CE_GASTO FROM sustentabilidade")
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
                
                print(f"\n\tMÉDIAS DE REGISTROS ({num_registros_media} registros):")
                if num_registros_media > 0:
                    print(f"\tÁgua utilizada: (L) {soma_ca_local / num_registros_media : .1f}")
                    print(f"\tResíduos não recicláveis: (kg) {soma_nrq_local / num_registros_media : .1f}")
                    print(f"\tResíduos reciclados: (%) {soma_nrp_local / num_registros_media : .1f}")
                    print(f"\tEnergia consumida: (kW) {soma_ce_local / num_registros_media : .1f}")
            pausar() 
        case 6:
            programaAtivo = False
            cursor.close()
            conexao.close()
            print (f'''Conexão encerrada! \nObrigada por atualizar a tabela!''')
            break