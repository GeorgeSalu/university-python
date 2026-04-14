#!/usr/local/bin/python3
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contatos = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contatos_grupos = {
    'Bia alterada': 'Casa',
    'Lu': 'Trabalho',
    'Gui': 'Casa',
    'Beca': 'Trabalho',
    'Lucas': 'Casa',
    'Bia': 'Trabalho',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contatos_grupos.items():
            cursor.execute(selecionar_grupo, ( grupo, ))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contatos, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')
    else:
        print('contatos associados')