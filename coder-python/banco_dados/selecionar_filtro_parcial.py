#!/usr/local/bin/python3
from bd import nova_conexao

sql = "SELECT tel, nome FROM contatos WHERE nome LIKE '%a%'"

with nova_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql)

        for contato in cursor:
            print(contato)