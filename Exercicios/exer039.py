nascimento = int(input('Digite seu ano de nascimento:'))
idade = 2022 - nascimento
anoAlistamento = nascimento + 18
if idade < 18:
        print('Com {} anos voce ainda nao tem idade para alistar, faltam {} ano(s) '.format(idade, (18 - idade)))
        print('Seu alistamento sera em {}'.format(anoAlistamento))
elif idade == 18:
    print('Com {} anos voce esta na idade certa de se alistar'.format(idade))
else:
    print('Com {} anos, seu alistamento ja se passou {} ano(s)'.format(idade, (idade - 18)))
    print('Seu alistamento foi em {}'.format(anoAlistamento))