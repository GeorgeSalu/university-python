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
