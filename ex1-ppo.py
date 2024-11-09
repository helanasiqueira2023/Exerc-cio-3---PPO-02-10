class Pessoa:
    def _init_(self,nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('Nome Invalido')

# Testee............................
abc = Pessoa('Helana Siqueira')
print(abc.get_nome())

abc.set_nome('Helana Siqueira')
print(abc.get_nome())