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

Em Python, para definir uma classe utilizamos a palavra reservada class.

obs: utilizamos a palavra pass em python quando temos um bloco de codigo que ainda não está implementado

obs: quando nomeamos as nossas classes em python utilizamos por convênçõ o nome com inicial em maiusculo.
se o nome for composto, utuliza-se as iniciais de ambas as palavras em maiusculo, todas juntas

obs geek: em computação não utilizamos: acentuação, caracteres especiais, espaços oi similares para nomes
de classes, atributos, metodos, arquivos, diretorios e etc

obs: quando estamos planejando um software e definimos quais classe teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade
"""
class Lampada:
    pass

class ContaCorrente:
    pass

lamp = Lampada()
print(type(lamp))