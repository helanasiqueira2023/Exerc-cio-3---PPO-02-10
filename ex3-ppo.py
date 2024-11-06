class ContaBancaria():
   def __init__(self, nome, deposito):
     self.saldo = 1000
     self. nome = nome
     self.deposito = deposito

   def saida(self):
      print(f"O saldo da conta da {self.nome} é R${self.saldo + self.deposito}")



deposito = ContaBancaria(input("Nome: "), (float(input("Valor: "))))
deposito.saida()