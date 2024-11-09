class Curso:
    def _init_(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    # Getter e Setter para o atributo nome
    def nome(self):
        return self._nome

    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome do curso não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para o atributo duracao
    def duracao(self):
        return self._duracao
    
    def duracao(self, nova_duracao):
        if not isinstance(nova_duracao, (int, float)) or nova_duracao <= 0:
            raise ValueError("A duração do curso deve ser um número positivo.")
        self._duracao = nova_duracao

# Exemplo de uso
curso = Curso("Matemática", 6)
print(curso.nome)      # Matemática
print(curso.duracao)   # 6

# Modificando os atributos com setters
curso.nome = "Física"
curso.duracao = 4
print(curso.nome)      # Física
print(curso.duracao)   # 4

# definir um nome vazio
try:
    curso.nome = ""  # Nome vazio
except ValueError as e:
    print(e)  # "O nome do curso não pode estar vazio."

# definir uma duração inválida
try:
    curso.duracao = -3  # Duração negativa
except ValueError as e:
    print(e)  # "A duração do curso deve ser um número positivo."
