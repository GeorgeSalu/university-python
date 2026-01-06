frase = "testamos o começo da string"

print(frase.endswith("string"))
print(frase.endswith("stringg"))

if frase.endswith("string") == True:
    print("encontramos a palavra")