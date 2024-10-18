# Solicitar a idade do usuário
idade = int(input("Digite a sua idade: "))

# Verificar se a idade é suficiente para dirigir
if idade >= 18:
    print("Você pode dirigir.")
else:
    anos_faltam = 18 - idade
    print(f"Você ainda não pode dirigir. Faltam {anos_faltam} anos para você poder dirigir.")