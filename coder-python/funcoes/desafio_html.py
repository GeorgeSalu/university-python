#!/usr/local/bin/python3
def tag(tag, *args, **kwargs):
    pass


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'curso de python 3'),
            tag('strong', 'juracy filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitao', id='ll'),
            tag('span', '.'),
            html_class='alert'
        )
    )


"""
retorno esperado
<p class="alert"><span >Curso de Python 3, por </span><strong id="jf">Juracy Filho</strong><span > e </span><strong id=
"ll">Leonardo Leitão</strong><span >.</span></p>
"""