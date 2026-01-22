"""
Documentando funções com Docstrings
obs: podemos ter acesso à documentação de uma função em python
utilizando a propriedade especial __doc__

podemos ainda fazer acesso à documentação com a função help
"""
# exemplos

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

def exponencial(numero,potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a potencia informada
    :param numero: Numero que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial, por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero**potencia