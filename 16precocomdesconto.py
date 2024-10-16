preco_produto = float(input('Informe o preço do praduto:'))
percentual_com_Desconto = float(input('E também informe o percentual com desconto:'))

valor_Desconto = preco_produto*(percentual_com_Desconto/100)
preco_final = preco_produto-valor_Desconto

print(f'O preço final com desconto é de R$: {preco_final:.2f}' )
