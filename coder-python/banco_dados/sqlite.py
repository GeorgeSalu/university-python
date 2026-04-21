#!/usr/local/bin/python3
from sqlite3 import connect, ProgrammingError

tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(30)
    )
"""

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50),
        tel VARCHAR(40),
        grupo_id INTEGER,
        FOREIGN KEY (grupo_id) REFERENCES grupos(id)
    )
"""

insert_grupos = """
    INSERT INTO 
        grupos (descricao) 
    VALUES (?)
"""
insert_contatos = """
    INSERT INTO 
        contatos (nome, tel, grupo_id) 
    VALUES (?, ?, ?)
"""

select_grupos = """
     SELECT id,
       descricao
     FROM   grupos  
"""
select_contatos = """
    SELECT
        grupos.descricao AS grupo,
        contatos.nome AS contato
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, contato
"""