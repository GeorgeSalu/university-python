"""
Try / Except / Else / Finally
Dica de quando e onde tratar codigo:
TODA ENTRADA DEVE SER TRATADA!
obs: A função do usuário é destruir o seu sistema
"""
# else -> é executado somente se não ocorrer o error
try:
    num = int(input('informe um numero: '))
except ValueError:
    print(f'valor incorreto')
else:
    print(f'o numero digitado foi {num}')

# finally
try:
    num = int(input('informe um numero: '))
except ValueError:
    print('voce não digitou um valor valido')
else:
    print(f'voce digitou o numero {num}')
finally:
    print('executando o finally')

# obs: o bloco finally é sempre executado, independente houve-se execução ou não
# o finally, geralmente é utilizado para fechar ou desalocar recursos

# exemplo mas complexo
def dividir(a, b):
    return a / b

num1 = int(input('informe o primeiro numero: '))

try:
    num2 = int(input('informe o segundo numero: '))
except ValueError:
    print('o valor precisa ser numerico')


try:
    print(dividir(num1, num2))
except NameError:
    print('valor incorreto')