class Pessoa:
    def _init_(self, nome):
        self._nome = nome

    def nome(self):
        return self._nome

    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome não pode estar vazio.")
        self._nome = novo_nome

p = Pessoa("Eduarda")
print(p.nome) 

p.nome = "Levi"  
print(p.nome) 