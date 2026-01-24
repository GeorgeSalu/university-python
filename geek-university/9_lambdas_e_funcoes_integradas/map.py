"""
Map

Com map fazemos mapeamento de valores para função
"""
import math

def area(r):
    """Calcula a area de um círculo com raio 'r'"""
    return math.pi * (r**2)

print(area(3))
print(area(5.3))

raios = [2,5,7.1,0.3,10,14]

# forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# forma 2 - com map
# map é uma função que recebe dois parametros: o primeiro a função o segundo um iteravel
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# forma 3 - map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# obs: apos utilizar a função map() depois da primeira utilização do resultado ele é zerado

# para fixar - map
# temos dados iteraveis
# dados: a1, a2, .... an
# temos uma função:
# função: f(x)
# Utilizamos a função map(f, dados) onde map ira 'mapear' cada elemento dos dados e aplicar a função

