"""
crie um loop que exibe os numeros digitados do usuario na tela
o loop deve ser canceldo quando o usuario digitar 0
"""
x = 0

while(x < 1):
  numero = int(input("Digite um número: "))

  print(numero)

  if numero == 0:
    print("Saindo do loop!")
    break