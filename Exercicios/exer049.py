tabuada = int(input("Digite o numero da tabuada: "))
print('TABUADA DO {}'.format([tabuada]))
for c in range(1, 11):
    print('{} X {} = {}'.format(c, tabuada, (c * tabuada)))
