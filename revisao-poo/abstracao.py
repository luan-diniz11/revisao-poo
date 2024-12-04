#Exemplo de Abstração
from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def calcular_salario(self):
        return 5000

class Estagiario(Funcionario):
    def calcular_salario(self):
        return 1500

# Uso
funcionarios = [Gerente(), Estagiario()]
for funcionario in funcionarios:
    print(f"Salário: {funcionario.calcular_salario()}")
