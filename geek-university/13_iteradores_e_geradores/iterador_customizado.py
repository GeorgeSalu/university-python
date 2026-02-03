"""
Escrevendo um iterador customizado
"""
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior


con = Contador(1,61)
print(con)