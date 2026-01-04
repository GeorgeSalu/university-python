"""
crie uma funcao que recebe outra como parametro
a que vai receber parametros deve receber um nome,uma idade e uma profisao
a funcao de argumentos deve apresentar estes dados em uam string dinamica
"""
def reune_dados(nome, idade, profisao,fnct):
    apresentacao = fnct(nome, idade, profisao)
    return apresentacao

def apresenta_dados(nome, idade, profisao):
    frase = "O nome do usuario %s e sua idade é %d e ele é um %s" % (nome, idade, profisao)
    return frase

print(reune_dados("matheus", 18, "programador", apresenta_dados))

apresentacao = reune_dados("pedro",40,"engenheiro",apresenta_dados)
print(apresentacao)