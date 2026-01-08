frase = "eu quero encontrar o peixe"

print(frase.find("peixe"))

if frase.find("peixe") >= 0:
    print("encontrei o peixe")


print(frase.find("tubarao"))

if frase.find("tubarao") >= 0:
    print("encontrei o tubarao")