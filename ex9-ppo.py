
class Casa:
    def _init_(self, endereco, valor):
        self._endereco = endereco
        self._valor = valor

    # Getter para o atributo endereco
    def endereco(self):
        return self._endereco

    # Setter para o atributo endereco
    def endereco(self, novo_endereco):
        if not novo_endereco:
            raise ValueError("O endereço não pode estar vazio.")
        self._endereco = novo_endereco

    # Getter para o atributo valor
    def valor(self):
        return self._valor

    # Setter para o atributo valor com validação
    def valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O valor deve ser um número positivo.")
        self._valor = novo_valor