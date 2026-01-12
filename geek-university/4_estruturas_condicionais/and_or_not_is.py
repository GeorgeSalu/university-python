"""
estruturas logicas: and(e), or(ou), not(nao), is(é)

operadores unarios
    - not, is
operadores binarios
    - and, or

regras de funcionamento
- para o 'and', ambos os valores precisam ser True
- para o 'or', um ou outro valor precisa ser True
- para 'not', o valor de boolean é invertido, ou seja se for True vira False e se for False vira True
"""
ativo = True
logado = False


if ativo:
    print("bem vindo usuario")
else:
    print("voce precisa ativar sua conta")

print(not ativo)
print(ativo is True)