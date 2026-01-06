class Aviao:
    __asas = 2
    __qtd_passageiro = 100

    def __init__(self, marca):
        self.marca = marca

    def mostrar_asas(self):
        print("o aviao tem %d asas "%self.__asas)

    def quantidade_passageiro(self):
        print("a quantidade de passageiros é %d "%self.__qtd_passageiro)

aviao = Aviao("Aviao hora de codar")
print(aviao.marca)
aviao.mostrar_asas()
aviao.quantidade_passageiro()