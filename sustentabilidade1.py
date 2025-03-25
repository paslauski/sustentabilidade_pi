# Coletando os dados do usuário
data = input("Qual é a data (DD/MM/AAAA)? ")
agua = float(input("Quantos litros de água você consumiu hoje? "))
energia = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
percentual_reciclado = float(input("Qual a porcentagem de resíduos reciclados no total (em %)? "))

# Entrada de múltiplos meios de transporte
print("\nEscolha os meios de transporte utilizados hoje (digite os números separados por vírgula):")
print("1. Transporte público (ônibus, metrô, trem)")
print("2. Bicicleta")
print("3. A pé")
print("4. Carro (combustível fósseis)")
print("5. Carro elétrico")
print("6. Carona compartilhada")

transportes = input("Digite os números correspondentes (ex: 1,3,5): ")
transportes = [int(x) for x in transportes.split(",")]

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

# Classificação do transporte
sustentavel = [1, 2, 3, 5]  # Transporte público, bicicleta, a pé, carro elétrico
intermediario = [6]  # Carona compartilhada
nao_sustentavel = [4]  # Carro a combustíveis fósseis

if all(t in sustentavel for t in transportes):
    class_transporte = "Alta Sustentabilidade"
elif all(t in nao_sustentavel for t in transportes):
    class_transporte = "Baixa Sustentabilidade"
else:
    class_transporte = "Moderada Sustentabilidade"

# Exibir relatório
print("\n--- Relatório de Sustentabilidade ---")
print(f"Data: {data}")
print(f"Consumo de água: {class_agua}")
print(f"Consumo de energia: {class_energia}")
print(f"Geração de resíduos: {class_residuos}")
print(f"Uso de transporte: {class_transporte}")
print("------------------------------------")
