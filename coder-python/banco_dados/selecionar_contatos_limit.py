#!/usr/local/bin/python3
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos LIMIT 5'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')
    else:
        for contato in contatos:
            print(f'id : {contato[2]:2d} - Nome: {contato[0]:20s} - Telefone: {contato[1]}')