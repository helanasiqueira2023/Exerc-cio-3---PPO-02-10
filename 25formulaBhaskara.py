# Função para calcular as raízes
def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c

# Entrada de dados
print("Calculadora de raízes da equação do segundo grau (ax² + bx + c = 0)")
a = float(input("Digite o coeficiente a (diferente de 0): "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

#Verifica se 'a' é diferente de zero
if a == 0:
    print("O coeficiente 'a' deve ser diferente de zero.")
else:
#Chama a função e imprime o resultado
    resultado = calcular_raizes(a, b, c)
    print('A raíz dessas variáveis é:', resultado)
