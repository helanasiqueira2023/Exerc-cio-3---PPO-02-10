class Veiculo:
    def _init_(self, velocidade_maxima):
        self._velocidade_maxima = velocidade_maxima  # Atributo privado

    # Getter para o atributo velocidade_maxima
    def velocidade_maxima(self):
        return self._velocidade_maxima

# Exemplo de uso
veiculo = Veiculo(180)
print(veiculo.velocidade_maxima) 
