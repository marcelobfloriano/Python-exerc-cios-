nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2022 - nascimento
if idade <= 9:
    print('Com {} anos voce esta na categoria MIRIM!!!'.format(idade))
elif 9 < idade <= 14:
    print('Com {} anos voce esta na categoria INFANTIL!!!'.format(idade))
elif 14 < idade <= 19:
    print('Com {} anos voce esta na categoria JUNIOR!!!'.format(idade))
elif 19 < idade <= 25:
    print('Com {} anos voce esta na categoria SENIOR!!!'.format(idade))
else:
    print('Com {} anos voce esta na categoria MASTER!!!'.format(idade))

