#!/usr/local/bin/python3
lista1 = [1,2,3]
dobro = map(lambda x: x * 2, lista1)
print(list(dobro))

lista_2 = [
    { 'nome': 'joao', 'idade': 31 },
    { 'nome': 'maria', 'idade': 37 },
    { 'nome': 'jose', 'idade': 41 },
]

so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idade = map(lambda p: p['idade'], lista_2)
print(list(so_idade))

# desafio: usando map retorne frases '<Nome> tem <Idade> anos.'
frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista_2)
print(list(frases))