#!/usr/local/bin/python3
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Lucas', '98765-4321'),
    ('Bia', '98765-1111'),
    ('Lu', '1111-4321'),
    ('Gui', '98765-2222'),
    ('Beca', '98765-3333')
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('registro incluído, ID:', cursor.rowcount)