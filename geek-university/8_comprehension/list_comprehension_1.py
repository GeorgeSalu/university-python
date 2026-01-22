"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro intravel

# sintaxe da list comprehension
[ dado for dado in iteravel ]
"""
# exemplo
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

res = [numero * 10 for numero in numeros]
print(res)