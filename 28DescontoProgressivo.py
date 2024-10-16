#Solicita o valor da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Aplica os descontos
if valor_compra > 500:
    desconto = 0.10  # 10% de desconto
elif valor_compra > 100:
    desconto = 0.05  # 5% de desconto
else:
    desconto = 0.0  # Sem desconto

# Calcula o valor final
valor_final = valor_compra * (1 - desconto)

# Exibe o resultado
print(f"O valor final da compra, após o desconto, é: R$ {valor_final:.2f}")
