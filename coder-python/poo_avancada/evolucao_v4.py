#!/usr/local/bin/python3
class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade


    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    # metodo estatico
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus','Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # metodo de classe
    @classmethod
    def is_evolido(cls):
        return cls.especie == cls.especies()[-1]


class Neandertal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('jose')
    jose.idade = 40
    print(f'Nome: {jose.nome} Idade: {jose.idade}')