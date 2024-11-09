def _init_(self, salario):
 self.salario = salario  # Usa o setter para aplicar a validação

    # Getter para o atributo salario

def salario(self):
 return self._salario

    # Setter para o atributo salario com validação
def salario(self, novo_salario):
  if novo_salario <= 0:
     raise ValueError("O salário deve ser um valor positivo.")
  self._salario = novo_salario