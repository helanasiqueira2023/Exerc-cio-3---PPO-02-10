class Celular:
    def _init_(self, marca):
        self._marca = marca

# Getter para o atributo marca
    def marca(self):
        return self._marca

# Setter para o atributo marca com validação
    def marca(self, nova_marca):
        if not nova_marca:
            raise ValueError("A marca não pode estar vazia.")
        self._marca = nova_marca

        celular = Celular("Samsung")
print(celular.marca)  # Samsun celular.marca = "Apple"

