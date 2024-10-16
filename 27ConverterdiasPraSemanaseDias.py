def converter_dias_para_semanas(dias):
    semanas = dias // 7  #Calcula o número de semanas
    dias_restantes = dias % 7  #Calcula os dias restantes
    return semanas, dias_restantes

#Solicita a entrada do usuário
try:
    dias_input = int(input("Digite o número de dias: "))
    
    if dias_input < 0:
        print("Por favor, digite um número de dias positivo.")
    else:
        semanas, dias_restantes = converter_dias_para_semanas(dias_input)
        print(f"{dias_input} dias = {semanas} semanas e {dias_restantes} dias.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
