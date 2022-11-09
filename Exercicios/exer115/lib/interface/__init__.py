def leiaInt(msg):
    while True:
        try:
            entrada = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite um numero INTEIRO valido!!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[33mEntrada de dados intemrrompida pelo usuario\033[m')
            return 0
        else:
            return entrada


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opão: ')
    return opc