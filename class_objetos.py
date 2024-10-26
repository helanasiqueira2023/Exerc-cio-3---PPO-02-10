class pessoa ():
    def __init__(self, nome, sobrenome, idade, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
#Entrada...
nome_inp = input("Qual o seu nome? ")
sobrenome_inp = input("Qual é o seu sobrenome? ")
idade_inp = inp = int(input("Qual sua idade? "))
cidade_inp = input("Qual sua cidade? ")

#..................................
p3ssoa = pessoa(nome_inp, sobrenome_inp, idade_inp, cidade_inp)
print(f"\nnome: {p3ssoa.nome}\nsobrenome:{p3ssoa.sobrenome} \nidade:{p3ssoa.idade} \ncidade:{p3ssoa.cidade} ")

