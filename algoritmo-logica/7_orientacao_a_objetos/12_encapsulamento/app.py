class Aviao:
    __asas = 2

    def __init__(self, marca):
        self.marca = marca

    def mostrar_asas(self):
        print("o aviao tem %d asas "%self.__asas)

aviao = Aviao("Aviao hora de codar")
print(aviao.marca)
aviao.mostrar_asas()