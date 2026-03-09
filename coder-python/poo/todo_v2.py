#!/usr/local/bin/python3
from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self,descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # possivel indexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefs pendentes'

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no Mercado')
    mercado.add('frutas secas')
    mercado.add('carne')
    mercado.add('tomate')
    print(mercado)

    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')

if __name__ == '__main__':
    main()