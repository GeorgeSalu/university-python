# join() = combina um iterável de strings em uma única string, inserindo a string separadora entre cada elemento
s1 = list('Python')
print(s1) # print separado
print(''.join(s1))
s1[0] = 'p'
print(''.join(s1))