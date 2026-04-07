#!/usr/local/bin/python3
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    SELECT
        grupos.descricao as grupo,
        contatos.nome as contato
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, contato
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]} - {contato["contato"]}')