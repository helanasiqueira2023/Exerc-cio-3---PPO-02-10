class Filme:
    def _init_(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento

    # Getter e Setter para o atributo titulo
    def titulo(self):
        return self._titulo
    def titulo(self, novo_titulo):
        if not novo_titulo:
            raise ValueError("O título não pode estar vazio.")
        self._titulo = novo_titulo

    # Getter e Setter para o atributo ano_lancamento
    def ano_lancamento(self):
        return self._ano_lancamento

    def ano_lancamento(self, novo_ano):
        if not isinstance(novo_ano, int) or novo_ano < 1888: 
            raise ValueError("O ano de lançamento deve ser um número inteiro maior ou igual a 1888.")
        self._ano_lancamento = novo_ano

# Exemplo de uso
filme = Filme("Inception", 2010)
print(filme.titulo)       
print(filme.ano_lancamento) 

# Modificando os atributos usando os setters
filme.titulo = "Interstellar"
filme.ano_lancamento = 2014
print(filme.titulo)        
print(filme.ano_lancamento) 

# Tentando definir um título vazio
try:
    filme.titulo = "A paixão de Cristo"  
except ValueError as e:
    print(e) 

# Tentando definir um ano inválido
try:
    filme.ano_lancamento = 1800 
except ValueError as e:
    print(e)  # "O ano de lançamento deve ser um número inteiro maior ou igual a 1888."
