num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num2 == 0:
    print("Divisão não é possível, o divisor não pode ser zero.")
else:
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
