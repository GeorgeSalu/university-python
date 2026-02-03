"""
2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são
vogais e quantas são consoantes.
"""
vogais: int = 0
consoantes: int = 0
arquivo: str = input('informe o nome do arquivo para abrir: ')

with open(arquivo, 'r') as arq:
    linhas = arq.readlines()


for linha in linhas:
    if linha.replace('\n', '').lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1
    else:
        consoantes += 1


if vogais > 0:
    print(f'existe {vogais} vogais no arquivo')
else:
    print(f'nao existe {vogais} vogais no arquivo')

if consoantes > 0:
    print(f'existe {consoantes} consoantes no arquivo')
else:
    print(f'nao existe {consoantes} consoantes no arquivo')