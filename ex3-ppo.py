class Carro ():
    def __geteer__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor

#entrada.....
marca_inp = input("Digite a marca de seu carro:")
ano_inp = input("Digite o ano de seu carro:")
cor_inp = input("Por último digite a cor dele:")
carro = Carro({marca_inp}, {ano_inp}, {cor_inp})
print(f"\n marca:{carro.marca} \n ano:{carro.ano} \n cor:{carro.cor}")
        