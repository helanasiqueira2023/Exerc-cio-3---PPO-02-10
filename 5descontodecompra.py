valor=int(input("insira valor da compra: "))
if valor>100:
 print(f'valor final é R%{valor*0.90}')
else:
 print(f'O valor final é R${valor}')
