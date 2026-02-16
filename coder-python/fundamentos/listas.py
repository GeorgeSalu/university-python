lista = []
print(type(lista))
print(dir(lista))
print(len(lista))
lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = [1,2,4,5,'ana','bia']
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista.index('Guilherme'))
print(lista[2])
print(1 in lista)
print('Rebeca' in lista)
print('Pedro' not in lista)
print(lista[0])
print(lista[0])
print(lista[-1])
print(lista[-5])