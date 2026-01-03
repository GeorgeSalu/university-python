escopo_global = "tchau"

def teste():
    teste = "ola"
    print(teste)
    print(escopo_global)

teste()

escopo_global = "ate logo"

teste()