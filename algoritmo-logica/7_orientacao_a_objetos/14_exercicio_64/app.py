"""
crie uma classe Mamifero com propriedades de mamifero
Herde os detalhes desta classe e crie novas para Cachorro, Gato e outros que quiser
crie objetos destas classes que herdam de mamifero
exiba as pripriedades e metodos ne tela
"""
class Mamifero:
    def __init__(self, patas, orelhas):
        self.patas = patas
        self.orelhas = orelhas

    def andar(self):
        print("o mamifero andou")

class Cachorro(Mamifero):
    def __init__(self, patas, orelhas,cor_do_pelo):
        super().__init__(patas, orelhas)
        self.cor_do_pelo = cor_do_pelo

    def latir(self):
        print("au au")


class Gato(Mamifero):
    def __init__(self, patas, orelhas,listras):
        super().__init__(patas, orelhas)
        self.listras = listras

    def miar(self):
        print("miau")

turca = Cachorro(4,2,"preto")
turca.andar()
turca.latir()

bartolomeu = Gato(4,2,False)
bartolomeu.andar()
bartolomeu.miar()