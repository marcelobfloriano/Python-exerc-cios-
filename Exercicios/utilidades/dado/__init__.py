def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO!! \"{entrada}"\ é um Preço Invalido')
        else:
            valido = True
            return float(entrada)


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


def leiaFloat(msg):
    while True:
        try:
            entrada = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mDigite um numero REAL valido!!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[33mEntrada de dados intemrrompida pelo usuario\033[m')
            return 0
        else:
            return entrada


def menu(opcao):
    print('-' * 30)
    print('MENU PRINCIPAL'.center(30))
    print('-' * 30)
    print(f'\\33[33m1\\33[m - \\33[32mVer pessoas cadastradas\\33[m')
    print(f'\\33[33m2\\33[m - \\33[32mCadastrar nova pessoa\\33[m')
    print(f'\\33[33m3\\33[m - \\33[32mSair do Sistema\\33[m')
    res = leiaInt('\\33[33mSua Opção:{opcao}\\33[m')
