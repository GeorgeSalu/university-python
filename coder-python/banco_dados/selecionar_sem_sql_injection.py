#!/usr/local/bin/python3
from bd import nova_conexao

sql = "SELECT tel, nome FROM contatos WHERE nome LIKE %s"

with nova_conexao() as conexao:
        nome = input('Contato a localizar: ')
        args = (f'%{nome}%',)

        cursor = conexao.cursor()
        cursor.execute(sql, args)

        for contato in cursor:
            print(contato)