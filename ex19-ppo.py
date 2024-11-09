class Cidade:
    def _init_(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        
        def nome(self):
            return self.nome
        
        def nome(self, novo_nome):
         if not novo_nome:
            raise ValueError("O nome da cidade não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para o atributo populacao
    def populacao(self):
        return self._populacao

    def populacao(self, nova_populacao):
        if not isinstance(nova_populacao, int) or nova_populacao < 0:
            raise ValueError("A população deve ser um número inteiro positivo.")
        self._populacao = nova_populacao

# Exemplo de uso
cidade = Cidade("São Paulo", 12300000)
print(cidade.nome)     
print(cidade.populacao)   
