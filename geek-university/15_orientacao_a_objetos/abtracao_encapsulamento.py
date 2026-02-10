"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular o nosso codigo dentro de um grupo logico e hierarquico utilizando
classes.

Encapsular -> capsula

            classes
------------------------------------------
|                                         |
|           atributos e metodos           |
|                                         |
-------------------------------------------
# Relembrando atributos/metodos privados em python
Imagine que temos uma classe chamada Pessoa.contendo um atributo privado chamado __nome e um metodo
privado chamado __falar()

Esses elementos privados so devem/deveriam ser acessados dentro da classe.mais python não bloqueia este
acesso fora da classe. com python acontecendo um fenomeno chamado Name Mangling, que faz uma alteração na
forma de se acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa_nome
instancia._Pessoa_falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e metodos
privados de usuario
"""
class Conta:

    contador = 400

    def __init__(self, titular, limite, saldo):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('o valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('saldo isuficiente')
        else:
            print('o valor deve ser positivo')

# testando
conta1 = Conta('geek',150.00, 1500)

print(conta1.__dict__)

conta1.depositar(150)
print(conta1.__dict__)

conta1.sacar(-200)
print(conta1.__dict__)