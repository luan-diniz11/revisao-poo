#Exemplo de Herança 
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        raise NotImplementedError("Este método deve ser sobrescrito pela subclasse.")

class Cachorro(Animal):
    def som(self):
        return "Au Au!"

class Gato(Animal):
    def som(self):
        return "Miau!"

dog = Cachorro("Rex")
cat = Gato("Frajola")
print(dog.som())
print(cat.som())
