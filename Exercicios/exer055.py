maiorPeso = 0
menorPeso = 0
for c in range(0, 5):
    peso = float(input('Peso da {}ª pessoa(KG): '.format(c + 1)))
    if c == 0:
        maiorPeso = peso
        menorPeso = peso
    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso
print('O maior peso foi {:.2f} KG'.format(maiorPeso))
print('O menor peso foi {:.2f} KG'.format(menorPeso))