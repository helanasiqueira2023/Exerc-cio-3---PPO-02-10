class Aluno:
    def _init_(self, nome, nota):
        self._nome = nome
        self._nota = nota

    # Getter e Setter para nome
    def nome(self):
        return self._nome

    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para nota
    def nota(self):
        return self._nota

    def nota(self, nova_nota):
        if not (0 <= nova_nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota = nova_nota
