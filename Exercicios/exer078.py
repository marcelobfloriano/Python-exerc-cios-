valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c} valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] < menor:
            menor = valores[c]
        elif valores[c] > maior:
            maior = valores[c]

print(f'Voce digitou os valores{valores}')
print(f'{menor} foi o menor valor nas posiçoes -> ', end='')
for cont, v in enumerate(valores):
    if v == menor:
        print(f'{cont}...', end='')
print()
print(f'{maior} foi o maior valor nas posiçoes -> ', end='')
for cont, v in enumerate(valores):
    if v == maior:
        print(f'{cont}...', end='')