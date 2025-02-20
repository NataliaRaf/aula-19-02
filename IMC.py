def calcular_imc(peso, altura):
    """Função para calcular o IMC."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Função para classificar o IMC."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Interação com o usuário
while True:
    print("\nCalculadora de IMC")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    # Cálculo do IMC
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")
    
    # Pergunta se deseja continuar
    continuar = input("Deseja calcular novamente? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break