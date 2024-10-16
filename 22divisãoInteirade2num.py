dividendo = float(input('Informe um número inteiro:'))
divisor = float(input('Informe o segundo número inteiro'))

quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"O resto de {dividendo} / {divisor} é {resto}")
