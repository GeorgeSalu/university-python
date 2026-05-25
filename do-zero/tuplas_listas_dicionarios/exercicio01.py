# Exercício 1
# crie um programa que contem uma tupla contendo o nome de 10 linguagens de programação
# Javascript, Rust, Swift, Python, Kotlin, Go, C#, Dart, Julia e Typescript
# em que posição esta a linguagem python?, mostre na tela

linguagens = ('Javascript', 'Rust','Swift','Python','Kotlin','Go','C#','Dart','Julia','Typescript')

i = 0
while linguagens[i] != 'Python':
    i += 1

print(f'Encontramos o python na {i + 1} posicao')