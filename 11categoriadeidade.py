idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Você é uma criança.")
elif 12 <= idade <= 17:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")