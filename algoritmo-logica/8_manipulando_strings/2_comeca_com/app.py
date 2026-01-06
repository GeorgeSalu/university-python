frase = "testamos o começo da string"

print(frase.startswith("testamos"))
print(frase.startswith("string"))

if frase.startswith("testamos") == True:
    print("encontramos a palavra")