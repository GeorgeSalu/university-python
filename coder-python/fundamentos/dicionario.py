pessoa = {'nome': 'Prof(a). Ana', 'idade': 38,'cursos': ['Inglês', 'Português']}
print(pessoa)
print(type(pessoa))
print(dir(pessoa))
print(len(pessoa))

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('nome'))
print(pessoa.get('idade'))
print(pessoa.get('tags'))

pessoa2 = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
print(pessoa2)
pessoa2['idade'] = 44
print(pessoa2)
pessoa2.pop('idade')
print(pessoa2)
pessoa2.clear()
print(pessoa2)