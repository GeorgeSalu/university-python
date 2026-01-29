"""
Try / Except / Else / Finally
Dica de quando e onde tratar codigo:
TODA ENTRADA DEVE SER TRATADA!
obs: A função do usuário é destruir o seu sistema
"""
try:
    num = int(input('informe um numero: '))
except ValueError:
    print(f'valor incorreto')

print(f'o numero digitado foi {num}')