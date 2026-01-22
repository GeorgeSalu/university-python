"""
**Kwargs

Poderiamos chamar este parametro de **xis, m por convenção chamamos de **kwargs

Este é so, mas um parametro, mas diferente do *args que coloca os valores extras
em tuplas, o **kwargs exige que utilizemos parametros nomeados, e transforma esses
paramatros extras em um dicionário
"""
# exemplos

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos='verde',julia='amarelo',fernando='azul',vanessa='branco')