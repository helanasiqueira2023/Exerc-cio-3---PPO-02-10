
class Animal:
    def _init_(self, idade):
        self.idade = idade  # Usa o setter para aplicar a validação

    # Getter para o atributo idade
    def idade(self):
        return self._idade

    # Setter para o atributo idade com validação
    def idade(self, nova_idade):
        if not isinstance(nova_idade, int) or nova_idade <= 0:
            raise ValueError("A idade deve ser um número inteiro positivo.")
        self._idade = nova_idade

animal = Animal(5)
print(animal.idade)  

animal.idade = 7
print(animal.idade) 
