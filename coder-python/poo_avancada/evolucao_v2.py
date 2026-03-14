#!/usr/local/bin/python3
class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    # metodo estatico
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus','Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # metodo de clsse
    @classmethod
    def is_evolido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('jose')
    grokn = Neanderthal('grokn')
    print(f'Evolucao (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Homo sapiens evoluido ? {HomoSapiens.is_evolido()}')
    print(f'Neanderthal evoluido ? {Neanderthal.is_evolido()}')
    print(f'Jose evoluido ? {jose.is_evolido()}')
    print(f'Grok evoluido ? {grokn.is_evolido()}')