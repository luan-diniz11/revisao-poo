#Exemplo de Encapsulamento
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado
    
    def depositar(self, valor):  # Método público
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):  # Método público
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):  # Método público
        return f"Saldo de {self.__titular}: {self.__saldo} reais"


conta = ContaBancaria("Luan", 100)
conta.depositar(50)
print(conta.consultar_saldo())
