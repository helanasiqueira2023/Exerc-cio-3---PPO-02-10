class Empresa:
    def _init_(self, nome, numero_funcionarios):
        self.nome = nome
        self.numero_funcionarios = numero_funcionarios

    # Getter e Setter para o atributo nome
    def nome(self):
        return self._nome

    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome da empresa não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para o atributo numero_funcionarios
    def numero_funcionarios(self):
        return self._numero_funcionarios

    def numero_funcionarios(self, novo_numero):
        if novo_numero < 0:
            raise ValueError("O número de funcionários deve ser um valor não negativo.")
        self._numero_funcionarios = novo_numero

# Exemplo de uso
empresa = Empresa("Tigre", 50)
print(empresa.nome)              
print(empresa.numero_funcionarios)

# Modificando os atributos usando os setters
empresa.nome = "Tigre"
empresa.numero_funcionarios = 60
print(empresa.nome)             
print(empresa.numero_funcionarios) 

# Tentando definir um nome vazio
try:
    empresa.nome = ""  # Nome vazio
except ValueError as e:
    print(e)  # "O nome da empresa não pode estar vazio."

# Tentando definir um número negativo de funcionários
try:
    empresa.numero_funcionarios = -5  # Número negativo de funcionários
except ValueError as e:
    print(e)  # "O número de funcionários deve ser um valor não negativo."
