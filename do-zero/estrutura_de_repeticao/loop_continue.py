while True:
    nome = input('Digite seu nome: ')
    if nome != 'george':
        continue
    senha = input('Digite sua senha: ')
    if senha == 'dog':
        break
print('acesso concedido')