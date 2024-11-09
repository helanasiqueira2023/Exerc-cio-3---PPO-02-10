class Livro:
    def _init_(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    # Getter para o atributo titulo
    def titulo(self):
        return self._titulo

    # Setter para o atributo titulo
    def titulo(self, novo_titulo):
        if not novo_titulo:
            raise ValueError("O título não pode estar vazio.")
        self._titulo = novo_titulo

    # Getter para o atributo autor
    def autor(self):
        return self._autor

    # Setter para o atributo autor
    def autor(self, novo_autor):
        if not novo_autor:
            raise ValueError("O autor não pode estar vazio.")
        self._autor = novo_autor