class Jogo:
    def _init_(self, pontuacao):
        self.pontuacao = pontuacao  # setter para aplicar a validação

    # Getter para o atributo pontuacao
    def pontuacao(self):
        return self._pontuacao

    # Setter para o atributo pontuacao
    def pontuacao(self, nova_pontuacao):
        if nova_pontuacao < 0:
            raise ValueError("A pontuação não pode ser negativa.")
        self._pontuacao = nova_pontuacao

# Exemplo de uso:
jogo = Jogo(100)
print(jogo.pontuacao) 

# Modificando a pontuação
jogo.pontuacao = 200
print(jogo.pontuacao) 

# Tentando definir uma pontuação negativa
try:
    jogo.pontuacao = -50  # Pontuação negativa
except ValueError as e:
    print(e)  # "A pontuação não pode ser negativa."
