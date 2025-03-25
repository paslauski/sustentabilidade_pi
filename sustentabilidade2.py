# Coletando os dados do usuário
data = input("Qual é a data (DD/MM/AAAA)? ")
agua = float(input("Quantos litros de água você consumiu hoje? "))
energia = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
nao_reciclado=float(input("Quantos KG de resíduos não reciclaveis você gerou hoje? "))
percentual_reciclado = float(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))
'''
# Entrada de múltiplos meios de transporte antiga
print("\nEscolha os meios de transporte utilizados hoje (digite os números separados por vírgula):")
print("1. Transporte público (ônibus, metrô, trem)")
print("2. Bicicleta")
print("3. A pé")
print("4. Carro (combustível fósseis)")
print("5. Carro elétrico")
print("6. Carona compartilhada")

transportes = input("Digite os números correspondentes (ex: 1,3,5): ")
transportes = [int(x) for x in transportes.split(",")]
'''
#Entrada de múltiplos meios de transporte atualizada
print(f"\nEscolha os meios de transporte utilizados hoje: Responda apenas com S ou N.")
transporte_publico = input(f"\t1. Transporte público (ônibus, metrô, trem) ")
while transporte_publico != 'S' and transporte_publico != 'N':
    transporte_publico = input(f"\tDigite apenas S ou N. ")
bicleta = input(f"\t2. Bicicleta ")
while bicleta != 'S' and bicleta != 'N':
    bicleta = input(f"\tDigite apenas S ou N. ")
caminhada = input(f"\t3. Caminhada ")
while caminhada != 'S' and caminhada != 'N':
    caminhada = input(f"\tDigite apenas S ou N. ")
carro = input(f"\t4. Carro (combustível fósseis) ")
while carro != 'S' and carro != 'N':
    carro = input(f"\tDigite apenas S ou N. ")
carro_eletrico = input(f"\t5. Carro elétrico ")
while carro_eletrico != 'S' and carro_eletrico != 'N':
    carro_eletrico = input(f"\tDigite apenas S ou N. ")
carona_compartilhada = input(f"\t6. Carona compartilhada ")
while carona_compartilhada != 'S' and carona_compartilhada != 'N':
    carona_compartilhada = input(f"\tDigite apenas S ou N. ")

# Classificação de consumo de água
if agua < 150:
    class_agua = "Alta Sustentabilidade"
elif 150 <= agua <= 200:
    class_agua = "Moderada Sustentabilidade"
else:
    class_agua = "Baixa Sustentabilidade"

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
'''
# Classificação do transporte antiga
sustentavel = [1, 2, 3, 5]  # Transporte público, bicicleta, a pé, carro elétrico
intermediario = [6]  # Carona compartilhada
nao_sustentavel = [4]  # Carro a combustíveis fósseis

if all(t in sustentavel for t in transportes):
    class_transporte = "Alta Sustentabilidade"
elif all(t in nao_sustentavel for t in transportes):
    class_transporte = "Baixa Sustentabilidade"
else:
    class_transporte = "Moderada Sustentabilidade"
'''
# Classificação do transporte atualizada
if transporte_publico == 'S' and carro == 'S':
    class_transporte = "Moderada Sustentabilidade"
elif bicleta == 'S' or transporte_publico == 'S' or carro_eletrico == 'S'or caminhada == 'S':
    class_transporte = "Alta Sustentabilidade"
else:
    class_transporte = "Baixa Sustentabilidade"
# Exibir relatório
print("\n--- Relatório de Sustentabilidade ---")
print(f"Data: {data}")
print(f"Consumo de água: {class_agua}")
print(f"Consumo de energia: {class_energia}")
print(f"Geração de resíduos: {class_residuos}")
print(f"Uso de transporte: {class_transporte}")
print("------------------------------------")
