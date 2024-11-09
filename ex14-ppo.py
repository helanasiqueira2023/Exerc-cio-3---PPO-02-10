class Computador:
    def _init_(self, memoria_ram):
        self.memoria_ram = memoria_ram  # Usa o setter para aplicar a validação

    # Getter para o atributo memoria_ram
    def memoria_ram(self):
        return self._memoria_ram

    # Setter para o atributo memoria_ram com validação
    def memoria_ram(self, nova_memoria_ram):
        if nova_memoria_ram <= 0:
            raise ValueError("A memória RAM deve ser maior que zero.")
        self._memoria_ram = nova_memoria_ram

# Exemplo de uso
computador = Computador(8) 
print(computador.memoria_ram) 

computador.memoria_ram = 16 
print(computador.memoria_ram)  