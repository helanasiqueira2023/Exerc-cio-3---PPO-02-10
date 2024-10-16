num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))

# Realizar a divisão e formatar o resultado com duas casas decimais
if num2 != 0:  # Verificar se o divisor não é zero
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")
else:
    print("Erro: Divisão por zero não é permitida.")

