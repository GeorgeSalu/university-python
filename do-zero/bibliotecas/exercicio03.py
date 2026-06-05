# Exercício 03
# os (Interação com o Sistema Operacional)
# Permite navegar entre pastas, ler diretórios e executar comandos do sistema.

import os

# Descobrir qual é o diretório atual
diretorio_atual = os.getcwd()
print(diretorio_atual)

# Listar todos os arquivos da pasta
print(os.listdir('.'))