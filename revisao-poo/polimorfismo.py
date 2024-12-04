#Exemplo de Polimorfismo
class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2

formas = [Retangulo(3, 4), Circulo(5)]
for forma in formas:
    print(f"Área: {forma.area()}")
