"""
Geradores
- Geradores (Generators) são Iterators (Iteradores)
obs: O contrario não é verdadeiro. ou seja, nem todo iterator é um generator

Outras informações
- Generators podem ser criados com funções geradoras
- Funções geradoras utilizam a palavr reservada yield
- Generators podem ser criados com expressões geradoras

Diferenças entre funções e Generator Functions (Funções Geradoras)
Funções
    -> utilizam return
    -> retorna uma vez
    -> quando executada, retorna valor
Generator Functions
    -> utilizam yield
    -> podem utilizar yield multiplas vezes
    -> quando executada, retorn um generator
"""
# exemplo função geradora (generator function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# Obs: um generator function não é um generator. Ela gera um generator

gen = conta_ate(5)
# print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


gen2 = conta_ate(10)
for num in gen2:
    print(num)