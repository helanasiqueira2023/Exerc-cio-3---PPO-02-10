class ContaBancaria:
    def _init_(self, saldo):
        self.__saldo = saldo if saldo >= 0 else 0 
#Inicializa o saldo, garantindo que não seja negativo


# Método para depositar valor na conta
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor depositado inválido")

# Método para sacar valor da conta
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Valor de saque inválido!")
    
#Método para obter o saldo atual
    def get_saldo(self):
        return self.__saldo