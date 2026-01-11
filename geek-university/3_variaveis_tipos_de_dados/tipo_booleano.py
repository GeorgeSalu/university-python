"""
tipo booleano
algebra booleano, criada por george boole
2 constantes, verdadeiro e falso
True -> Vrdadeiro
False -> Falso
obs: sempre com a inicial maiuscula
"""
ativo = False
print(ativo)

# operacoes basicas
"""
negacao (not)
fazendo a negação, se o valor boolena for verdadeiro o resultado sera falso
se for falso o resultado sera verdadeiro, ou seja sempre o contrario
"""
print(not ativo)
logado = False
"""
ou (or)
é uma operacao binaria, ou seja depende de dois valores, ou um ou outro deve ser verdadeiro
True or True -> True
False or False -> True
False or True -> True
False or False -> False 
"""
print(ativo or logado)

"""
e (and)
também é uma operacao binaria, ou seja depende de dois valores. ambos os valores devem ser verdadeiro

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""