"""
crie uma classe Carro com as propriedades marca, valor, numero de portas e tanque de gasolina
crie um metodo que abastece o tanque de gasolina
crie um metodo dirigir que remove gasolina baseado em uma kilometragem rodada
"""
class Carro:
    def __init__(self,marca,valor,numero_de_porta,tanque):
        self.marca = marca
        self.valor = valor
        self.numero_de_porta = numero_de_porta
        self.tanque = tanque

    def abastecer(self,litros):
        if self.tanque >= 100:
            print("o tanque esta cheio")
        else:
            self.tanque += litros
            if self.tanque > 100:
                self.tanque = 100

    def dirigir(self, km):
        km_por_litro = 10
        self.tanque -= (km / km_por_litro)

fusca = Carro("VW", 15000,4, 80)

print(fusca.marca)
print(fusca.valor)

fusca.abastecer(100)
print(fusca.tanque)

fusca.dirigir(100)
print(fusca.tanque)