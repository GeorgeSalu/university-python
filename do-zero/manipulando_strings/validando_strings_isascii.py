# isascii() = é uma função interna do Python que verifica se todos os caracteres de uma string pertencem ao conjunto padrão ASCII.
# Ele retorna True se a string estiver vazia ou contiver apenas caracteres com valores entre 0 e 127, e False caso contrário

nome_usuario = "Carlos"
print(nome_usuario.isascii())

usuario_estrangeiro = "François"
print(usuario_estrangeiro.isascii())