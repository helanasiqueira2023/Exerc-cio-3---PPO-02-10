class Produto:
    def _init_(self, preco):
        self.preco = preco  
    # Utiliza o setter para aplicar validação


    # Getter para o atributo preco
    def preco(self):
        return self._preco

    # Setter para o atributo preco com validação
    def preco(self, novo_preco):
        if novo_preco <= 0:
            raise ValueError("O preço deve ser positivo.")
        self._preco = novo_preco