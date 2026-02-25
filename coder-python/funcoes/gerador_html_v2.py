def tag_bloco(text0, classe='success',inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{text0}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info',True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))