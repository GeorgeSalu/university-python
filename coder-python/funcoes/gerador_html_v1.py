#!/usr/local/bin/python3
def tag_bloco(text0, classe='success'):
    return f'<div class="{classe}">{text0}</div>'


if __name__ == '__main__':
    # testes (assertions)
    assert tag_bloco('Incluindo com sucesso') == '<div class="success">Incluindo com sucesso</div>'
    assert tag_bloco('impossivel excluir','error') == '<div class="error">impossivel excluir</div>'
    print(tag_bloco('bloco'))