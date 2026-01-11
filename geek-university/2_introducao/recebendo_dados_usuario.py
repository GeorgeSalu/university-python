"""
recebendo dados do usuario
"""
# entrada de dados
print("qual seu nome ? ")
nome = input()
print("seja bem-vindo {0}".format(nome))

print("qual sua idade ? ")
idade = input()

print("a {0} tem {1} anos".format(nome, int(idade)))