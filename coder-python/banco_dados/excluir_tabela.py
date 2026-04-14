#!/usr/local/bin/python3
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute("DROP TABLE IF EXISTS emails")
    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')