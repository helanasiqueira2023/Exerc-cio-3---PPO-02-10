# 01

nome = input("Digite seu nome aqui:")
sobrenome = input("Agora seu sobrenome:")
idade = int(input("E por fim informe sua idade:"))

listaA = [nome, sobrenome, idade]

print(listaA)

# 02
meses = int(input("Informe um número de 1 à 12: "))
mes1 = "Janeiro"
mes2 = "Fevereiro"
mes3 = "Março"
mes4 = "Abril"
mes5 = "Maio"
mes6 = "Junho"
mes7 = "Julho"
mes8 = "Agosto"
mes9 = "Setembro"
mes10 = "Outubro"
mes11 = "Novembro"
mes12 = "Dezembro"

listaB = [mes1, mes2, mes3, mes4, mes5, mes6, mes7, mes8, mes9, mes10, mes11, mes12]

meses=meses-1
print(listaB[meses])

#Extra
usuario = input("Qual a questão você quer executar?")
if listaA: 
    print("Você escolheu a lista A")
elif listaB:
    print("Você escolheu a Lista B")