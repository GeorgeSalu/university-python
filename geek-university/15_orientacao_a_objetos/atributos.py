"""
POO - atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
conseguimo-nos representar computacionalmente os estados de um objeto

Em python, dividimos os atributos em 3 grupos:
    - atributos de instância
    - atributos de classe
    - atributos dinamicos

# atributos de instância: são atributos declarados dentro do metodo construtor
# obs: metodo contrutor: é um metodo especial utilizado para construção do objeto

em python, por conveção, ficou estabelecido que, todo atributo de uma classe é publico
ou seja, pode er acessado em todo o projeto
caso queiramos demostrar que determinado atributo deve ser tratado como provado, ou seja
que deve ser acessado/utilizado somente dentro da propria classe onde está declarado, utiliza-se
__ duplo underscore no inicio de seu nome, isso é conhecido também como Name Mangling
"""
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# atributos publicos e atributos privados
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostrar_senha(self):
        print(self.__senha)

    def mostrar_email(self):
        print(self.email)

# obs: lembre-se que isso é apenas uma convenção, ou seja,a linguagem python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe

# exemplo

user = Acesso('teste@gmail.com', '12323')
print(user.email)
# print(user.__senha) AttributeError
#print(user._Acesso__senha) # temos acesso, mas não deveriamos fazer esse acesso (Name Mangling)
user.mostrar_senha()
user.mostrar_email()

# o que significa atributos de instancias ?

# significa que ao criarmos instancias/objetos de uma classe, todas as instâncias term estes
# atributos

user1 = Acesso('aluno@gmail.com','1234')
user2 = Acesso('aluno2@gmail.com','1234')

user1.mostrar_email()
user2.mostrar_email()

# Atributos de classe
p1 = Produto('PlayStattion 4','video game', 2500)
p1 = Produto('xbox S','video game', 4500)

# Atributos de classes, são atributos, clarro, que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe, Ou seja, ao inves de instâncias da classe ter os seus próprios valores
# como é o caso dos atributos de instâncias, com os atributos de classe todas as instâncias teram o
# mesmo valor para este atributo

class Produto2:

    # atributo de classe
    imposto = 1.05 # 0.5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto2.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto2.imposto)
        Produto2.contador = self.id

p1 = Produto2('PlayStattion 4','video game', 2500)
p2 = Produto2('xbox S','video game', 4500)

print(p1.imposto)
print(p2.imposto)

# obs: não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto2.imposto) # acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# obs: em linguagens como o java, os atributos conhecidos como atributos de classe aqui em python
# são chamados atributos estáticos

# Atributos dinamicos -> Um atributo de instância pode ser criado em tempo de execução

# obs: o atributo dinamico será exclusivo da instancia que o criou

p1 = Produto('PlayStattion 4','video game', 2500)
p2 = Produto('xbox S','video game', 4500)

# criando um atributo dinamico em tempo de execução

p2.peso = '5kg'
print(f'Produto: {p2.nome}: Descricao: {p2.descricao} Valor: {p2.valor}, Peso: {p2.peso}')

# deletando atributos
print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)