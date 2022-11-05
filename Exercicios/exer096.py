def area(a, b):
    m2 = a * b
    print(f'A area do terreno de {a} x {b} é de {m2} m².')

print('CONTROLE DE TERRENOS')
print('-' * 25)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)
