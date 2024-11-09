
class Professor:
    def _init_(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    # Getter e Setter para o atributo nome
    def nome(self):
        return self._nome

    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome do professor não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para o atributo disciplina

    def disciplina(self):
        return self._disciplina

    def disciplina(self, nova_disciplina):
        if not nova_disciplina:
            raise ValueError("A disciplina não pode estar vazia.")
        self._disciplina = nova_disciplina

# Exemplo de uso
professor = Professor("Davi", "Matemática")
print(professor.nome)       
print(professor.disciplina) 
