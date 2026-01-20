"""
Definindo funções
- Funções são pequenas partes de codigo que realizam tarefas específicas
- Pode ou não receber entradas de dados e retornar uma saida de dados
- Muto uteis para executar procedimentos similares por repetidas vezes

obs: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a sua função seja simplificada

Em python a forma geral de definir uma funcção é:

def nome_da_funcao(parametros_entradas):
    bloco_da_funcao

onde:
nome_da_funcao -> sempre, com letras minusculas, e se for nome composto, separado por underline
parametros_entradas -> opcionais, onde tendo, mas de um,cada um separado por vírgula, podendo ser opcionais ou não
bloco_da_funcao -> também chamado de corpo da funcção ou implementeção, é onde o processamento da função acontece.

obs: veja que para definir uma função, tuilizamos a palavra reservada 'def' informando ao python que estamos definindo uma
função. também abrimos o bloco de codigo com o ja conhecido dois pontos : que é utilizado em python para definir blocos
"""
# exemplo de utilizacao de função
cores = ['verde','amarelo','azul','branco']

# utilizando a função integrada do python
print(cores)

curso = 'programao em python'
print(curso)

cores.append('roxo')
print(cores)

# curso.append('mais dados...') # AttributeError

cores.clear()
print(cores)

# print(help(print))
