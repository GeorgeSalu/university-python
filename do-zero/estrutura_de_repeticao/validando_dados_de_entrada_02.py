# saindo quando quiser
print("digite uma mensagem que irei repetir para voce")
print("para encerrar escreva 'sair'")
texto = input('')
while texto != 'sair':
    print(texto)
    texto = input('')
print('encerrando o programa')