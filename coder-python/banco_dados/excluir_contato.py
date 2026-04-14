#!/usr/local/bin/python3
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = "DELETE FROM contatos WHERE nome = %s"
args = ('Lucas',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as erro:
        print(f'ERRO: {erro.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s).')