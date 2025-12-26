"""
crie um programa que recebe o numero de rodas que o veiculo possui
se for mas que 2, imprima uma mensagem para pagar pedgio
se for igual a 2, imprima uma mensagem pdizendo que pode passar livremente
"""
numero_de_rodas = int(input("Quantas rodas tem o veículo? "))

print(numero_de_rodas)

if(numero_de_rodas > 2):
  print("O seu veículo precisa pagar pedágio.")

if(numero_de_rodas == 2):
  print("Você pode seguir adiante.")