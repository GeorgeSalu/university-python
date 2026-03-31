#!/usr/local/bin/python3
from mysql.connector import ProgrammingError
from bd import nova_conexao

tabela_contatos = """
    CREATE TABLE contatos (nova VARCHAR(50), telm VARCHAR(40));
"""

tabela_emails = """
    CREATE TABLE emails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)
    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')