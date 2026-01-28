"""
Levantando os proprios erros com raise

raise -> Lança exceções

obs: O raise não é uma função. é uma palavra reservada, assim como def ou qualquer outra em python
Para simplificar, pense no raise como sendo util pra que possamos criar as nossas proprias exceções e mensagens
de error.

A forma geral de utilização é:
raise TipoDoErro('mensagem de erro')
"""
# exemplo real
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'o texto {texto} sera impresso na cor {cor}')

colore('geek',4)