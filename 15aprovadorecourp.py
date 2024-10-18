media = float(input("Digite a média do aluno: "))
# Verificar a situação do aluno
if media >= 7:
    print("Aluno aprovado.")
elif 5 <= media < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
