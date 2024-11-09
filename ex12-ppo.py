
class Estudante:
    def _init_(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    # Getter e Setter para o atributo nome
    def nome(self):
        return self._nome

    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para o atributo matricula
    def matricula(self):
        return self._matricula

    def matricula(self, nova_matricula):
        if not isinstance(nova_matricula, str) or len(nova_matricula) == 0:
            raise ValueError("A matrícula deve ser uma string não vazia.")
        self._matricula = nova_matricula

# Exemplo de uso
estudante = Estudante("Helana Siqueira", "15678")
print(estudante.nome)      
print(estudante.matricula)