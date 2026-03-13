#!/usr/local/bin/python3
class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthal'

if __name__ == '__main__':
    jose = Humano('jose')
    grokn = Humano('grokn')
    grokn.das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.nome: {jose.especie}')
    print(f'grokn.nome: {grokn.especie}')