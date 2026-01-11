"""
recebendo dados do usuario

input() -> todo dado recebido via input é do tipo string

Em python,string e tudo que estiver entre:
- aspas simples
- aspas duplas
- aspas simples triplas
- aspas duplas triplas

"""
# entrada de dados
nome = input("qual seu nome ? ")
print(f"Seja bem vindo {nome}")

idade = int(input("qual sua idade ? "))

print(f"A {nome} tem {idade} anos")