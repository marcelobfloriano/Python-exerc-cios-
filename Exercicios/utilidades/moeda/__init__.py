def aumentar(a=0,b=0, formatado=False):
    res = ((a * b) /100) + a
    return res if formatado==False else moeda(res)


def diminuir(a=0,b=0, formatado=False):
    res = a - ((a* b) / 100)
    return res if formatado==False else moeda(res)


def dobro(a=0, formatado=False):
    res = a * 2
    return res if formatado==False else moeda(res)


def metade(a=0, formatado=False):
    res = a / 2
    return res if formatado==False else moeda(res)


def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:>2.2f}'.replace('.',',')


def resumo(a=0,ba=0,bd=0):
    print('-' * 36)
    print(f'RESUMO DO VALOR'.center(36))
    print('-' * 36)
    print(f'Preço analisado -> \t{moeda(a)}')
    print(f'O dobro -> \t\t{dobro(a, True)}')
    print(f'Metade do valor -> \t{metade(a, True)}')
    print(f'Acrescimo de {ba}% -> \t{aumentar(a,ba, True)}')
    print(f'Diminuindo {bd}% -> \t{diminuir(a,bd, True)}')
    print('-' * 36)