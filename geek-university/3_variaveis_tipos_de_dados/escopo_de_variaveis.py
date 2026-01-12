"""
escopo de variaveis

dois casos de escopo

1 - variaveis globais
  - variaveis globais são reconhecidas, ou seja,seu escopo compreende todo o programa
2 - variaveis locais
  - variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo esta limitado ao bloco onde foi declarada
"""
# escopo global
numero = 42
print(numero)
print(type(numero))

numero2 = "geek"
print(numero2)
print(type(numero2))

nao_existo = "oi"
print(nao_existo)

# escopo local
numero3 = 42
if numero3 > 10:
    novo = numero3 + 10 # a varivei 'novo' esta declarada localmente dentro do bloco do if, portanto é local
    print(novo)

print(novo)