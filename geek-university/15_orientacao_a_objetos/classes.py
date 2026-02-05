"""
POO - Classes

Em POO,Classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente

Imagine que você queira fazer um sistema para automatizar o controle das lampadas da sua casa

Classes podem conter:
    - atributos -> representam as caracteristicas do objeto. Ou seja. Pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lampada, possivelmente iriamos
    querer saber se a lampada é de 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor,
    qual é a luminosidade dela, etc.

    - Metodos (funções) -> Representam os comportamentos do objeto. ou seja, as ações que este objeto pode
    realizar no seu sistema. No caso da lampada. Por exemplo, um comportamento comum que muito provavelmente
    iriamos querer representar no nosso sistema é o do ligar e desligar

"""
class Lampada:
    pass


lamp = Lampada()
print(type(lamp))