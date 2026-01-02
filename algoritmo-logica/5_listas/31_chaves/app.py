dicionario = {
    "testando": 2,
    "nome": "george",
    "idade": 29
}

print(dicionario)

print("nome" in dicionario)
print("sobrenome" in dicionario)

if "nome" in dicionario:
    print("o seu nome é %s" % dicionario["nome"])